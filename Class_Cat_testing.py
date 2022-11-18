class Cat:
    colour = ""
    tail = True
    legs = 0
    def cat_says():
        print("Meow.")

bubbs = Cat
bubbs.colour = "Black"
bubbs.legs = 4
bubbs.cat_says()
print(bubbs.colour)
print('Bubbs has {} legs'.format(bubbs.legs))