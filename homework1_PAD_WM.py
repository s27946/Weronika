# Ćwiczenie 1a
def check_range(x,y,z):
    if (x >= y and x <= z):
        print("{} jest między {} a {}".format(x,y,z))
    else:
        print("{} nie jest między {} a {}".format(x,y,z))
check_range(34, 9, 228)
check_range(7, 2, 5)

#Ćwiczenie 1b
def bool_range(x,y,z):
    condition = (x >= y and x <= z)
    if condition:
        print(condition)
    else:
        print(condition)
bool_range(34, 9, 228)
bool_range(7, 2, 5)

#Ćwiczenie 2
my_list = [1,3,5,6,4,3,2,3,3,4,3,4,5,6,6,4,3,2,12,3,5,63,4,5,3,3,2]

def unique_list(list):
    list_unique = []
    for x in list:
        if x in list_unique:
            continue
        else:
            list_unique.append(x)
    return list_unique

print(unique_list(my_list))
#inny sposób bez wykonywania funkcji:
set_of_my_list = set(my_list)
print(set_of_my_list)

#Ćwiczenie 3
def volume_of_sphere(radius):
    volume_of_sphere = 4/3 * 3.14 * (radius ** 3)
    return round(volume_of_sphere,2)
print(volume_of_sphere(2))

#Ćwiczenie 4
def num_fact(number):
    if number == 1:
        return 1git
    else:
        return(number * num_fact(number-1))

num_fact(10)
print(num_fact(10))










