import re
import streamlit as st
import html2text
from bs4 import BeautifulSoup
from md_to_plain_text.extensions import EscapedNewLineToLinebreakExtension
from markdown import Markdown

st.title('Markdown → HTML → Plain Text')
st.text('Experimenting with conversion of markdown to HTML and exporting plain text')
EXAMPLE_MARKDOWN = """
# Header 1

some line of text

another line of tekst with a [link](https://www.streamlit.io)

A line of text with a\
soft line break

- Unordered list item 1

- Unordered list item 2

- Unordered list item 3
- Unordered list item 4

1. Ordered list item 1
2. Ordered list item 2

3. Ordered list item 3

"""
markdown = st.text_area('Enter Markdown', value=EXAMPLE_MARKDOWN, height=200)

st.sidebar.markdown('### Markdown Features')
st.selectbox

md_converter = Markdown(extensions=[EscapedNewLineToLinebreakExtension()])

## Disable markdown features based on user input
if not st.sidebar.checkbox('Header'):
    md_converter.parser.blockprocessors.deregister('hashheader')

if not st.sidebar.checkbox('Blockquote'):
    md_converter.parser.blockprocessors.deregister('quote')

if not st.sidebar.checkbox('Ordered List'):
    md_converter.parser.blockprocessors.deregister('olist')

if not st.sidebar.checkbox('Unordered List'):
    md_converter.parser.blockprocessors.deregister('ulist')

# do markdown conversion
html = md_converter.convert(markdown)


with st.expander('HTML'):
    # print html code
    st.markdown(f"```html\n{html}\n```")

    # reset bottom margins of paragraphs to zero
    st.write("<style>p {margin-bottom: 0;}</style>", unsafe_allow_html=True)

    # render html
    st.write(html, unsafe_allow_html=True)

# configure html2text
html2text.config.BODY_WIDTH = 0
html2text.config.SINGLE_LINE_BREAK = True

# do html to plain text conversion
plaintext = html2text.html2text(html)

# add an escaped newline character for visualisation of the 'characters' only
escaped_plain_text = re.sub('\n$', '\\n\n', plaintext)

with st.expander('Plain Text'):
    # print plain text 'characters'
    st.markdown(f"```plaintext\n{escaped_plain_text}\n```")
    # render plain text
    st.text(plaintext)
