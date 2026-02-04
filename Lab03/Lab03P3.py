#
# Gregory Jones
# February 3, 2026
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

# Make sure the amount of books is between 0 and 30
while books_number < 0 or books_number > 30:
        print('Number of books must be between 0 and 30')
        books_number = int(input("Enter the number of books: "))

DVDs_number = int(input("Enter the number of DVDs: "))

# Make sure the number of DVDs is between 0 and 15
while DVDs_number < 0 or DVDs_number > 15:
        print('Number of DVDs must be between 0 and 15')
        DVDs_number = int(input("Enter the number of DVDs: "))

games_number = int(input("Enter the number of games: "))

# Make sure the number of games is between 0 and 10
while games_number < 0 or games_number > 10:
        print('Number of games must be between 0 and 10')
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
