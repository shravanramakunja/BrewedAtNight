# ScrapeIt

## Introduction
ScrapeIt is a Python-based Streamlit app for searching GitHub repositories by keyword and programming language. It uses the GitHub API to fetch repository data, processes the results with `pandas`, and allows users to view and download the results as a CSV file. The app displays results in a table where only the repository link is clickable, and the repository name is shown as plain text.

## What is Used?
- **streamlit**: For building the interactive web app interface.
- **requests**: To send HTTP requests to the GitHub API and fetch repository data.
- **pandas**: To organize, clean, and display the data in a tabular format, and to export results as CSV.

## Features
- Search GitHub repositories by keyword and programming language.
- Sort results by stars or forks.
- View results in a table with clickable repository links.
- Download the list of repositories as a CSV file (plain text, no HTML).
- User-friendly interface built with Streamlit.

## Requirements
- Python 3.x
- streamlit
- requests
- pandas

Install dependencies with:
```
pip install streamlit requests pandas
```

## Usage
1. Edit `main.py` if you want to change default settings or UI text.
2. Run the Streamlit app:
```
streamlit run main.py
```
3. Use the web interface to search for repositories and download results. The results table will show the repository name (plain text) and a clickable repository link.

## License
For personal and educational use.
