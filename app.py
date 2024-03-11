import re
import streamlit as st
from bs4 import BeautifulSoup
from markdown import Markdown
from md_to_plain_text.html_to_plain_text import convert_html_to_plain_text
from md_to_plain_text.extensions import EscapedNewLineToLinebreakExtension
from md_to_plain_text.example_cases import EXAMPLES


st.title('Markdown → HTML → Plain Text')
st.text('Experimenting with conversion of markdown to HTML and exporting plain text')

st.sidebar.markdown('### Markdown Features')
st.sidebar.markdown('### Examples')
example_key = st.selectbox('Select an example', list(EXAMPLES.keys()))
if example_key in EXAMPLES:
    example_case = EXAMPLES[example_key].read_text()
else:
    example_case = ""

markdown = st.text_area('Enter Markdown', value=example_case, height=200)

md_converter = Markdown(extensions=[EscapedNewLineToLinebreakExtension()])
## Disable markdown features based on user input
if not st.sidebar.checkbox('Header'):
    md_converter.parser.blockprocessors.deregister('hashheader')


if not st.sidebar.checkbox('Ordered List'):
    md_converter.parser.blockprocessors.deregister('olist')

if not st.sidebar.checkbox('Unordered List'):
    md_converter.parser.blockprocessors.deregister('ulist')

if not st.sidebar.checkbox('Horizontal Rule'):
    md_converter.parser.blockprocessors.deregister('hr')

if not st.sidebar.checkbox('Setext-style Headers'):
    md_converter.parser.blockprocessors.deregister('setextheader')

if not st.sidebar.checkbox('Indent'):
    md_converter.parser.blockprocessors.deregister('indent')

if not st.sidebar.checkbox('Blockquote'):
    md_converter.parser.blockprocessors.deregister('quote')

if not st.sidebar.checkbox('Code Block'):
    md_converter.parser.blockprocessors.deregister('code')

if not st.sidebar.checkbox('Empty Blocks',True):
    md_converter.parser.blockprocessors.deregister('empty')

if not st.sidebar.checkbox('Paragraph', value=True):
    md_converter.parser.blockprocessors.deregister('paragraph')

if not st.sidebar.checkbox('Styling'):
    md_converter.inlinePatterns.deregister('em_strong')

if not st.sidebar.checkbox('Backtick'):
    md_converter.inlinePatterns.deregister('backtick')




bs = BeautifulSoup(markdown, 'html.parser')
# do markdown conversion
html = md_converter.convert(markdown)



with st.expander('HTML'):
    # print html code
    st.markdown(f"```html\n{html}\n```")

    # reset bottom margins of paragraphs to zero
    st.write("<style>p {margin-bottom: 0;}</style>", unsafe_allow_html=True)

    # render html
    st.write(html, unsafe_allow_html=True)

# do html to plain text conversion
plaintext = convert_html_to_plain_text(html)

# add an escaped newline character for visualisation of the 'characters' only
escaped_plain_text = re.sub('\n$', '\\n\n', plaintext)

with st.expander('Plain Text'):
    # print plain text 'characters'
    st.markdown(f"```plaintext\n{escaped_plain_text}\n```")
    # render plain text
    st.text(plaintext)
