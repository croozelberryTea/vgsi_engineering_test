import configparser
import unittest
import models

import database

config = configparser.ConfigParser()
config.read("settings.ini")
HOST = config["DEFAULT"]["host"]
PORT = config["DEFAULT"]["port"]


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = database.Database(HOST, PORT)

    def test_init(self):
        """Test to make sure that the data is in dict format and contains only House models"""
        self.assertEqual(type(self.db.data), dict)
        for x in self.db.data:
            self.assertEqual(type(self.db.data[x]), models.house.House)

    def test_get_houses_all(self):
        """Test to make sure that the data that is returned from get_houses_all matches the standard data from the file"""
        expected = [
            {
                "firstName": " Jack",
                "lastName": " Smith",
                "street": " South St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Single Family",
                "location": "http://LOCALHOST:5001/api/houses/1",
            },
            {
                "firstName": " Fred",
                "lastName": " Mack",
                "street": " Central St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Multi Family",
                "location": "http://LOCALHOST:5001/api/houses/2",
            },
            {
                "firstName": " Jane",
                "lastName": " Willson",
                "street": " Fuyat St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Multi Family",
                "location": "http://LOCALHOST:5001/api/houses/3",
            },
            {
                "firstName": " Sue",
                "lastName": " Jones",
                "street": " Park St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Multi Family",
                "location": "http://LOCALHOST:5001/api/houses/4",
            },
            {
                "firstName": " Jeff",
                "lastName": " Black",
                "street": " Elm St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Single Family",
                "location": "http://LOCALHOST:5001/api/houses/5",
            },
            {
                "firstName": " Jenny",
                "lastName": " Wright",
                "street": " Main St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Single Family",
                "location": "http://LOCALHOST:5001/api/houses/6",
            },
            {
                "firstName": " Jake",
                "lastName": " Wilcox",
                "street": " Carter St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Multi Family",
                "location": "http://LOCALHOST:5001/api/houses/7",
            },
            {
                "firstName": " Sally",
                "lastName": " Turner",
                "street": " Cox St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Single Family",
                "location": "http://LOCALHOST:5001/api/houses/8",
            },
            {
                "firstName": " Bill",
                "lastName": " Jet",
                "street": " Dewey St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Multi Family",
                "location": "http://LOCALHOST:5001/api/houses/9",
            },
            {
                "firstName": " Dan",
                "lastName": " Sandstone",
                "street": " River St",
                "city": " Hudson",
                "state": " MA",
                "zip": " 01749",
                "propertyType": " Single Family",
                "location": "http://LOCALHOST:5001/api/houses/10",
            },
        ]
        actual = self.db.get_houses_all()
        self.assertEqual(expected, actual)

    def test_get_houses_by_id_01(self):
        """Test to make sure that getting by id returns expected value"""
        expected = {
            "firstName": " Jack",
            "lastName": " Smith",
            "street": " South St",
            "city": " Hudson",
            "state": " MA",
            "zip": " 01749",
            "propertyType": " Single Family",
            "location": "http://LOCALHOST:5001/api/houses/1",
        }
        actual = self.db.get_houses_by_id("1")
        self.assertEqual(expected, actual)

    def test_get_houses_by_id_02(self):
        """Test to make sure that getting by id a House that doesn't exist returns None"""
        actual = self.db.get_houses_by_id(11)
        self.assertEqual(actual, None)

    def test_put_houses_by_id_01(self):
        """Test to make sure that data is updated correctly in db"""
        edit = {
            "city": " new town",
            "firstName": " tyler",
            "lastName": " crosby",
            "location": "http://LOCALHOST:5001/api/houses/1",
            "propertyType": " Single Family",
            "state": " me",
            "street": " Maine St",
            "zip": " 13579",
        }
        actual = self.db.put_houses_by_id("1", edit)
        self.assertEqual(actual, edit)
        self.assertEqual(edit, self.db.get_houses_by_id("1"))

    def test_put_houses_by_id_02(self):
        """Test to make sure that if data that is put but doesn't exist will create an object with that id"""
        edit = {
            "city": " new town",
            "firstName": " tyler",
            "lastName": " crosby",
            "location": "http://LOCALHOST:5001/api/houses/11",
            "propertyType": " Single Family",
            "state": " me",
            "street": " Maine St",
            "zip": " 13579",
        }
        actual = self.db.put_houses_by_id("11", edit)
        self.assertEqual(actual, edit)
        self.assertEqual(edit, self.db.get_houses_by_id("11"))
