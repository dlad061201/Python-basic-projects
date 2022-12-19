import random as rn

def dice():
    x = rn.randint(1,6)

    print("""---------
    [       ]
    [  """,x,"""  ]
    [       ]
    ---------""")
    q = input("Again?")

    if q == "Y" or q == "y":
        dice()
    if q == "N" or q == "n":
        print("stimulator stops")
    else:
        print("Invalid input!!!")


dice()
