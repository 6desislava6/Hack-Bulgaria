import math
def find_volume(edge):
	return edge*edge*edge/(6*math.sqrt(2))

def tetrahedron_filled(edges, water):
	volumes = []
	for edge in edges:
		volumes.append(find_volume(edge/100))
	water_cubic = water/1000
	count = 0
	volumes.sort()
	for volume in volumes:
		water_cubic = water_cubic - volume
		if water_cubic<0:
			break
		count = count + 1
	return count

string_input = input ('Enter the edges: ')
numbers = string_input.split(' ')
edges = []
for num in numbers:
	edges.append(int(num))
water = int(input('Enter the amount of water: '))
print (tetrahedron_filled(edges, water))