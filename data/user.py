"""User test data generator."""

import time
from random import randint

from data.test_data import UserTestData


class NewUser(UserTestData):
    """Creates user test data with random values."""

    def __init__(self):
        """Initialize user with random name, email, phone."""
        self.id = int(time.time() * 1000)
        self.firstname = UserTestData.get_first_name()
        self.lastname = UserTestData.get_last_name()
        self.email = f"{self.firstname}_{self.lastname}@mail.com".lower()
        self.username = f"{self.firstname}_{self.lastname}".lower()
        self.password = self.username
        self.phone = UserTestData.get_phone_number()
        self.status = randint(0, 1)

    def get_user(self):
        """Returns user data dict ready for API request."""
        user_data = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.status,
        }
        return user_data

    def update_user_data(self):
        """Returns user update data with new phone number."""
        self.phone = UserTestData.get_phone_number()
        user_data_for_update = {"phone": self.phone}
        return user_data_for_update
