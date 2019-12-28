from reception import Hotel


if __name__ == "__main__":
    print()
    hotel = Hotel()
    print(" ---- Welcome to Vaibhav-Hotel ----")
    while True:
        inp = int(input("""
        1) New Check-in
        2) Checkout
        3) Restaurant (Food-Order)
        4) Quit

        """))

        if 1 == inp:
            hotel.check_in()
        elif 2 == inp:
            hotel.check_out()
        elif 3 == inp:
            hotel.order_food()
        else:
            print("Wrong choices, Try Again !!")
