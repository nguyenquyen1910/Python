# Tuong tu nhu map o c++
thisdict={
    "brand": "Apple",
    "model": "Iphone 15 promax",
    "year" : 2023
}
# Moi key luu 1 gia tri tuong ung
print(thisdict)

# Truy cap vao tung item
print(thisdict['model'])

# Kich thuoc cua dict
print(len(thisdict))

# Dict Item and data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"] # Mot key co the co value la 1 mang,set,...
}
print(type(thisdict))
print(thisdict['colors'])

# Ham dict duoc build san
thisdict=dict(name = "Quyen",age=19,country="Nghe An")
print(dict)

# Lay gia tri value duoc chi dinh
x=thisdict.get('name')

# Lay gia tri key
x=thisdict.keys()

# Lay gia tri value
x=thisdict.values()

# Lay theo gia tri cap phan tu
x=thisdict.items()

# Them element vao dict
thisdict['majoring']='Information Technology'
print(thisdict)


# Xoa phan tu ra khoi dict
thisdict.pop('age')
print(thisdict)
# Co the dung (del thisdict['age']) tuong tu
# Ham popitem() se xoa phan tu cuoi cung cua dict
# Ham clear() de xoa toan bo

# Copy dict
mydict=thisdict.copy() # hoac su dung (dict(thisdict))
print(mydict)


# Dict long nhau
my_class={
    "friend1":{
        "name":"Quyen",
        "majoring":"Data Science"
    },
    "friend2":{
        "name":"Nguyen",
        "majoring":"Web Development"
    },
    "friend3":{
        "name":"Viet",
        "majoring":"Game Development"
    }
}
print(my_class["friend1"]["majoring"])
for i,major in my_class.items():
    print(i)
    for j in major:
        print(j+":",major[j])