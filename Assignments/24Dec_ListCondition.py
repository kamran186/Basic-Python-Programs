requested_toppings=['mushroom','green peppers','extra cheese']

if 'green peppers' and 'mushroom' not in requested_toppings:
    print("Sorry we are out of service")
else:
    print(" Hai")


current_users=['kamran186','vigilante186','admin','abc123','batman0000']

new_users=['new1','new2','kamran186','batman0000','ADMIN'];

for new_user in new_users:
    if new_user in current_users:
        print('It already exists')
    else:
        current_users.append(new_user)
        print("Added Successfully")

print(current_users)

for i in range(0,len(current_users)):
    current_users[i]=current_users[i].upper()

print(current_users)
