# import timedelta
from datetime import datetime, timedelta

n = int(input())
for _ in range(n):
    time, StrM = list(map(str, input().split()))
    startingDate = datetime.strptime(time, '%H:%M')
    ans = 0
    endingDate = datetime.strptime("23:59", '%H:%M') - startingDate
    print(endingDate)
    endingMinutes = endingDate.seconds // 60
    print(endingMinutes)
    for i in range(0, endingMinutes + 1, int(StrM)):
        startingDate += timedelta(minutes=int(StrM))
        tmpy = startingDate.strftime("%H:%M")
        
        # print(tmpy)
        print(tmpy[::-1])
        if tmpy == tmpy[::-1]:
            print(tmpy)
            ans += 1
    print("ans", ans)
        # print(startingDate.strftime("%H:%M"))
    # print(time, StrM)