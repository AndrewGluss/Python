from datetime import datetime, timedelta

def time_to_fly(value):
		totaltime = timedelta(seconds=0)
		while len(value) > 0:
			#print(value)
			start = value[0][1]
			#print("Start :", start)
			for i in range(1, len(value)+1):
				end1 = start
				if "C" in value[i][-1] or "S" in value[i][-1]:
					end1 = value[i][1]
					#print("end1: ", end1)
					delta = end1-start
					#print("delta: ", delta)
					totaltime += delta
					#print("totaltime: ", totaltime)
					value = value[i+1:]
					break
				else:
					continue
		return totaltime

n = int(input())
dict_logs = dict()
for i in range(n):
	log = input().split(" ")
	time_p = datetime.strptime(".".join(log[:3]), "%j.%H.%M")
	info = tuple([log[0], time_p, log[-1]])
	dict_logs[int(log[3])] = dict_logs.setdefault(int(log[3]), []) + [info]

for key in dict_logs:
	value = sorted(dict_logs[key], key=lambda x: x[1])
	seconds = time_to_fly(value)
	print(int(seconds.total_seconds()//60))


'''8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B'''

'''time_to_fly([('14', datetime(1900, 1, 14, 21, 30), 'A'),
('14', datetime(1900, 1, 14, 23, 52), 'B'),
('15', datetime(1900, 1, 15, 0, 5), 'C'),
('50', datetime(1900, 2, 19, 7, 25), 'A'),
('50', datetime(1900, 2, 19, 7, 26), 'C')])'''