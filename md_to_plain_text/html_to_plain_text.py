from bs4 import BeautifulSoup

def convert_html_to_plain_text(html: str) -> str:
    """Converts HTML to plain text"""
    bs4 = BeautifulSoup(html, 'html.parser')

    # replace all <br> tags with newlines
    for br in bs4.find_all("br"):
        br.replace_with("\n")

    # replace all <p> tags with a \n

    return bs4.get_text("\n")
