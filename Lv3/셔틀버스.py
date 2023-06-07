def solution(n, t, m, timetable):
    for idx, time in enumerate(timetable):
        minute, second = time.split(':')
        timetable[idx] = int(minute) * 60 + int(second)
    table = sorted(timetable)
    mydict = [[540 + i * t, int(m), 0] for i in range(n)]
    tidx, didx = 0, 0
    while True:
        if tidx == len(table) or didx == n:
            break
        if mydict[didx][1] > 0 and table[tidx] <= mydict[didx][0]:
            mydict[didx][2] = table[tidx]
            mydict[didx][1] -= 1
            tidx += 1
        else:
            didx += 1
    if mydict[-1][1] == 0:
        answer = mydict[-1][2] - 1
    else:
        answer = mydict[-1][0]
    return "%02d:%02d" % (answer // 60, answer % 60)
