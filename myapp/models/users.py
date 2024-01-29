# store the users in memory
users = []


# return the list of serialized users
def get_users():
    return [u.serialize() for u in users]


class User:
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    # serialize the user's data
    def serialize(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    # get list of users
    def all():
        return get_users()

    # find the user with the given id
    def find(id: int, serialize=True):
        for user in users:
            if user.id == id:
                if serialize:
                    return user.serialize()
                else:
                    return user
        return None

    # create a new user
    def save(self):
        users.append(self)
        return self.serialize()

    # update the user's attributes
    def update(self, **kwargs):
        # update the user's attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

        # return the user's serialized data
        return self.serialize()

    # delete the user
    def delete(self):
        users.remove(self)
        return self.serialize()
