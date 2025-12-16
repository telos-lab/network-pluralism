import pandas as pd
from network_pluralism.access.resolved import to_level
from network_pluralism.access.utils.files import load_matrix


def return_top_n(matrix, rows_mapping, col_mapping, axis=0, top_n=10):
    results = pd.DataFrame(
        matrix.sum(axis=axis).A1,
        index=col_mapping.keys() if axis == 0 else rows_mapping.keys(),
        columns=["count"],
    ).sort_values("count", ascending=False)
    return results.head(top_n) if top_n > 0 else results


def sparse_matrix_to_edge_list(m, r, c):
    coo = m.tocoo()

    # Turn to df
    df = pd.DataFrame(
        zip(coo.row, coo.col, coo.data), columns=["r_num", "c_num", "num"]
    )
    df = df.merge(pd.DataFrame(r.items(), columns=["r_sem", "r_num"]))
    df = df.merge(pd.DataFrame(c.items(), columns=["c_sem", "c_num"]))
    return df


def get_aggregation_edge_list(node_type="j", higher_level=2):
    node_type = "decisions" if node_type == "j" else "statutes"
    aggregation_matrix, am_rows, am_cols = load_matrix(
        name=f"{node_type}_level_{higher_level}"
    )
    return sparse_matrix_to_edge_list(aggregation_matrix, am_rows, am_cols)



def get_incidence_edge_list(d: int = 3, s: int = 1):
    m, r, c = to_level(d, s)

    incidence_df = sparse_matrix_to_edge_list(m, r, c)

    # add metata
    aggr_df = get_aggregation_edge_list(node_type="j", higher_level=d - 1)

    incidence_df = incidence_df.merge(
        aggr_df[["r_sem", "c_sem"]],
        left_on="r_sem",
        right_on="c_sem",
        suffixes=["_inc", "_aggr"],
    )

    return incidence_df
