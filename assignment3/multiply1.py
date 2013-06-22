import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # Each record is of form [matrix, i,j, value]
    matrix, row, col, value = record

    # We are trying to multiply A x B, so A is the row dominator.
    if matrix == 'a':
        # hardcoding the max col = 5
        for i in range(5):
            mr.emit_intermediate((row, i), [col, value])
    else:
        for i in range(5):
            mr.emit_intermediate((i, col), [row, value])

def reducer(key, list_of_values):
    row, col = key
    total = 0
    for x in range(5):
        values = filter(lambda i: i[0] == x, list_of_values)
        if len(values) <= 1:
            i_val = 0
        else:
            i_val = reduce(lambda x, y: x[1] * y[1], values)
        total = total + i_val
    mr.emit((row, col, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
