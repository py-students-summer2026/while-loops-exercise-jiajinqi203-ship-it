def get_starting_number():
    bottles = ""
    while not bottles.isnumeric() or int(bottles) < 1:
        bottles = input("How many bottles of beer on the wall? ")
    return int(bottles)


def sing(starting_bottles):
    bottles = starting_bottles
    while bottles > 0:
        if bottles > 1:
            if bottles - 1 == 1:
                next_word = "bottle"
            else:
                next_word = "bottles"
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} {next_word} of beer on the wall.")
            print()
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        bottles = bottles - 1