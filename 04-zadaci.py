def fn_four(lis_one, lis_two):
    if isinstance(lis_one, list) and isinstance(lis_two, list) and len(lis_one) == len(lis_two):
        return([-1 if item1 != item2 else item1 for item1, item2 in zip(lis_one, lis_two)])        

print(fn_four([1, 2, 3, 4, 5], [2, 2, 4, 4, 5]))