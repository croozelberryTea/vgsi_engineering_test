class House:
    def __init__(self, home, host, port):
        """An object that has all of the fields that are present in the rows of the sample csv. Contains two variants of
        the constructor for either list or dict creation"""
        if type(home) is list:

            self.data = {
                "firstName": home[1],
                "lastName": home[2],
                "street": home[3],
                "city": home[4],
                "state": home[5],
                "zip": home[6],
                "propertyType": home[7],
                "location": "http://{}:{}/api/houses/{}".format(host, port, home[0]),
            }
        elif type(home) is dict:
            self.data = home
