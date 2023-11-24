import re

def check_date(date):
    pattern = r'^(0[1-9]|[12][0-9]|3[01])[./-](0[1-9]|1[0-2])[./-](\d{4})$|^(19|20)\d{2}, (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2$|^(0[1-9]|[12][0-9]|3[01]) (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}$'
    return bool(re.match(pattern, date))

print(check_date("20 января 1806"))  
print(check_date("1924, July 25"))  

print(check_date("25.08-1002"))  
print(check_date("декабря 19, 1838"))  
print(check_date("8.20.1973"))  
