import os
from pathlib import Path, PosixPath

import dotenv

dotenv.load_dotenv()


class DataPathError(Exception):
    """Raised when the DATA_PATH environment variable is missing or invalid."""


class InvalidDataFolder(Exception):
    """Raised when an expected subfolder does not exists."""


if not os.getenv("DATA_PATH"):
    raise DataPathError("Must provide a DATA_PATH, i.e., the path to the data folder.")

DATA_PATH = Path(os.getenv("DATA_PATH"))

if not DATA_PATH.exists():
    raise InvalidDataFolder(f"The DATA_PATH does not exists: {DATA_PATH}")

# RAW_DATA = DATA_PATH / "0_raw_data"

# RAW_DATA_DECISIONS = RAW_DATA / "0_decisions"
# DE_DECISIONS_DOWNLOAD_TOC = RAW_DATA_DECISIONS / "de_rii_toc.xml"
# DE_DECISIONS_DOWNLOAD_ZIP = RAW_DATA_DECISIONS / "0_input"
# DE_DECISIONS_DOWNLOAD_XML = RAW_DATA_DECISIONS / "1_xml"


# RAW_DATA_STATUTES = RAW_DATA / "1_statutes"
# DE_STATUTES_DOWNLOAD_TOC = RAW_DATA_STATUTES / "de_rii_toc.xml"
# DE_STATUTES_DOWNLOAD_ZIP = RAW_DATA_STATUTES / "0_input"
# DE_STATUTES_DOWNLOAD_XML = RAW_DATA_STATUTES / "1_xml"

# for folder in [
#     DE_DECISIONS_DOWNLOAD_ZIP,
#     DE_DECISIONS_DOWNLOAD_XML,
#     DE_STATUTES_DOWNLOAD_ZIP,
#     DE_STATUTES_DOWNLOAD_XML,
# ]:
#     folder.mkdir(exist_ok=True, parents=True)

PREPROCESSED_DATA = DATA_PATH / "1_preprocessed_data"
PREPROCESSED_DATA_DECISIONS = PREPROCESSED_DATA / "1_decisions"
PREPROCESSED_DATA_STATUTES = PREPROCESSED_DATA / "2_statutes"
PREPROCESSED_DATA_COMBINED = PREPROCESSED_DATA / "3_combined"

if not PREPROCESSED_DATA.exists():
    raise InvalidDataFolder(
        'Expected folder "1_preprocessed_data". Are you sure you have correctly set the DATA_PATH to be the actual data folder?'
    )

PREPROCESSED_DATA.mkdir(exist_ok=True)

for folder in [
    PREPROCESSED_DATA_DECISIONS,
    PREPROCESSED_DATA_STATUTES,
    PREPROCESSED_DATA_COMBINED,
]:
    folder.mkdir(exist_ok=True, parents=True)

COMPUTATION_PATH = DATA_PATH / "2_network_data"

if not COMPUTATION_PATH.exists():
    raise InvalidDataFolder(
        'Expected folder "2_network_data". Are you sure you have correctly set the DATA_PATH to be the actual data folder?'
    )
