def fn_five(lis):
    return[{"id": id, "ime": name, "prezime": surname} 
        for tupl in zip(sorted(lis)) 
            for (id, name, surname) in tupl if name[0] == surname[0]]

print(fn_five([
    (121, "Ivan", "Ivic"),
    (431, "Pero", "Horvat"),
    (31, "Marija", "Maric")]))