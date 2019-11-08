import sys

from server import mongo


class User():
    @classmethod
    def get(self):
        users = mongo.db.users.find()
        user_list = []

        return user_list

    def insert(self, data):
        users = mongo.db.users
        # print('Luu thanh cong', file=sys.stderr)
        return str(users.insert(data))

    def login(self, email, password):
        user = mongo.db.users.find({})
        return True
