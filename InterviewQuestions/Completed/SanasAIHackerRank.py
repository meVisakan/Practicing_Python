# Inaccuracy in the functionality logic to get the vendor and price with the least price in the table

mobile_dict = {"Apple": 660, "Blackberry": 300, "Samsung": 440, "OnePlus": 120}
lowest_price = min(mobile_dict.items(), key=lambda x: x[1])
lowest_price_dict = {lowest_price[0]: lowest_price[1]}
print(lowest_price_dict)
