s="M1 jkj@gmail.com"
import re
m=re.match("(.*)@",s)
if m!=None:
    print(m.group(1))