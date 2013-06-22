import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: id
    # value: rest of records for item
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value,key)

def reducer(key, list_of_values):
    # key: id
    # value: records for id. value[0] labels val as either order or line_item
    for v in list_of_values:
    	if list_of_values.count(v) ==1:
    		mr.emit((key, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
