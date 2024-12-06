# Sort a dictionary

def dict_sort(ds):
    dict2 = {}
    d = sorted(ds.keys())
    for i in d:
        dict2[i] = ds[i]
    print(dict2)


# Sort a dictionary by values

def dict_vsort(ds):
    dict2 = {key: value for key, value in sorted(ds.items(), key=lambda x: x[1])}
    print(dict2)


# Input
ds = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
dict_sort(ds)
dict_vsort(ds)
