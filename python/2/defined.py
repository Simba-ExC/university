import re

phones_str = input ("введите " )
phones = re.split(r' *; *', phones_str, flags=re.M)

def check_phone(num: str):
    clear_phone = re.sub(r'\D', '', num)
    result = re.match(r'^[78]?\d{10}$', clear_phone)
    if bool(result) == 'true':
        return "phone"
    else :
        text = phones_str
        pattern = r"sidorov@([\w\.-]+)(\.[\w\.]+)"
        if re.search(pattern, text):
            return "email"
        else :
            return "unknown" 

for phone in phones:
    t = check_phone(phone)
    print (t)
