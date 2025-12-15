from scipy.sparse import tril


def to_lower_third_triangle(matrix):
    return tril(matrix, k=-1)


# Transforming the graph to either side of the bipartite relation


def to_projection(
    matrix,
    axis=1,
    lower_third: bool = False,
    csr_format: bool = True,
):
    matrix.data[:] = 1
    projection = matrix.T @ matrix if axis == 1 else matrix @ matrix.T

    projection = projection if not lower_third else to_lower_third_triangle(projection)
    return projection.tocsr() if csr_format else projection
