"""Order test data generator."""

import datetime
import time
from random import randint

from data.test_data import OrderTestData


class NewOrder(OrderTestData):
    """Creates order test data for a given pet."""

    def __init__(self, petId):
        """Initialize order with random quantity and status."""
        self.id = int(time.time() * 1000)
        self.petId = petId
        self.quantity = randint(1, 5)
        self.shipDate = str(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.status = OrderTestData.get_order_status()
        self.complete = "false"

    def get_order(self):
        """Returns order data dict ready for API request."""
        order_data = {
            "id": self.id,
            "petId": self.petId,
            "quantity": self.quantity,
            "shipDate": self.shipDate,
            "status": self.status,
            "complete": self.complete,
        }
        return order_data

    def update_order_data(self):
        """Returns order update data marking order as complete."""
        self.complete = "true"
        order_data_for_update = {"complete": self.complete}
        return order_data_for_update
