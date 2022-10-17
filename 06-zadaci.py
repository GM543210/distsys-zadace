def fn_six(a, b):
    return(a + b if type(a) == type(b) and isinstance(a, list) and isinstance(b, list) else {**a, **b})

print(fn_six([1,2,1,2],[3,2]))
print(fn_six({1:2,3:2},{5:2,4:1}))