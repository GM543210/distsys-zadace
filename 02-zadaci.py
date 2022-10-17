def fn_two(lis, dktnry):
    if isinstance(lis,list) and isinstance(dktnry, dict) and len(lis) == len(dktnry):
        return({k:v if isinstance(k, int) and v in range(5, 10) else -1 for k, v in zip(dktnry, lis) })
    else:
        return("Greška")

print(fn_two([8,7,1], {1:2,2:1,3:2}))