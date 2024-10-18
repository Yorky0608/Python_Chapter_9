import random as r

l = [1,3,4,6,2,7,5,9,7,8,10,
     'a','c','b','e','d']

selected = r.sample(l, 4)

print("If any ticket matches these four number or letters wins a prize", end=": ")
for nl in selected:
    print(nl, end=" ")

my_ticket = r.sample(l, 4)

'''Used to draw a new ticket'''
def draw_ticket():
    global my_ticket
    my_ticket = r.sample(l, 4)

run = True
count = 0

'''Checking if a winning ticket has been drawn'''
while run:
    if my_ticket == selected:
        print(f"\nThis ticket, {my_ticket}, won!")
        break
    else:
        count+=1
        print(f"\nThis ticket, {my_ticket}, is not a winner.")
        while True:
            #break
            if input(f"\nWant to draw again? y/n  ").title == 'N':
                run = False
                break
            else:
                break
        draw_ticket()

print(f"It took {count} tickets to draw the winning one.")