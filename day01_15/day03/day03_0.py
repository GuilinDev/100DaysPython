"""
练习1 英制公制单位转换
"""
value = float(input('Please input imperial length: '))
unit = input('Please input scale: ')

if unit == 'in' or unit == '英寸':
  print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
  print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
else:
  print('请输入有效的单位！')