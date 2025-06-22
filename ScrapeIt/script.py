import streamlit as st
import pandas as pd
import requests

def search_github_repos(keyword, language, sort_by='stars', per_page=20):
    url = "https://api.github.com/search/repositories"
    query = f"{keyword} language:{language}"
    params = {
        'q': query,
        'sort': sort_by,
        'order': 'desc',
        'per_page': per_page
    }
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        st.error("GitHub API error: " + response.json().get("message", "Unknown error"))
        return pd.DataFrame()
    items = response.json().get('items', [])
    data = []
    for repo in items:
        data.append({
            'repo_name': repo['full_name'],
            'repo_link': repo['html_url'],
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count']
        })
    return pd.DataFrame(data)

st.title("GitScrape")

keyword = st.text_input("Enter repo or any keyword (e.g., machine learning):")
language = st.text_input("Enter programming language (e.g., python):")
sort_by = st.selectbox("Sort by", ['stars', 'forks'])
per_page = st.slider("Number of results", min_value=5, max_value=150, value=20)

if st.button("Search"):
    if not keyword:
        st.warning("Please enter repo or any keyword.")
    else:
        df = search_github_repos(keyword, language, sort_by, per_page)
        if not df.empty:
            st.markdown("### Results")
            # Only repo_link is clickable, repo_name is plain text
            def make_clickable_link(link):
                return f'<a href="{link}" target="_blank" title="Click for the repo link" style="text-decoration:none; color:#1f77b4; font-weight:bold;">{link}</a>'
            df['repo_link_clickable'] = df['repo_link'].apply(make_clickable_link)
            st.write(
                df[['repo_name', 'repo_link_clickable', 'stars', 'forks']].to_html(
                    escape=False, index=False, header=["Repo Name", "Repo Link", "Stars", "Forks"]
                ),
                unsafe_allow_html=True
            )
            # CSV download (plain text, no HTML)
            csv = df[['repo_name', 'repo_link', 'stars', 'forks']].copy()
            csv = csv.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download repo list as CSV",
                data=csv,
                file_name='github_repos.csv',
                mime='text/csv'
            )
        else:
            st.info("No repositories found. Try different keywords or language.")
