import unittest
import time
from markdowntohtml import MarkdownToHTMLConverter

class TestMarkdownToHTMLConverterPerformance(unittest.TestCase):

    def setUp(self):
        self.converter = MarkdownToHTMLConverter()

    def test_performance_large_input(self):
        """
        Time taken for performance test: 0.0367 seconds
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.038s

        OK
        """
        large_markdown = "# Header 1\n\n" + "\n\n".join(["This is a paragraph with a [link](http://1.com)."] * 10000) + "\n\n" + \
                         "## Header 2\n\n" + "\n\n".join(["This is another paragraph with a [link](http://2.org)."] * 10000) + "\n\n" + \
                         "### Header 3\n\n" + "\n\n".join(["This is again another paragraph with a [link](http://3.net)."] * 10000)

        start_time = time.time()
        result = self.converter.convert(large_markdown)
        end_time = time.time()
        
        print(f"Time taken for performance test: {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    unittest.main()
