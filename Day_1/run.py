def find_highest_amount_of_calories(lines):
	current_elf_calories = 0
	highest_calories = 0
	for line in lines:
		if(line != '\n'):
			current_elf_calories += int(line)
		else:
			if(current_elf_calories > highest_calories):
				highest_calories = current_elf_calories
			current_elf_calories = 0

	return highest_calories

def find_index_of_lowest_calories(calorie_array):
	ret = False;
	lowest_calorie = False;
	for index, calorie in enumerate(calorie_array):
		if lowest_calorie == False:
			lowest_calorie = calorie;
		elif(calorie < lowest_calorie):
			lowest_calorie = calorie
			ret = index
	return ret

def find_calorie_count_of_top_three_elves(lines):
	current_elf_calories = 0
	highest_calories = [];
	count = 0
	for line in lines:
		if(line != '\n'):
			current_elf_calories += int(line)
		else:
			if(count < 3):
				count += 1
				highest_calories.append(current_elf_calories);
				current_elf_calories = 0
				continue
			index_of_lowest_calorie = find_index_of_lowest_calories(highest_calories)
			if(current_elf_calories > highest_calories[index_of_lowest_calorie]):
				highest_calories[index_of_lowest_calorie] = current_elf_calories
			current_elf_calories = 0

	ret = 0;
	for calories in highest_calories:
		ret += calories

	return ret

file = open('input.txt')
lines = file.readlines()
file.close()
answer1 = find_highest_amount_of_calories(lines)
answer2 = find_calorie_count_of_top_three_elves(lines)
print("answer 1 = " + str(answer1))
print("answer 2 = " + str(answer2))
