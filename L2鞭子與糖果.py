first=int(input('輸入英文的成績'))
second=int(input('輸入數學的成績'))
if first>=90 and second>=90:
    print('獲得獎勵')
elif first<60 and second<60:
    print('需懲罰')
elif first<60 or second<60:
    print('再加油')
else:
    print()