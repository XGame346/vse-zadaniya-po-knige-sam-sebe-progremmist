def f(x):
    """Принимает целое число и возвращает его, возводя число в квадрат.
    :параметр x: целое число
    """
    return x*x



def my_string(my_string):
    """Выводит переданную строку
    : параметр string: строка.
    """
    print (my_string)



def f(x,y,z, d=16, a=5):def f(x):
    """Принимает целое число и возвращает его, возводя число в квадрат.
    :параметр x: целое число
    """
    return x*x



def my_string(my_string):
    """Выводит переданную строку
    : параметр string: строка.
    """
    print (my_string)



def f(x,y,z, d=16, a=5):
    """ Возвращает результат умножения 3 обязательных параметров
    с двумя необязательными параметрами
    :параметр x: целое число.
    :параметр y: целое число.
    :параметр z: целое число.
    :параметр d: целое число.
    :параметр z: целое число.
    :return: целое число.
    """
    return (x+y+z+d+a)



def f1(x):
    """Принимает целое число и возвращает его, разделив на 2
    :параметр x: целое число
    """
    return int(x/2)
def f2(x):
    """Принимает целое число и возвращает его, умножив на 4 
    :параметр x: целое число
    """
    return int(x*4)



def f(x):
    """ Преобразует строку в целое число.
    :параметр string: строка.
    :return: строка, преобразованная в целое число.
    """
    x=str(x)
    try:
        return float(x)
    except ValueError:
        print ("Возникло исключение")