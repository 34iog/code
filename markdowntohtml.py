# https://gist.github.com/mc-interviews/305a6d7d8c4ba31d4e4323e574135bf9

import re

class MarkdownToHTMLConverter:
    
    def __init__(self):
        self.MIN_HEADER = 0
        self.MAX_HEADER = 6

    def starts_with_hashes(self, line):
        return bool(re.match(r'^#+\s', line)) # ensures there is a space after the hash

    def convert(self, markdown_text):
        lines = markdown_text.splitlines()
        html_lines = []
        current_paragraph = []

        for line in lines:
            line = line.strip()

            # ignore blank lines
            if not line:
                if current_paragraph:
                    html_lines.append('<p>' + ' '.join(current_paragraph).strip() + '</p>')
                    current_paragraph = []
                continue

            # handle links in the format [text](url)
            line = self.convert_links(line)

            # handle headers (from h1 to h6)
            if self.starts_with_hashes(line):
                if current_paragraph:
                    html_lines.append('<p>' + ' '.join(current_paragraph).strip() + '</p>')
                    current_paragraph = []
                header_level = line.count("#", self.MIN_HEADER, self.MAX_HEADER)
                if header_level <= self.MAX_HEADER:
                    header_content = line[header_level:].strip()
                    html_lines.append(f"<h{header_level}>{header_content}</h{header_level}>")
                continue

            # add lines to current paragraph
            current_paragraph.append(line.strip())

        # add any remaining text as a paragraph
        if current_paragraph:
            html_lines.append('<p>' + ' '.join(current_paragraph).strip() + '</p>')

        return "\n".join(html_lines)  # use single newline for paragraph separation

    def convert_links(self, line):
        # use regex to find all occurrences of [text](url) or [] (url) patterns
        def replace_link(match):
            link_text = match.group(1) if match.group(1) is not None else ""
            link_url = match.group(2).strip()
            return f'<a href="{link_url}">{link_text}</a>'

        # replace all links in the line using regex
        line = re.sub(r'\[([^\]]*)\]\(([^)]+)\)|\[\]\(([^)]+)\)', 
                    lambda match: replace_link(match) if match.group(1) is not None else f'<p><a href="{match.group(3)}"></a></p>', 
                    line)
        return line

    def convert_links_iteratively(self, line):
        # find the starting link
        start_text = line.find('[')
        end_text = line.find(']', start_text)
        start_url = line.find('(', end_text)
        end_url = line.find(')', start_url)

        # convert all the links in the line
        while start_text != -1 and end_text != -1 and start_url != -1 and end_url != -1:
            link_text = line[start_text + 1:end_text]
            link_url = line[start_url + 1:end_url]
            link_html = f'<a href="{link_url.strip()}">{link_text}</a>'
            line = line[:start_text] + link_html + line[end_url + 1:]

            # find the next link
            start_text = line.find('[')
            end_text = line.find(']', start_text)
            start_url = line.find('(', end_text)
            end_url = line.find(')', start_url)

        return line
