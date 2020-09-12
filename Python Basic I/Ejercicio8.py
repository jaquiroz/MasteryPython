#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.extend(new_friend)# Extend debido a que incluimos un termino a la lista con datos de inicio
friends.sort()
 
print(friends)