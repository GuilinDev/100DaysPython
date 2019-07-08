"""
练习5
计算个人所得税
麻省州税$8000以下不用交，否则%5.05
"""
salary = float(input('Salary: '))
if salary < 8000:
  salary_after_tax = salary
else:
  salary_after_tax = salary * (1 - 0.0505)

print ("Salary: %.2f" % salary_after_tax)