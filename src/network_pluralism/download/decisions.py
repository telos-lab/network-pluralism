import os
import zipfile
from multiprocessing.pool import Pool
import time
import requests
from quantlaw.utils.files import ensure_exists
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from network_pluralism.setup.paths import (
    DE_DECISIONS_DOWNLOAD_TOC,
    DE_DECISIONS_DOWNLOAD_XML,
    DE_DECISIONS_DOWNLOAD_ZIP,
)


def download_item(link_text):
    time.sleep(1)
    s = requests.Session()
    retries = Retry(
        total=10,
        backoff_factor=2,
    )
    s.mount("https://", HTTPAdapter(max_retries=retries))

    filename = link_text.split("/")[-1]
    if not os.path.isfile(f"{DE_DECISIONS_DOWNLOAD_ZIP}/{filename}"):
        content = s.get(link_text).content
        print(f"Downloading {filename}.")

        with open(f"{DE_DECISIONS_DOWNLOAD_ZIP}/{filename}", "wb") as f:
            f.write(content)
    else:
        print(f"{filename} Exists already")


def download_all_decisions():
    toc = requests.get("https://www.rechtsprechung-im-internet.de/rii-toc.xml").text

    with open(DE_DECISIONS_DOWNLOAD_TOC, "w") as f:
        f.write(toc)

    with open(DE_DECISIONS_DOWNLOAD_TOC) as f:
        toc = f.read()

    soup = BeautifulSoup(toc, "lxml-xml")
    len(soup.findAll("item"))

    ensure_exists(DE_DECISIONS_DOWNLOAD_ZIP)
    items = [i.link.text for i in soup.findAll("item")][:10]

    existing_file_names = os.listdir(DE_DECISIONS_DOWNLOAD_ZIP)
    new_items = [
        item for item in items if item.split("/")[-1] not in existing_file_names
    ]
    with Pool(4) as p:
        p.map(download_item, new_items)

    ensure_exists(DE_DECISIONS_DOWNLOAD_XML)

    i = 0
    for filename in os.listdir(DE_DECISIONS_DOWNLOAD_ZIP):
        if os.path.splitext(filename)[1] == ".zip":
            try:
                zip_ref = zipfile.ZipFile(
                    f"{DE_DECISIONS_DOWNLOAD_ZIP}/{filename}", "r"
                )
                zip_ref.extractall(DE_DECISIONS_DOWNLOAD_XML)
                zip_ref.close()
                i += 1
                print(f"\r{i} entpackt", end="")
            except zipfile.BadZipFile:
                print(f"Bad Zip File: {filename}")
                continue


if __name__ == "__main__":
    download_all_decisions()
