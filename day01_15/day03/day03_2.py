"""
练习3
百分制成绩转换
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> F
"""
score = float(input('Input score: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("分数对应的等级： " + grade)