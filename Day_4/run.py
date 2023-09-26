def parse_lines(lines_raw):
	parsed_lines = []
	for line in lines:
		ranges = line.split(',')
		temp = []
		for _range in ranges:
			bounds = _range.split('-')
			_min = int(bounds[0])
			_max = int(bounds[1])
			temp.append(CustomRange(_min, _max))
		parsed_lines.append(temp)

	return parsed_lines


def find_number_of_fully_contained_IDs(lines_raw):
	num_of_fully_contained_IDs = 0
	parsed_lines = parse_lines(lines_raw)
	for line in parsed_lines:
		if line[0].encapsulates(line[1]) or line[1].encapsulates(line[0]):
			num_of_fully_contained_IDs += 1

	return num_of_fully_contained_IDs

def find_number_of_overlapping_pairs(lines_raw):
	# not the number of overlapping IDs, but number of pairs that contain 1+ overlap
	num_overlapping_pairs = 0
	parsed_lines = parse_lines(lines_raw)
	for line in parsed_lines:
		if line[0].overlaps(line[1]) or line[1].overlaps(line[0]):
			num_overlapping_pairs += 1

	return num_overlapping_pairs



class CustomRange:
	def __init__(self, _min, _max):
		self.min = _min
		self.max = _max

	def __str__(self):
		return str(self.min) + '-' + str(self.max)

	def encapsulates(self, _range):
		# only check if self encapsulates _range
		return self.min >= _range.min and self.max <= _range.max

	def overlaps(self, _range):
		return (self.min <= _range.min and self.max >= _range.min) or (self.min <= _range.max and self.max >= _range.max)



file = open('input.txt')
lines = file.readlines()
file.close()

print("Part 1: " + str(find_number_of_fully_contained_IDs(lines)))
print("Part 2: " + str(find_number_of_overlapping_pairs(lines)))