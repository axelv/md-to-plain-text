from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class EscapedNewLineToLinebreak(Preprocessor):
    """Convert escaped newlines to HTML line breaks."""
    def run(self, lines):
        new_lines = []
        for line in lines:
            new_lines.append(re.sub(r'\\$', "<br/>", line))
        return new_lines

class EscapedNewLineToLinebreakExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(EscapedNewLineToLinebreak(md), 'escaped-new-line', 175)
