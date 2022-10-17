def fn_one(lista):
    return([isinstance(item, str) == True and item for item in lista if len(item) > 4])    
    
print(fn_one(["Pas", "Macka", "Stol"]))
