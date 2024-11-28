s={1,4,2,3,5}
# Luu y set o python se sap xep theo thu tu tu be den lon nhu c++
# Va se khong co su trung lap
s.add(True) # Add them phan tu vao set
# Gia tri True se trung voi 1 va nguoc lai False la 0
print(s)

# Truy cap vao cac phan tu cua set
se={1,2,3,4,101,202,303}
for i in se:
    print(i,end=' ')
print()
# Check su co mat cua 1 item
print(1 in se)

# Update in set (Cong 2 set lai voi nhau)
set1={'orange','banana','apple'}
set2={'pineapple','mango'}
list1=[1,2,3,4]
set1.update(set2)
print(set1)
set2.update(list1) # Update duoc ca list
print(set2)


# Xoa phan tu ra khoi set
set1.remove('banana')
print(set1)

# Union in set (co the dung | thay cho Union)
# Tap hop cua cac tap
set1={'orange','banana','apple'}
set2={1,2,3,'banana'}
set3=set1.union(set2) # set1 | set2 (cung nhan duoc ket qua tuong tu)
print(set3)


# Intersection (Co the su dung toan tu &)
# Tap giao cua cac tap (Chi giu lai ban sao)
set3=set1.intersection(set2)
print(set3)
set1.intersection_update(set2) # (Update ngay o tap goc)
print(set1)

# Tap tru(A\B) (Co the su dung - cho 2 tap)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.difference(set2) #(set1-set2) cung ra ket qua tuong tu
# Phuong thuc update se giu lai o tap goc
set1.difference_update(set2)
print(set3)

# Phuong thuc xoa phan tu trùng ở cả 2 set(co the dung set1^set2 cung ra ket qua tuong tu)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# Tuong tu voi phuong thuc symmetric_difference_update nhu ben tren