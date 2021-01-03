from Model.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user:
        if user.password == password:
            return user
        else:
            return {'message': 'The password is wrong'}, 400
    else:
        return {'message': 'This username does not exists'}, 400


def identification(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
