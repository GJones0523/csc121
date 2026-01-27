#
# Gregory Jones
# January 27, 2026
# This program determines what gift card a customer will be awarded from a store
# based on their membership status and the cost of their purchase, as well as
# display the sales tax and calculate the total cost after tax.
#

# Get customer information.
total_purchase = float(input('Enter the total purchase amount: '))
membership = str(input('Is the customer a loyalty program member (y/n): '))

# Calculating sales tax.
sales_tax = total_purchase * 0.065

# Calculating total after tax.
total_taxed = total_purchase + sales_tax

# Display sales tax and total after tax.
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total after tax: ${total_taxed:.2f}")

# Determine gift card amount.
if membership == 'y' and (total_purchase >= 50 and total_purchase <= 100):
    gift_card = 15
elif membership == 'y' and total_purchase > 100:
    gift_card = 25
elif membership == 'n' and total_purchase > 100:
    gift_card = 5
else:
    gift_card = 0

# Display gift card amount.
print(f"Gift Card Awarded: ${gift_card}")