#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) #Output b
print(new_list[-2]) #Output b
print(new_list[1:3])#Output b, c
new_list[0] = 'z' 
print(new_list) #Output z, b, c

my_list = [1,2,3]
bonus = my_list + [5] #Output 1, 2, 3, 4, 5
my_list[0] = 'z'
print(my_list) #Output z, 2, 3
print(bonus) #Output 1, 2, 3, 5