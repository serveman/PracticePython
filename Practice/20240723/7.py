# Create a sample collection
users = {
    'Hans': 'active', 
    'Eleonore': 'inactive',
    '김씨': 'active'
    }

# Strategy: Iterate over a copy
print('original: ', users)
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print('after process: ', users)
print()

# Strategy: Create a new collection
another_users = {
    'Hans': 'active', 
    'Eleonore': 'inactive',
    '김씨': 'active'
    }
active_users = {}
print('original: ', another_users)
for user, status in another_users.items():
    if status == 'active':
        active_users[user] = status
print('after process (another_users): ', another_users)
print('after process (active_users):  ', active_users)
