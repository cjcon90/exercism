def saddle_points(matrix):

    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("Rows in matrix have different lengths")

    cols_max = {key:min(col) for key, col in enumerate(zip(*matrix))}

    saddles = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == max(row) and col == cols_max[j]:
                saddles.append({"row": i+1, "column": j+1})

    return saddles
