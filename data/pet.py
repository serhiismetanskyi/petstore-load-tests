"""Pet test data generator."""

import time

from data.test_data import PetTestData


class NewPet(PetTestData):
    """Creates pet test data with random values."""

    def __init__(self):
        """Initialize pet with random category, tag, name and status."""
        self.category = PetTestData.get_pet_category()
        self.tag = PetTestData.get_pet_tag()

        self.id = int(time.time() * 1000)
        self.category_id = self.category["id"]
        self.category_name = self.category["name"]
        self.name = PetTestData.get_pet_name()
        self.photoUrls = "string"
        self.tag_id = self.tag["id"]
        self.tag_name = self.tag["name"]
        self.status = PetTestData.get_pet_status()

    def get_pet(self):
        """Returns pet data dict ready for API request."""
        pet_data = {
            "id": self.id,
            "category": {"id": self.category_id, "name": self.category_name},
            "name": self.name,
            "photoUrls": [self.photoUrls],
            "tags": [{"id": self.tag_id, "name": self.tag_name}],
            "status": self.status,
        }
        return pet_data

    def update_pet_data(self):
        """Returns pet update data with new name and status."""
        self.status = PetTestData.get_pet_status()
        self.name = PetTestData.get_pet_name()
        pet_data_for_update = {"name": self.name, "status": self.status}
        return pet_data_for_update
