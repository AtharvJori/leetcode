s= "011101"
highest_score = 0
for i in range(1,len(s)):
    left_s = s[:i]
    right_s = s[i:]
    print(left_s, right_s)
    score = left_s.count('0') + right_s.count('1')
    print(score)
    highest_score = max(highest_score, score)

print(highest_score)