import pandas as pd


def return_top_n(matrix, rows_mapping, col_mapping, axis=0, top_n=10):
    results = pd.DataFrame(
        matrix.sum(axis=axis).A1,
        index=col_mapping.keys() if axis == 0 else rows_mapping.keys(),
        columns=["count"],
    ).sort_values("count", ascending=False)
    return results.head(top_n) if top_n > 0 else results
