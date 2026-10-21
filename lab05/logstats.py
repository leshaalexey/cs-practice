test = '''2026-03-01T09:00:11 INFO Сервис запущен
2026-03-01T09:00:12 INFO Загружена конфигурация config.yaml
2026-03-01T09:01:40 DEBUG Соединение с базой установлено
2026-03-01T09:03:02 WARNING Очередь задач растёт
2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv
2026-03-01T09:04:10 INFO Повторная попытка чтения
2026-03-01T09:04:12 ERROR Не удалось открыть файл data.csv
2026-03-01T09:06:30 INFO Задача 14 выполнена
2026-03-01T09:07:00 WARNING Медленный ответ базы
2026-03-01T09:08:21 ERROR Превышено время ожидания
2026-03-01T09:09:02 DEBUG Кэш очищен
сломанная строка без уровня
2026-03-01T09:10:44 INFO Задача 15 выполнена
2026-03-01T09:11:09 ERROR Не удалось открыть файл data.csv
2026-03-01T09:12:30 WARNING Очередь задач растёт
2026-03-01T09:13:01 INFO Задача 16 выполнена
2026-03-01T09:14:20 ERROR Превышено время ожидания
2026-03-01T09:15:00 DEBUG Соединение переоткрыто
2026-03-01T09:16:11 INFO Задача 17 выполнена
2026-03-01T09:17:40 TRACE непонятный уровень
2026-03-01T09:18:02 ERROR Нет доступа к каталогу /var/log
2026-03-01T09:19:15 INFO Задача 18 выполнена
2026-03-01T09:20:00 WARNING Диск заполнен на 85%
2026-03-01T09:21:30 INFO Отчёт сформирован
2026-03-01T09:22:00 DEBUG Фоновая проверка завершена
2026-03-01T09:23:10 ERROR Не удалось открыть файл data.csv
2026-03-01T09:24:00 INFO Задача 19 выполнена
2026-03-01T09:25:05 WARNING Очередь задач растёт
2026-03-01T09:26:00 INFO Сервис остановлен'''







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
	levels_counter = {
		"BROKEN": 0,
		"DEBUG": 0,
		"ERROR": 0,
		"INFO": 0,
		"WARNING": 0,
	}

	for line in lines:
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

	return messages_count

def format_report(counts, errors):
	print("Отчет по журналу\n")
	
	for count in counts.keys():
		print(f"{count}: {counts[count]}")


	print("\nЧастые ошибки: ")

	for error_with_cnt in errors:
		print(f"- {error_with_cnt[0]} - {error_with_cnt[1]}")