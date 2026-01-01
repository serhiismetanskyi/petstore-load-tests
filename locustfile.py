"""
Main Locust file.
"""

from tests.test_order import OrderTestUser
from tests.test_pet import PetTestUser
from tests.test_user import TestUser

__all__ = ["PetTestUser", "TestUser", "OrderTestUser"]
