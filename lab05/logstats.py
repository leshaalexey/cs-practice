def parse_event(line):
	line = line.strip()
	f_space_index = line.find(" ")
	s_space_index = line.find(" ", f_space_index+1)

	time = line[:f_space_index]
	level = line[f_space_index+1:s_space_index]
	message = line[s_space_index+1:]

	if time == "" or level == "" or message == "" or f_space_index == -1 or s_space_index == -1:
		raise ValueError("")


	return {
		"time": time,
		"level": level,
		"message": message
	}


def count_levels(lines):
	levels = [
		"BROKEN",
		"DEBUG",
		"ERROR",
		"INFO",
		"WARNING",
	]
	levels_counter = {}

	for line in lines:
		if line != "":
			try:
				event = parse_event(line)
			except ValueError:
				levels_counter["BROKEN"] += 1

			if event["level"] not in levels:
				levels_counter["BROKEN"] += 1
			else:
				for l in levels:
					if event["level"] == l:
						levels_counter[l] += 1
	
	return levels_counter

def top_errors(lines, n):
	events = []
	if lines:
		for line in lines:
			try:
				events.append(parse_event(line))
			except ValueError:
				continue

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