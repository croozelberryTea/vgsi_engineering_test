class House:
    def __init__(self, home, host, port):
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
