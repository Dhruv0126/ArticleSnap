# ArticleSnap

## Overview
The **News Summarizer** application allows users to input a URL of a news article and get a summarized version of the article along with key metadata such as the title, authors, publishing date, and a sentiment analysis of the article's content. This tool is designed to save time and provide insights at a glance.

## Features
- Fetches the article from the given URL.
- Displays the article's title, authors, and publishing date.
- Summarizes the content of the article.
- Performs sentiment analysis on the article's text.

## Requirements
- Python 3.6+
- Libraries:
  - tkinter
  - nltk
  - textblob
  - newspaper3k

## Installation
1. Clone the repository or download the source code.
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Enter the URL of the news article in the provided text box.
3. Click the **Summarize** button.
4. View the summarized article, metadata, and sentiment analysis results.

## Files
- **main.py**: The main script for running the News Summarizer application.
- **requirements.txt**: Contains the list of required libraries and their versions.

## Example
1. Input a news article URL into the text box.
2. Click on "Summarize."
3. The application will display:
   - The article's title.
   - Authors of the article.
   - Publishing date.
   - A concise summary.
   - Sentiment analysis with polarity and sentiment type (positive, negative, or neutral).

## Limitations
- The summarization and sentiment analysis are dependent on the quality of the fetched article.
- Requires an active internet connection to fetch the news article.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

## Acknowledgments
- [TextBlob](https://textblob.readthedocs.io/)
- [newspaper3k](https://newspaper.readthedocs.io/)

---
Feel free to contribute to the project by submitting issues or pull requests!

