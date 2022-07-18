import sys

def process_string(stringParam):
    results = len(stringParam)
    return results
def process_bool(boolParam):
    results = not(boolParam)
    return results
def process_number(numberParam):
    results = abs(numberParam - 100)
    return results
numberOfParams = len(sys.argv)
if numberOfParams != 3:
    sys.exit("Введите 3 аргумента")
firstParam = sys.argv[1]
secondParam = sys.argv[2]
if firstParam == 's':
    if (type(secondParam) == str):
        res = process_string(secondParam)
        print (res)
    else:
        print("Должна быть строка")
elif firstParam == 'b':
    if ((secondParam == "True") or (secondParam == "False")):
        res = process_bool(eval(secondParam))
        print (res)
    else:
        print("Должен быть бул")
elif firstParam == 'n':
    if (secondParam.isdigit()):
        secondParam = int(secondParam)
        res = process_number(secondParam)
        print (res)
    else:
        print("Должен быть int")