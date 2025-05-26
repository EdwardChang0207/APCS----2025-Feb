n = int(input()) #幾筆資料

# submissions = []
s = [], t = []

error_count = 0
for _ in range(n):
    time, score = map(int , input().split())
    # submissions.append((time , score))
    s.append(score)
    t.append(time)
    if score == -1:
        error_count += 1

# max_score = max(score for time , score in submissions)
max_score = max(s)

# first_max_time = next(time for time , score in submissions if score == max_score)
first_max_time = t[s.index(max_score)]
total_score = max_score - n - error_count * 2

if total_score < 0:
    total_score = 0
print(total_score , first_max_time)