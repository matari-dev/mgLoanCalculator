import math

edge_length = int(input())
area = 2 * math.sqrt(3) * math.pow(edge_length, 2)
volume = (math.sqrt(2) * math.pow(edge_length, 3)) / 3

print('%.2f %.2f' % (area, volume))
