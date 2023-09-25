def parse_round(_round):
	return _round.strip().split(' ')

def parse_rounds(rounds):
	parsed_rounds = []
	for _round in rounds:
		parsed_rounds.append(parse_round(_round))

	return parsed_rounds

def get_move_that_matches_result(opponent_choice, result_of_round):
	# result of round
	# X = Lose
	# Y = Draw
	# Z = Win
	RESULT_MAP = {
		"AX": "Z",
		"AY": "X",
		"AZ": "Y",
		"BX": "X",
		"BY": "Y",
		"BZ": "Z",
		"CX": "Y",
		"CY": "Z",
		"CZ": "X"
	}

	return RESULT_MAP[opponent_choice + result_of_round]


def get_result_of_round(_round, is_part_2 = False):
	opponent_choice = _round[0]
	if(is_part_2):
		my_choice = get_move_that_matches_result(opponent_choice, _round[1])
	else:
		my_choice = _round[1]
	score = 0
	if my_choice == "X": # rock gives 1 point
		score += 1
	elif my_choice == "Y": # paper gives 2 points
		score += 2
	else: # skizzorz gives 3 points
		score += 3

	SCORE_MAP = {
		"AX": 3, # tie
		"AZ": 0, # lose
		"AY": 6, # win
		"BX": 0, # lose
		"BY": 3, # tie
		"BZ": 6, # win
		"CX": 6, # win
		"CY": 0, # lose
		"CZ": 3  # tie
	}

	score += SCORE_MAP[opponent_choice + my_choice]

	return score

def calc_total_score_from_strategy_guide(rounds, is_part_2 = False):
	parsed_rounds = parse_rounds(rounds)
	score_running_total = 0
	for _round in parsed_rounds:
		score_running_total += get_result_of_round(_round, is_part_2)

	return score_running_total

file = open('input.txt')
rounds = file.readlines()
file.close()
print("Part 1: " + str(calc_total_score_from_strategy_guide(rounds)))
print("Part 2: " + str(calc_total_score_from_strategy_guide(rounds, True)))