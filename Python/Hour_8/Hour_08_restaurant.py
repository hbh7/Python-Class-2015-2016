print ("Hunter Harris - 12-7-15")

def print_seat(seat):
    for item in seat:
        print ("${}".format(item))
        print ("-"*15)
        total = get_seat_total(seat)
        print ("Total: ${}".format(total))

def get_seat_total(seat):
    total = 0
    for dish in seat:
        total = total + dish
    return total

def main():
    seats = [[23.95 + 4.00],
        [12.50/2 + 14.85 + 4.00],
        [12.50/2 + 11.95 + 2.00]]
    grand_total = 0
    for seat in seats:
        print_seat(seat)
        grand_total = grand_total + get_seat_total(seat)
        print ("\n")
    print ("="*15)
    print ("Grand total: ${}".format(grand_total))
    
if __name__ == "__main__":
 main() 
