import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()


BASE_PATH = Path(os.getenv("DATA_PATH", "."))
DATA_PATH = BASE_PATH / "network_pluralism_data"
DATA_PATH.mkdir(exist_ok=True)

RAW_DATA = DATA_PATH / "0_raw_data"

RAW_DATA_DECISIONS = RAW_DATA / "0_decisions"
DE_DECISIONS_DOWNLOAD_TOC = RAW_DATA_DECISIONS / "de_rii_toc.xml"
DE_DECISIONS_DOWNLOAD_ZIP = RAW_DATA_DECISIONS / "0_input"
DE_DECISIONS_DOWNLOAD_XML = RAW_DATA_DECISIONS / "1_xml"


RAW_DATA_STATUTES = RAW_DATA / "1_statutes"
DE_STATUTES_DOWNLOAD_TOC = RAW_DATA_STATUTES / "de_rii_toc.xml"
DE_STATUTES_DOWNLOAD_ZIP = RAW_DATA_STATUTES / "0_input"
DE_STATUTES_DOWNLOAD_XML = RAW_DATA_STATUTES / "1_xml"

for folder in [
    DE_DECISIONS_DOWNLOAD_ZIP,
    DE_DECISIONS_DOWNLOAD_XML,
    DE_STATUTES_DOWNLOAD_ZIP,
    DE_STATUTES_DOWNLOAD_XML,
]:
    folder.mkdir(exist_ok=True, parents=True)

PREPROCESSED_DATA = DATA_PATH / "1_preprocessed_data"
PREPROCESSED_DATA.mkdir(exist_ok=True)


COMPUTATION_PATH = DATA_PATH / "2_network_data"
COMPUTATION_PATH.mkdir(exist_ok=True, parents=True)
