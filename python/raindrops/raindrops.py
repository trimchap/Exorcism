def convert(number):
    result = ''
    if number%3 == 0:
        result = result + 'Pling'
    if number%5 == 0:
        result = result+'Plang'
    if number%7 == 0:
        result = result+'Plong'
    if result == '':
        result = str(number)
    return result

#TEST
print('27 -',convert(27))
print('28 -',convert(28))
print('30 -',convert(30))
print('34 -',convert(34))
print('8 -',convert(8))
print('1 -',convert(1))
