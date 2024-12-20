from Strings.Json_Dump import jason 
from Strings.json_format_convert import convert
from Notifications.Notify import noti

def foo():
    lines, cleaned_list = convert.conversion_to_json()
    jason.FilePut(lines,cleaned_list)
    noti.check(cleaned_list)

if __name__ == "__main__":
    foo()
