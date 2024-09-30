user_registered = {}

def register_user(user_id):
    user_registered[user_id] = True

def is_user_registered(user_id):
    return user_registered.get(user_id, False)
