"""
https://markdowntohtml.com/
https://dillinger.io/
"""

import unittest, re
from markdowntohtml import MarkdownToHTMLConverter

class TestMarkdownToHTMLConverter(unittest.TestCase):

    def setUp(self):
        self.converter = MarkdownToHTMLConverter()

    def test_single_h1(self):
        markdown = "# Header 1"
        expected_html = "<h1>Header 1</h1>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_single_h2(self):
        markdown = "## Header 2"
        expected_html = "<h2>Header 2</h2>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_single_space_h2(self):
        markdown = " ## Header 2"
        expected_html = "<h2>Header 2</h2>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_h6(self):
        markdown = "###### Header 6"
        expected_html = "<h6>Header 6</h6>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_header_with_no_space(self):
        markdown = "#HeaderWithoutSpace"
        expected_html = "<p>#HeaderWithoutSpace</p>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_hashtag_in_header(self):
        markdown = "###### Header ###6"
        expected_html = "<h6>Header ###6</h6>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_multiple_headers(self):
        markdown = "# Header 1\n## Header 2\n###### Header 6"
        expected_html = "<h1>Header 1</h1>\n<h2>Header 2</h2>\n<h6>Header 6</h6>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_paragraph(self):
        markdown = "This is a simple paragraph."
        expected_html = "<p>This is a simple paragraph.</p>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_multiple_paragraphs(self):
        markdown = "This is the first paragraph.\n\nThis is the second paragraph."
        expected_html = "<p>This is the first paragraph.</p>\n<p>This is the second paragraph.</p>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_ignore_blank_lines(self):
        markdown = "This is a paragraph.\n\nAnother paragraph.\n\n\n"
        expected_html = "<p>This is a paragraph.</p>\n<p>Another paragraph.</p>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_inline_link(self):
        markdown = "This is a [link](http://example.com)."
        expected_html = '<p>This is a <a href="http://example.com">link</a>.</p>'
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_inline_link_in_header(self):
        markdown = "## This is a header [with a link](http://example.com)"
        expected_html = '<h2>This is a header <a href="http://example.com">with a link</a></h2>'
        self.assertEqual(self.converter.convert(markdown), expected_html)
    
    def test_multiple_links(self):
        markdown = "This is [link 1](http://example1.com) and [link 2](http://example2.com)."
        expected_html = '<p>This is <a href="http://example1.com">link 1</a> and <a href="http://example2.com">link 2</a>.</p>'
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_link_without_text(self):
        markdown = "[](http://example.com)"
        expected_html = '<p><a href="http://example.com"></a></p>'
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_link_with_spaces(self):
        markdown = "[ link with spaces ]( http://example.com )"
        expected_html = '<p><a href="http://example.com"> link with spaces </a></p>'
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_combined_headers_paragraphs_and_links(self):
        markdown = """
# Header one

This is a paragraph [with an inline link](http://google.com). Neat, eh?

## Another Header

Another paragraph with [another link](http://example.com).
"""
        expected_html = """<h1>Header one</h1>
<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>
<h2>Another Header</h2>
<p>Another paragraph with <a href="http://example.com">another link</a>.</p>"""
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_no_markdown(self):
        markdown = "Just some plain text."
        expected_html = "<p>Just some plain text.</p>"
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_empty_input(self):
        markdown = ""
        expected_html = ""
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_only_blank_lines(self):
        markdown = "\n\n\n"
        expected_html = ""
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_headers_and_links(self):
        markdown = """
            # Sample Document

            Hello!
            
            This is sample markdown for the [Mailchimp](https://www.mailchimp.com) homework assignment.""".strip()
        expected_html = """<h1>Sample Document</h1>\n<p>Hello!</p>\n<p>This is sample markdown for the <a href="https://www.mailchimp.com">Mailchimp</a> homework assignment.</p>"""
        self.assertEqual(self.converter.convert(markdown), expected_html)

    def test_headers_and_links2(self):
        markdown = """
# Header one

Hello there

How are you?
What's going on?

## Another Header

This is a paragraph [with an inline link](http://google.com). Neat, eh?

## This is a header [with a link](http://yahoo.com)""".strip()

        expected_html = """<h1>Header one</h1>
<p>Hello there</p>
<p>How are you? What's going on?</p>
<h2>Another Header</h2>
<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>
<h2>This is a header <a href="http://yahoo.com">with a link</a></h2>"""
        self.assertEqual(self.converter.convert(markdown), expected_html)


if __name__ == '__main__':
    unittest.main()
