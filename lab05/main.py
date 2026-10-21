import logstats
import os

log_file_name = input() + ".log"

current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, log_file_name)

log_st = []
with open(log_file_path, encoding="utf-8") as log:
	for line in log:
		log_st.append(line[:-1])

counts = logstats.count_levels(log_st)

all = [
	"Ввод:           Вывод:\n",
	f"{log_file_name}      {sum(counts.values())}\n",
	f"                {sum(counts[x] for x in counts.keys() if x == "ERROR")}\n",
	f"                {sum(counts[x] for x in counts.keys() if x == "BROKEN")}",
]
with open("lab05/report.txt", "w", encoding="utf-8") as file:
    file.writelines(all)
