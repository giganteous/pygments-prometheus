import unittest

from pygments import highlight
from pygments.formatters import HtmlFormatter

from prom import PrometheusLexer

with open('metrics.prom') as fh: sample = fh.read()

class TestSample(unittest.TestCase):
    def test_Html(self):
        html = highlight(sample, PrometheusLexer(), HtmlFormatter())

        self.assertFalse('class="err"' in html, "errors were found in the pygments output")

if __name__ == '__main__':
    unittest.main()

