# raise Exception('Bad')

try:
    x = 5 / 0
except Exception as e:
    print(e)
finally:
    print('finally')
