# Inaccuracy in the functionality logic to get the vendor and price with the least price in the table

mobile_dict = {"Blackberry": 300, "Samsung": 440, "Apple": 660, "OnePlus": 120}
lowest_price = min(mobile_dict.items(), key=lambda x: x[0])
lowest_price_dict = {lowest_price[0]: lowest_price[1]}
print(lowest_price_dict)
