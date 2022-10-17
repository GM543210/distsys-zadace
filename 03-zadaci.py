def fn_three(list_of_dktnrs):
    if isinstance(list_of_dktnrs, list) and all(isinstance(item, dict) for item in list_of_dktnrs):
        return{
            "ukupno": {"artikli": [item["naziv"] for item in list_of_dktnrs], 
            "cijena": sum(item["cijena"] * item["kolicina"] for item in list_of_dktnrs)}
        }
    else:
        return("Greška")

print(fn_three([
    {"cijena": 8, "naziv": "Kruh", "kolicina": 1},
    {"cijena": 13, "naziv": "Sok", "kolicina": 2},
    {"cijena": 7, "naziv": "Upaljac", "kolicina": 1}
    ]))