from scipy.sparse import issparse
from network_pluralism.access.matrix_files import load_matrix
from network_pluralism.setup.paths import COMPUTATION_PATH
import re
from pathlib import Path


def find_max_levels(directory=COMPUTATION_PATH):
    statutes_max = -1
    decisions_max = -1

    statutes_pattern = re.compile(r"statutes_level_(\d+)_relative")
    decisions_pattern = re.compile(r"decisions_level_(\d+)")

    for item in Path(directory).iterdir():
        if item.is_dir():
            folder_name = item.name
            statutes_match = statutes_pattern.match(folder_name)
            decisions_match = decisions_pattern.match(folder_name)

            if statutes_match:
                level = int(statutes_match.group(1))
                statutes_max = max(statutes_max, level)

            if decisions_match:
                level = int(decisions_match.group(1))
                decisions_max = max(decisions_max, level)

    return decisions_max, statutes_max


def to_level(d, s, binary=False, normalize: str | int = None):
    """Converts the dynamically counted matrix into a aggregated matrix."""
    ground_truth, ground_truth_rows, ground_truth_cols = load_matrix(
        COMPUTATION_PATH / "ground_truth"
    )
    deppest_decision_level, deppest_statute_level = find_max_levels()

    incidence_matrix = ground_truth
    incidence_matrix_rows = ground_truth_rows
    incidence_matrix_cols = ground_truth_cols
    assert issparse(incidence_matrix)

    # Aggregate on statutes
    for level in range(deppest_statute_level, s, -1):
        aggregation_matrix, am_rows, am_cols = load_matrix(
            name=f"statutes_level_{level - 1}"
        )
        assert issparse(aggregation_matrix)
        incidence_matrix = incidence_matrix @ aggregation_matrix.T
        incidence_matrix_cols = am_rows
    # Aggregate on decisions
    for level in range(deppest_decision_level, d - 1, -1):
        aggregation_matrix, am_rows, am_cols = load_matrix(
            name=f"decisions_level_{level}"
        )
        assert issparse(aggregation_matrix)
        incidence_matrix = aggregation_matrix @ incidence_matrix
        incidence_matrix_rows = am_rows
    print(f"Out Matrix of shape {incidence_matrix.shape}")
    assert issparse(incidence_matrix)

    if binary:
        incidence_matrix.data[:] = 1
    if normalize in [0, 1]:
        if normalize == 1:
            incidence_matrix = (
                (
                    incidence_matrix.transpose() / incidence_matrix.sum(axis=1).A1
                ).transpose()
            ).tocsr()
        elif normalize == 0:
            incidence_matrix = (
                incidence_matrix / incidence_matrix.sum(axis=0).A1
            ).tocsr()
    return incidence_matrix, incidence_matrix_rows, incidence_matrix_cols
