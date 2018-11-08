# Based on pygments documentation
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ['PrometheusLexer']

class PrometheusLexer(RegexLexer):
    name = 'Prometheus'
    aliases = ['prom', 'prometheus']
    filenames = ['*.prom']

    tokens = {
        'root': [
            (r'^#.*$', Comment),
            (r'[a-zA-Z0-9_]+', Name.Tag, ('maybe_dimensions')),
        ],
        'value': [
            (r'[0-9]+(\.[0-9]+(e[-+][0-9]+)?)?$', Number.Float),
        ],
        'maybe_dimensions': [
            (r'\s+', Text, ('#pop', 'value')),
            (r'\{', Punctuation, 'dimensions'),
            (r'\}', Punctuation, '#pop'),
        ],
        'dimensions': [
            (r',', Punctuation),
            (r'\}', Punctuation, '#pop'),
            (r'([^=}]+)(=)("[^"]*")',
                bygroups(Name.Attribute, Operator, String.Double)),
        ],
    }

