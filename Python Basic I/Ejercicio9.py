#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value.

#Solution
#1
user_profile ={
    'age':21,
    'username':'darklaw32',
    'weapons':['espada','lanza'],
    'is_active':True,
    'clan':'Bolivia',
}

#2
print(user_profile)
#print(user_profile.keys())

#3
user_profile['weapons'].append('hacha')
print(user_profile)

#4
user_profile.update({'is_banned':False})
print(user_profile)

#5
user_profile.update({'is_banned':True})
print(user_profile)

#6
user_profile2 = user_profile.copy()
user_profile2.update({'age':25})
user_profile2.update({'username':'coco25'})
print(user_profile2)
