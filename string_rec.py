# recursevely capitalize a word

mystring = "mystring"

def capitalize_recursevely(astring):
  if len(astring) == 0:
    return ""
  else:
    return astring[0].upper() + capitalize_recursevely(astring[1:])
 
print(capitalize_recursevely(mystring))