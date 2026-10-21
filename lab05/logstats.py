def parse_event(line):
	f_space_index = line.find(" ")
	s_space_index = line.find(" ", f_space_index+1)

	time = line[:f_space_index]
	level = line[f_space_index+1:s_space_index]
	message = line[s_space_index+1:]

	if time == "" or level == "" or message == "" or f_space_index == -1 or s_space_index == -1:
		raise ValueError("Некорректная строка")


	return {
		"time": time,
		"level": level,
		"message": message
	}


def count_levels(lines):
	...


def top_errors(lines, n):
	...

def format_report(counts, errors):
	...

