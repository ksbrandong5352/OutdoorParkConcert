class User:
  def __init__(self, name, email, purchase_amount):
    self.balance = purchase_amount # keeps track of purchases
    self.seats = [] # list of seats they bought
    self.name = name
    self.email = email


def create_seating(rows, cols):
  return [["a" for _ in range(cols)] for _ in range(rows)]

def print_seating(seat_data, users):
  output_string = f"   "
  # print out column letters first
  for c in range(26):
    char = chr(97 + c)
    output_string += f" {char}" # 97 is ascii code for 'a'
  # print out each row
  for number, row in enumerate(seat_data):
    output_string += f"\n {number + 1:>{2}}"
    for seat in row:
      output_string += f" {seat}"
  print(output_string)

def buy_seats(seat_data, users):
  def edit_seating(row, col):
    if seat_data[row][col] == "a":
      seat_data[row][col] = "X"
      return True
    else:
      return False

  prices = {
    range(5) : 80,
    range(5, 11) : 50,
    range(11, 20) : 25
  }

  numtickets = int(input("Number of tickets: "))
  i = 0
  purchase_amount = 0
  while i < numtickets:
    rowinput = int(input("Enter row number: ")) - 1
    colinput = ord(input("Enter seat letter: ").lower()) - 97
    if (rowinput <= len(seat_data)) and (colinput <= len(seat_data[0])):
      if edit_seating(rowinput, colinput):
        for pricebracket in prices:
          if rowinput in pricebracket:
            purchase_amount += prices[pricebracket]
        i += 1
        continue
      else:
        print("Seat has already been purchased")
        i = 0
        continue
    else:
      print("Invalid input, order canceled")
      break
  uname = input("Enter reservation name: ")
  usrmail = input("Enter e-mail address: ")
  print(f"Purchase of {numtickets} ticket for ${purchase_amount} successful")
  users.append(User(uname, usrmail, purchase_amount))

def search(seat_data, users):
  searchstring = input("Get information for user: ")
  for user in users:
    if searchstring == user.name:
      print(f"Seats: {user.seats}\n"
            f"Balance: ${user.balance}")

def display_purchases(seat_data, users):
  purchases = f""
  total_income = 0
  for user in users:
    purchases += f"seats {user.seats} for a total of ${user.balance}\n"
    total_income += user.balance
  print(purchases)
  print(f"Total income: ${total_income}")
  

def main():
  seating = create_seating(20, 26)
  users = []

  dispatch = {
    "v": print_seating,
    "b": buy_seats,
    "s": search,
    "d": display_purchases,
  }
  while True:
    print(f"Menu:\n"
        f" [V]iew Seats\n"
        f" [B]uy Seats\n"
        f" [S]earch for Seats\n"
        f" [D]isplay Purchases\n"
        f" [Q]uit")
    usrinput = input()
    if usrinput.lower() in dispatch:
      dispatch[usrinput](seating, users)
    elif usrinput.lower() == "q":
      break
    else:
      print("Invalid Input")

if __name__ == "__main__":
  main()
