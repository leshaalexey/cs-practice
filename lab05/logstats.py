def parse_event(line):
	f_space_index = line.find(" ")
	s_space_index = line.find(" ", f_space_index+1)

	time = line[:f_space_index]
	level = line[f_space_index+1:s_space_index]
	message = line[s_space_index+1:]

	if time == "" or level == "" or message == "" or f_space_index == -1 or s_space_index == -1:
		return ""


	return {
		"time": time,
		"level": level,
		"message": message
	}


def count_levels(lines):
	levels_counter = {
		"BROKEN": 0,
		"DEBUG": 0,
		"ERROR": 0,
		"INFO": 0,
		"WARNING": 0,
	}

	for line in lines:
		if line != "":
			event = parse_event(line)

			if event["level"] not in levels_counter.keys():
				levels_counter["BROKEN"] += 1
			else:
				for l in levels_counter.keys():
					if event["level"] == l:
						levels_counter[l] += 1
	
	return levels_counter

def top_errors(lines, n):
	events = []
	for line in lines:
		events.append(parse_event(line))

	messages = [x["message"] for x in events if x["level"] == "ERROR"]

	messages_count = [[x, 0] for x in set(messages)]

	for message_cnt in messages_count:
		message_cnt[1] = messages.count(message_cnt[0])

	return messages_count[:n] if len(lines) > n else messages_count

def format_report(counts, errors):
	print("Отчет по журналу\n")
	
	for count in counts.keys():
		print(f"{count}: {counts[count]}")


	print("\nЧастые ошибки: ")

	for error_with_cnt in errors:
		print(f"- {error_with_cnt[0]} - {error_with_cnt[1]}")