# start with users that need to be verified, 
# and an empty list to hold comfirmed users.


unconfirmed_users = ['alice', 'brian','candace']
confirmed_users = []

# verify each user until there are no more uncomfirmed users.
# Move each verified user into the list of comfirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


# display all comfrimed users.
print("\nThe following users have been comfirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())