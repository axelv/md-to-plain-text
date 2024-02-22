## Markdown → HTML → Plain Text

This repository contains a Streamlit app to discover the nuances in converting markdown to html to plain text.
At [Tiro.health](https://tiro.health) we use markdown as the data format to store rich text. Converting this to different formats (PDF, plain text, etc.) is a common requirement. This repository is an attempt to understand the nuances in this conversion process.

## Observations

1. empty lines are hard to maintain => combination of hard and soft breaks??
2. single line breaks for paragraphs require disabling of line wrapping. Is this OK?
