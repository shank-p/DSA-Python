"""
    skip a character say a
"""
string = 'baccad'

def skip_a(string):
    if len(string)==0:
        return ""
    if string[0] != 'a':
        return string[0] + skip_a(string[1:])
    else:   
        return skip_a(string[1:])

res = skip_a(string)
print(res)
     
    
    


