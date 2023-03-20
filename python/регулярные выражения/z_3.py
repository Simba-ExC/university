import re

_repl_old = 'ABCEHIKMOPTXYЗ'
_repl_new = 'АВСЕН1КМОРТХУ3'
_repl_tuples = set(zip(_repl_old, _repl_new))

ALLOWED_LETTERS = 'АВЕКМНОРСТУХ'
ALLOWED_NUMBERS = '0123456789'
ALLOWED_SYMBOLS = ALLOWED_LETTERS + ALLOWED_NUMBERS

ALLOWED_LETTERS = set(ALLOWED_LETTERS)
ALLOWED_NUMBERS = set(ALLOWED_NUMBERS)
ALLOWED_SYMBOLS = set(ALLOWED_SYMBOLS)

ALLOWED_FORMATS = {
    'Х999ХХ99',  # Тип 1 — Регистрационные знаки легковых, грузовых автомобилей и автобусов 
    'Х999ХХ999', # Тип 1 — Регистрационные знаки легковых, грузовых автомобилей и автобусов (3 знака в регионе)
    'ХХ99999',   # Тип 1Б — Регистрационные знаки для легковых такси
    'ХХ999999',  # Тип 2 — Регистрационные знаки для автомобильных прицепов и полуприцепов
    '9999ХХ99',  # Тип 3 — Регистрационные знаки для тракторов, самоходных дорожно-строительных и иных машин
    'ХХ99ХХ99'   # Тип 4Б — Регистрационные знаки для мопедов
}

def normalize(no):
   
    no = str(no).replace(' ', '')  # переводим в строку и убираем все пробелы

    no = no.upper()  # все в верхний регистр

    for rt in _repl_tuples:  # латиницу в кириллицу
        no = no.replace(rt[0], rt[1])

    # строим маску формата номера, где "*"" - "0" или "О", "Х" - буква, "9" - цифра
    f = ''
    for c in no:
        if c in '0О':
            f = f + '*'
            continue
        if c in ALLOWED_LETTERS:
            f = f + 'Х'
            continue
        if c in ALLOWED_NUMBERS:
            f = f + '9'
            continue
        raise ValueError(f'Номер не валиден, недопустимый символ: "{c}"')

    # рекурсивно ищем подходящий формат
    def find_acceptable_format(f):
        i = f.find('*')
        if i > -1:
            found_format = find_acceptable_format(f[:i] + 'Х' + f[i+1:])
            if found_format:
                return found_format
            found_format = find_acceptable_format(f[:i] + '9' + f[i+1:])
            if found_format:
                return found_format
        else:
            if f in ALLOWED_FORMATS:
                return f
            else:
                return None

    af = find_acceptable_format(f)

    # подгоняем 0 и О под найденный формат
    if af:
        for i, c in enumerate(f):
            if (c == '*'):
                new_c = '0' if af[i] == '9' else 'О'
                no = no[:i] + new_c + no[i+1:]
    else:
        raise ValueError(f'Номер не валиден, недопустимый формат: "{f}"')

    # проверяем наличие комбинаций вида "000"
    if len(re.findall(r'(^|\D)0+(\D|$)', no)) > 0:
        raise ValueError(f'Номер не валиден, номер не может содержать числовые последовательности, состоящие только из нулей')

    # проверяем допустимость региона
    if (af == 'Х999ХХ999') and (no[-3:-2] == '0'):
        raise ValueError(f'Номер не валиден, первая цифра трехзначного региона не может быть нулем')
    
    no = ''.join(('Номер ',no,' валиден'))
    return no

no = input("Введите номер автомобиля: ")
print("")
print(normalize(no))
