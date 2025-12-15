from pathlib import Path
import json
from scipy.sparse import save_npz, load_npz
from network_pluralism.setup.paths import COMPUTATION_PATH


def save_matrix(path, sparse_matrix, rows, columns):
    folder_path = path
    Path.mkdir(folder_path, exist_ok=True)
    save_npz(folder_path / "matrix", sparse_matrix)
    with open(folder_path / "rows.json", "w") as f:
        json.dump(rows, f)
    with open(folder_path / "columns.json", "w") as f:
        json.dump(columns, f)


def load_matrix(folder_path: Path = None, name: str = None, as_csr=False):
    if not folder_path:
        folder_path = COMPUTATION_PATH / name
    matrix = load_npz(folder_path / "matrix.npz")
    with open(folder_path / "rows.json", "r") as f:
        rows = json.load(f)
    with open(folder_path / "columns.json", "r") as f:
        columns = json.load(f)
    return matrix if not as_csr else matrix.tocsr(), rows, columns


def load_indices(folder_path: Path = None, name: str = None):
    if not folder_path:
        folder_path = COMPUTATION_PATH / name
    with open(folder_path / "rows.json", "r") as f:
        rows = json.load(f)
    with open(folder_path / "columns.json", "r") as f:
        columns = json.load(f)
    return rows, columns
