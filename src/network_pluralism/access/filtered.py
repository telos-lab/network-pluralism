from network_pluralism.access.resolved import to_level

# Get filtered matrix

def convert_mapping(old: dict, boolean_mapping: list[bool]):
    idx = 0
    new = {}
    for (sem_id, old_index), exists in zip(old.items(), boolean_mapping):
        if exists:
            new[sem_id] = idx
            idx += 1
    return new


def get_filtered_matrix(
    statutes: list = None,
    decisions: list = None,
    d=3,
    s=2,
    reduce_mapping=True,
    reduction_axis=-1,
    m=None,
    r=None,
    c=None,
):
    if m is None:
        m, r, c = to_level(d, s)
    new_col_indices = c
    new_row_indices = r

    masked = m
    # Filter by columns
    if statutes:
        col_indices = sorted([c.get(s) for s in statutes])
        sorted_statutes = sorted([(c.get(s), s) for s in statutes], key=lambda x: x[1])
        new_col_indices = {
            sem_id: i for i, (old_id, sem_id) in enumerate(sorted_statutes)
        }

        masked = masked[:, col_indices]

    if decisions:
        row_indices = sorted([r.get(s) for s in decisions])
        sorted_decisions = sorted(
            [(r.get(d), d) for d in decisions], key=lambda x: x[1]
        )

        new_row_indices = {
            sem_id: i for i, (old_id, sem_id) in enumerate(sorted_decisions)
        }  # {sem_id: i for i, sem_id in enumerate(decisions)}

        masked = masked[row_indices, :]

    # Remove unneccessary rows
    if reduce_mapping:
        axis_to_reduce = [0, 1]
        if reduction_axis != -1:  # reducing both
            axis_to_reduce = [reduction_axis]
        for axis in axis_to_reduce:
            non_zero_indices = (
                masked.getnnz(axis=axis) > 0
            )  # Use getnnz for efficient non-zero checks
            if axis == 0:
                masked = masked[:, non_zero_indices]
                new_col_indices = convert_mapping(new_col_indices, non_zero_indices)
            elif axis == 1:
                masked = masked[non_zero_indices, :]
                new_row_indices = convert_mapping(new_row_indices, non_zero_indices)
        return masked, new_row_indices, new_col_indices
    return masked, new_row_indices, new_col_indices
