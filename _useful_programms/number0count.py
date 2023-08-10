#подсчет кол-ва нулей 
import re
pattern = '[0]*'
text = '01010101010100000000000110100101'
print(len(re.findall(pattern,text)))
