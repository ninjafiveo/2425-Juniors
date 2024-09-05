# Returns
from statistics import mean 
def temps (temp1, temp2, temp3):
    the_list = {temp1, temp2, temp3}
    the_average = mean(the_list)
    return the_average

average_1 = temps(10, 95, 1010)
average_2 = temps(20, 65, 110)
average_3 = temps(30, 75, 9010)
average_4 = temps(40, 985, 10)

print(average_1)
print(average_2)
print(average_3)
print(average_4)