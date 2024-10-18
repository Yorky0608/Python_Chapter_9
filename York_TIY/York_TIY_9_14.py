import random as r

l = [1,3,4,6,2,7,5,9,7,8,10,
     'a','c','b','e','d']

selected = r.sample(l, 4)

print("If any ticket matches these four number or letters wins a prize", end=": ")
for nl in selected:
    print(nl, end=" ")