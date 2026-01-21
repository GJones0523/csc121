#
# Gregory Jones
# January 15, 2026
# This program receives input on the amount of each item being purchased
# and then calculates the total price of goods both before
# and after tax is applied.
#

# Constants
books_price = 2.25
DVDs_price = 4.35
games_price = 5.00

# This section of code receives input.
books_number = int(input("Enter the number of books: "))

DVDs_number = int(input("Enter the number of DVDs: "))

games_number = int(input("Enter the number of games: "))

# This section of code processes the inputs.
total = (books_price * books_number) + \
        (DVDs_price * DVDs_number) + \
        (games_price * games_number)

sales_tax = total * 0.065

total_taxed = sales_tax + total

# This section of code produces the output.
print(f"Total before tax: ${total:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total after tax: ${total_taxed:.2f}")
