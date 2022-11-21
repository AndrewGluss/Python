from datetime import datetime, timedelta


def timer(time_dt, timer_seconds):
    ring_timer = time_dt + timedelta(seconds=timer_seconds)
    return ring_timer.time()


time_dt = datetime.strptime(input(), "%H:%M:%S")
timer_seconds = int(input())
#ring_timer = time_dt + timedelta(seconds=timer_seconds)
#print(ring_timer.time())


print(timer(time_dt,timer_seconds))