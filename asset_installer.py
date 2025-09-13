import requests
from bs4 import BeautifulSoup
import zipfile
import io
import os

EXTRACT_PATH = "pirate-pack"
PAGE_URL = "https://kenney.nl/assets/pirate-pack"
response = requests.get(PAGE_URL, timeout=5)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
zip_links: list[str] = [
    a["href"]
    for a in soup.find_all("a")
    if "href" in a.attrs and a["href"].endswith(".zip")
]

if zip_links:
    link = zip_links[0]
    if link.startswith("/"):
        link = "https://kenney.nl" + link
    print(f"Downloading from: {link}")

    # Download the zip file
    resp = requests.get(link, timeout=5)
    resp.raise_for_status()

    # Unzip in memory and extract all contents
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zipped:
        os.makedirs(EXTRACT_PATH, exist_ok=True)
        zipped.extractall(path=EXTRACT_PATH)
        print(f"Extracted files to folder: {EXTRACT_PATH}")
else:
    print("No direct ZIP download link found.")
