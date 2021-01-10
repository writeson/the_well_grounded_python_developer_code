import pickle
from logging import getLogger
from pathlib import Path
from flask import current_app
from flask_bcrypt import generate_password_hash, check_password_hash
from . import login_manager

logger = getLogger(__name__)

class User:
    USERS = {}
    ID_COUNTER = 1

    def __init__(self, email, password):
        self.id = self.ID_COUNTER
        self.ID_COUNTER += 1
        self.email = email
        self._password_hash = generate_password_hash(password)
        self._authenticated = False

    # required attributes for flask_login        
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self._authenticated

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    @property
    def authenticated(self):
        raise AttributeError("authenticated is not a readable attribute")

    @authenticated.setter
    def authenticated(self, value):
        self._authenticated = False
        User.write_users(User.USERS)

    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)

    def is_authenticated(self):
        return self._authenticated        

    @staticmethod
    def get_by_email(email):
        if email in User.USERS:
            return User.USERS.get(email)

    @staticmethod
    def get_by_id(id):
        for email, user in User.USERS.items():
            if id == user.id:
                return User.USERS.get(user.email)
                    
    @staticmethod
    def add_user(user):
        User.USERS[user.email] = user
        # save users to file
        User.write_users(User.USERS)

    @staticmethod
    def read_users():
        """Read users file into the system
        """
        app_path = Path(current_app.root_path)
        myblog_root_path = app_path.parent
        user_path = myblog_root_path / "data" / "users.data"
        with open(user_path, mode="rb") as fh:
            User.USERS = pickle.load(fh)
        logger.debug("read users data from file")            

    @staticmethod
    def write_users(users):
        """Write the users file out to the system
        """
        app_path = Path(current_app.root_path)
        myblog_root_path = app_path.parent
        user_path = myblog_root_path / "data" / "users.data"
        with open(user_path, mode="wb") as fh:
            pickle.dump(User.USERS, fh)
        logger.debug("wrote users data to file")            


# read the users into the class one time on import of the module
User.read_users()        


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)
