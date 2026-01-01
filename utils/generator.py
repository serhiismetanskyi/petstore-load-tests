"""Fake data generator using Faker library."""

from faker import Faker


class DataGenerator:
    """Generates fake test data using Faker library."""

    def __init__(self, seed=None):
        """Initialize Faker. Optional seed for reproducible data."""
        self.fake = Faker()
        if seed:
            self.fake.seed(seed)

    def first_name(self):
        """Returns random first name."""
        return self.fake.first_name()

    def last_name(self):
        """Returns random last name."""
        return self.fake.last_name()

    def phone_number(self):
        """Returns random phone number."""
        return self.fake.phone_number()
