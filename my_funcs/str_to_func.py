'''функция возвращает результат функции (которую находит в строке txt по поиску в списке через элемент,
содержащий латинскую "x"), подставляя в нее переменные (*args),
по необходимости удаляя из уже полученного текста функции лишний знак препинания (delimiter)'''

def text_to_func(*args, txt='', delimiter=''):
    from math import sin, log
    func_txt = list(filter(lambda x: 'x' in x, txt.split()))[0]
    func_txt = func_txt.strip(delimiter).replace('ln', 'log')
    vars_list = ['x', 'y', 'z']
    args = list(map(lambda x: int(x), args))
    for i in range(len(args)):
        func_txt = func_txt.replace(vars_list[i], f'int(args[{i}])')
    result = eval(func_txt)
    return result
