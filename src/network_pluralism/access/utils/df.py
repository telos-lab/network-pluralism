from itertools import product
import pandas as pd
from network_pluralism.access.resolved import to_level
from network_pluralism.access.utils.files import load_matrix
from network_pluralism.access.ego import get_ego_matrix

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

def get_cooccurrence_edge_list_df(d: int = 3, s: int = 1):
    incidence_edge_list = get_incidence_edge_list(d, s)
    cooccurrence_edge_list = []

    target_col = "c_sem_inc"

    for i, values in incidence_edge_list.groupby("r_sem_inc"):
        referenced_section = values[target_col].to_list()
        edges = list(product(referenced_section, referenced_section))
        for e in edges:
            cooccurrence_edge_list.append(list(e) + [i])

    aggr_df = get_aggregation_edge_list(node_type="j", higher_level=3 - 1)
    aggr_df.head()

    cooccurrence_edge_list_df = pd.DataFrame(cooccurrence_edge_list, columns=["s1", "s2", "source"]).merge(
        aggr_df[["r_sem", "c_sem"]], left_on="source", right_on="c_sem"
    )
    return cooccurrence_edge_list_df

def get_data_for_perspectives(
    perspectives=list[dict],
    top_n: int = 10,
    only_union: bool = True,
    sort_by_p_number: int = 0,
):
    ego_matrices, indices = {}, {}

    # Get Ego matrices
    for i, p in enumerate(perspectives):
        ego_matrices[i], indices[i] = get_ego_matrix(**p)

    dfs = []
    overall_top_n = []

    for i, p in enumerate(perspectives):
        df = pd.DataFrame(
            ego_matrices[i][:, indices[i][p["statute"]]].toarray(), index=indices[i], columns=["count"]
        ).sort_values("count", ascending=False)
        overall_top_n.extend(list(df.head(top_n + 1).index)[1:])
        dfs.append(df)

    union_top_n = list(set(overall_top_n))

    dfs_with_suffixes = [dfs[i].add_prefix(f"{i}_") for i in range(len(dfs))]

    merged_df = pd.concat(dfs_with_suffixes, axis=1).fillna(0)

    # Only top n union
    if only_union:
        sort_col = f"{sort_by_p_number}_{'count'}"
        merged_df = merged_df.loc[union_top_n].sort_values([sort_col], ascending=False)

    cols = merged_df.columns
    global_max = merged_df[cols].to_numpy().max()

    # Normalize based on per col max rescale both global (across max value of all rows) and local (per row)
    for col in cols:
        merged_df[f"{col}_norm_global"] = merged_df[col] / global_max
        merged_df[f"{col}_norm_local"] = merged_df[col] / merged_df[col].max()
    
    global_max_local = merged_df[[f"{col}_norm_local" for col in cols]].to_numpy().max()
    for col in cols:
        merged_df[f"{col}_norm_global_local"] = merged_df[f"{col}_norm_local"] / global_max_local

    return merged_df