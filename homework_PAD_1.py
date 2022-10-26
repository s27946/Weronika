my_string2 = 'This is actually a significantly longer phrase than the previous one'
split_string2_list = my_string2.split()
# print(split_string2_list)
# nie możemy tutaj przechować wartości, bo mamy output jako "None", w tej funkcji
# został użyty return, my wywołujemy metodę na jakiejś instniejącej danej
# w naszym przypadku wywołujemy metodę na liście i zmieniamy jej kolejność
# nie zmieniamy typu danych, nie wykonujemy procesu
split_string2_list.reverse()
print(split_string2_list)
string_again = " ".join(split_string2_list)
# # tutaj output to będzie string, przechowujemy sobie go w zmiennej
print(string_again)

d = {'start here': 1,
     'k1': [1, 2, 3, {'k2': [1, 2, {'k3': ['keep going', {'further': [1, 2, 3, 4, [{'k4': 'python'}]]}]}]}]}
print(d['k1'][3]['k2'][2]['k3'][1]['further'][4])

sklep = {'ceny': [{'pomidor': 0.87}, {'cukier': 1.09}, {'gąbki': 0.29}, {'sok': 1.89}, {'folia': 1.29}],
         'rozmiary_opakowania': [{'pomidor': "Pack of 6"}, {'cukier': "500g"}, {'gąbki:'"Pack of 10"},
                                 {'sok': "1.5l bottle"}, {'folia': "30m roll"}]}
print(sklep)

pack_cost = sklep['ceny']
print(pack_cost)
pack_sizes = sklep['rozmiary_opakowania']
print(pack_sizes)
quant = [18, 2, 4.5, 4, 2]
# tsp = pack_cost[0] * quant[0] * pack_sizes[0]
# print(tsp)
# pack_size = sklep['rozmiary_opakowania'[0]]
# tsp = pack_cost *

# petla for cw 1
count_odd = 0
count_even = 0
for number in range(1, 100):
    if number % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1

print("Number of Even Numbers: {}".format(count_even))
print("Number of Odd Numbers: {}".format(count_odd))

# petla for cw.2
order_list = [("tom", 0.87, 4),
              ("sug", 1.09, 3),
              ("ws", 0.29, 4),
              ("juc", 1.89, 1),
              ("fo", 1.29, 2)]

names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 16.00
running_total = 0
receipt = []

# rozpakowanie krotek w liście
for order, price, amount in order_list:
    if running_total > budget:
        print('Przekroczono budżet!')
        break
    else:
        running_total = running_total + price * amount
        print("Current Total: $ {}".format(running_total))
        print("Added {} ({})".format((names[order]), amount))
        budget = budget - price * amount
        receipt.append(order)

print("The total for the order is: £{:5.2f}".format(running_total))
print("The items in the order are: {}".format(receipt))
print("The remaining budget is: £{:5.2f}".format(budget))

my_list = [34, 52, 71, 39, 22, 73, 92]

my_new_list = [x ** 2 if x % 2 == 0 else (x ** 2 + 1) for x in list(my_list)]
print(my_new_list)

shop_dict = {"tom": 0.87,
             "sug": 1.09,
             "ws": 0.29,
             "cc": 1.89,
             "ccz": 1.29}

names_dict = {"tom": "Tomatoes",
              "sug": "Sugar",
              "ws": "Washing Sponges",
              "cc": "Coca-Cola",
              "ccz": "Coca-Cola Zero"}
# Each item in the "shop_dict" is a value. Keys and values are not two seperate
# values in the dictionary. We solve this error by using a method called items()
# This method analyzes a dictionary and returns keys and values stored as tuples
filtered_shop = [names_dict[key] for key, value in shop_dict.items() if value > 1.00]

print(filtered_shop)

#bonus
for x in range(10, 51):
    for i in range(2, x):
        if x % i == 0:
            print('The number is not a prime number: {} '.format(x))
            break
        elif i == x-1:
            print('The number is a prime number: {} '.format(x))
            







