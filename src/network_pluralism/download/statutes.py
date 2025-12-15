import os
import zipfile
from multiprocessing.pool import Pool

import requests
from bs4 import BeautifulSoup
from quantlaw.utils.files import ensure_exists
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from network_pluralism.setup.paths import (
    DE_STATUTES_DOWNLOAD_TOC,
    DE_STATUTES_DOWNLOAD_XML,
    DE_STATUTES_DOWNLOAD_ZIP,
)

import time


def download_item(link_text):
    time.sleep(1)
    s = requests.Session()
    retries = Retry(
        total=10,
        backoff_factor=2,
    )
    s.mount("https://", HTTPAdapter(max_retries=retries))

    filename = f"{link_text.split('/')[-2]}.zip"
    if not os.path.isfile(f"{DE_STATUTES_DOWNLOAD_ZIP}/{filename}"):
        content = s.get(link_text).content
        print(f"Downloading {filename}.")

        with open(f"{DE_STATUTES_DOWNLOAD_ZIP}/{filename}", "wb") as f:
            f.write(content)
    else:
        print(f"{filename} Exists already")


def download_all_statutes():
    toc = requests.get("https://www.gesetze-im-internet.de/gii-toc.xml").text

    with open(DE_STATUTES_DOWNLOAD_TOC, "w") as f:
        f.write(toc)

    with open(DE_STATUTES_DOWNLOAD_TOC) as f:
        toc = f.read()

    soup = BeautifulSoup(toc, "lxml-xml")
    len(soup.findAll("item"))

    ensure_exists(DE_STATUTES_DOWNLOAD_ZIP)
    items = [i.link.text for i in soup.findAll("item")][:10]
    with Pool(4) as p:
        p.map(download_item, items)

    ensure_exists(DE_STATUTES_DOWNLOAD_XML)

    i = 0
    for filename in os.listdir(DE_STATUTES_DOWNLOAD_ZIP):
        statute_folder = DE_STATUTES_DOWNLOAD_XML / filename.split(".")[0]
        ensure_exists(statute_folder)
        if os.path.splitext(filename)[1] == ".zip":
            zip_ref = zipfile.ZipFile(f"{DE_STATUTES_DOWNLOAD_ZIP}/{filename}", "r")
            zip_ref.extractall(statute_folder)
            zip_ref.close()
            i += 1
            print(f"\r{i} entpackt", end="")


if __name__ == "__main__":
    download_all_statutes()
