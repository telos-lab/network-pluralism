import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()


BASE_PATH = Path(os.getenv("DATA_PATH", "."))
DATA_PATH = BASE_PATH / "network_pluralism_data"
DATA_PATH.mkdir(exist_ok=True)
