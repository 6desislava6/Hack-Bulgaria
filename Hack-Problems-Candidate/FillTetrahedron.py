import math
def find_volume(edge):
	edge_meters = edge/100
	volume = edge_meters*edge_meters*edge_meters/(6*math.sqrt(2))
	return volume
def fill_tetrahedron (volume):
	return volume*1000

edge = int(input('Write edge here: '))
volume = find_volume(edge)
amount_litres = fill_tetrahedron(volume)
print("{0:.2f}".format(amount_litres))