from datetime import datetime, timedelta

def scheduleTutor(start, end):
    breakfast = timedelta(minutes=10)
    lesson = timedelta(minutes=45)
    end1 = start + lesson
    while end1 <= end:
        print(start.time().strftime("%H:%M"), "-", end1.time().strftime("%H:%M"))
        start = end1 + breakfast
        end1 = start + lesson
        # print(start.time(), "-", end1.time())


start = datetime.strptime(input(), "%H:%M")
end = datetime.strptime(input(), "%H:%M")

scheduleTutor(start, end)