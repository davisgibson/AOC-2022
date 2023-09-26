def divide_string_in_half(string):
	string = string.strip()
	compartment_1, compartment_2 = string[:len(string)//2], string[len(string)//2:]
	return [compartment_1, compartment_2]

def find_common_char(compartments):
	compartment_1 = compartments[0]
	compartment_2 = compartments[1]
	return next(iter(set(compartment_1).intersection(compartment_2))) # it looks bad but it works and it's fast

def get_priority_of_char(char):
	priority = ord(char.lower()) - 96
	if char.isupper():
		priority += 26
	return priority
	

def calc_total_priorities(backpacks):
	priority_total = 0
	for backpack in backpacks:
		compartments = divide_string_in_half(backpack)
		common_char = find_common_char(compartments)
		priority = get_priority_of_char(common_char)
		priority_total += priority
	return priority_total

def find_common_chars(string_1, string_2):
	return ''.join(set(string_1).intersection(set(string_2)))

def calc_priorities_of_badges(backpacks):
	priority_total = 0
	current_elf_group = []
	current_similar_items = ''
	for backpack in backpacks:
		current_elf_group.append(backpack.strip())
		if len(current_elf_group) == 1:
			continue
		if len(current_elf_group) == 2:
			current_similar_items = find_common_chars(current_elf_group[0], current_elf_group[1])
		else:
			badge = find_common_char([backpack, current_similar_items])
			priority_total += get_priority_of_char(badge)
			current_elf_group = []
	return priority_total






file = open('input.txt')
backpacks = file.readlines()
file.close()

print("Part 1: " + str(calc_total_priorities(backpacks)))
print("Part 2: " + str(calc_priorities_of_badges(backpacks)))