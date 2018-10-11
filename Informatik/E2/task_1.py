# Please do not modify this part of the code!
price_banana = 1.5
price_milk = 2.0
number_of_bananas_purchased = 4
number_of_milks_purchased = 3

# Your code goes here
promotion_percentage = int(input("How high is your discount coupon?"))  # 1
subtotal_price = number_of_bananas_purchased * price_banana + number_of_milks_purchased * price_milk  # 2
print("The subtotal of your purchase is %s" % subtotal_price)  # 3
savings = promotion_percentage / 100 * subtotal_price  # 4
print("Your savings are %s" % savings)  # 5
total_price = subtotal_price - savings  # 6
print("The total price of your purchase is %s" % total_price)  # 7
