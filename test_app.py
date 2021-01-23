import configparser
import json
import unittest

import app

config = configparser.ConfigParser()
config.read("settings.ini")
HOST = config["DEFAULT"]["host"]
PORT = config["DEFAULT"]["port"]

BASE_URL = "http://localhost:5001/"
    #"http://{}:{}".format(HOST, PORT)
HOUSE_URL = "{}/api/houses/".format(BASE_URL)
BAD_ITEM_URL = "{}12".format(HOUSE_URL)
ADD_ITEM_URL = "{}11".format(HOUSE_URL)
GOOD_ITEM_URL = "{}3".format(HOUSE_URL)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # because yes its important enough to get tested :)
        res = self.app.get(BASE_URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_data().decode('utf-8'), "Hello World!")

    def test_houses_all(self):
        """Get all houses test"""
        res = self.app.get(HOUSE_URL)
        data = json.loads(res.get_data().decode("utf-8"))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data["items"]), 10)
        self.assertEqual(data["itemCount"], 10)

    def test_get_houses_by_id_01(self):
        """Get by id test for success"""
        res = self.app.get(GOOD_ITEM_URL)
        data = json.loads(res.get_data().decode("utf-8"))
        x = {'city': ' Hudson', 'firstName': ' Jane', 'lastName': ' Willson', 
             'location': 'http://LOCALHOST:5001/api/houses/3', 'propertyType': ' Multi Family', 'state': ' MA', 
             'street': ' Fuyat St', 'zip': ' 01749'}
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, x)  # hard coded this test, for this example it works fine tho
        
    def test_get_houses_by_id_02(self):
        """Get by id test for failure"""
        res = self.app.get(BAD_ITEM_URL)
        self.assertEqual(res.status_code, 404)

    def test_put_houses_by_id_01(self):
        """PUT update existing object test for success"""
        edit = {"city": " Not Hudson", "firstName": " Jane", "lastName": " Doe", "location": "http://LOCALHOST:5001/api/houses/3", "propertyType": " Single Family", "state": " MA", "street": " Edit Ln", "zip": " 12345"}

        res = self.app.put(GOOD_ITEM_URL, data=json.dumps(edit), content_type='application/json')
        data = json.loads(res.get_data().decode("utf-8"))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, edit)

    def test_put_houses_by_id_02(self):
        """PUT update existing object with malformed data"""
        edit = {"city": " Not Hudson", "firstName": " Jane", "lastName": " Doe",
                "location": "http://LOCALHOST:5001/api/houses/3"}
        res = self.app.put(GOOD_ITEM_URL, data=json.dumps(edit), content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_put_houses_by_id_03(self):
        """PUT update new object test for success"""
        # note for test data, make sure the location matches the url, data checking updates it to match when it puts but
        # then the assert will fail
        edit = {"city": " new town", "firstName": " tyler", "lastName": " crosby", "location": "http://LOCALHOST:5001/api/houses/11", "propertyType": " Single Family", "state": " me", "street": " Maine St", "zip": " 13579"}
        res = self.app.put(ADD_ITEM_URL, data=json.dumps(edit), content_type='application/json')
        data = json.loads(res.get_data().decode("utf-8"))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, edit)


if __name__ == "__main__":
    unittest.main()
