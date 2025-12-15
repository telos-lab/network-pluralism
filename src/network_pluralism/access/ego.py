from network_pluralism.access.utils.ids import get_decision_ids, get_paragraph_ids
from network_pluralism.access.filtered import get_filtered_matrix


def get_ego_matrix(statute, s=1, d=3, from_institutions=None):
    if isinstance(from_institutions, str):
        from_institutions = [from_institutions]
    decisions_or_paragraphs = []
    if from_institutions:
        for institution in from_institutions:
            if d == 2:
                decisions_or_paragraphs.extend(get_decision_ids(institution))
            if d == 3:
                decisions_or_paragraphs.extend(get_paragraph_ids(institution))

    iltered_by_statutes, r, new_col_indices = get_filtered_matrix(
        [statute], decisions=decisions_or_paragraphs, s=s, d=d
    )
    # check statute is actually cited

    filtered_by_rulings, r2, new_col_indices2 = get_filtered_matrix(
        decisions=r.keys(), s=s, d=d
    )

    if from_institutions:
        filtered_by_neighbors, decisions, neighbors = get_filtered_matrix(
            new_col_indices2.keys(), decisions=r.keys(), s=s, d=d
        )
    else:
        filtered_by_neighbors, decisions, neighbors = get_filtered_matrix(
            new_col_indices2.keys(), s=s, d=d
        )
    filtered_by_neighbors.data[:] = 1  # Binarize before

    projection_of_neighbors = filtered_by_neighbors.T @ filtered_by_neighbors
    # projection_of_neighbors = to_lower_third_triangle(projection_of_neighbors)
    projection_of_neighbors = projection_of_neighbors.tocsr()
    return projection_of_neighbors, neighbors
