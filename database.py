from models.house import House


class Database:
    def __init__(self, host, port):
        """
        Database class just reads the file from the example on initialization and stores it in a more usable format
        in memory.
        """
        self.data = {}
        tmp = []
        self.host = host
        self.port = port
        # load the raw data into data array
        with open("data/houses.csv", "r") as f:
            for line in f:
                tmp.append(line.strip().split(","))

        # remove the header
        del tmp[0]

        # update the data to use a model for ease of use and use a map with the id as the key for quick lookup
        for x in tmp:
            self.data[x[0]] = House(x, self.host, self.port)
        print(self.data)

    def get_houses_all(self):
        """
        Collects all of the houses objects dict representations in a list and returns it
        """
        all_houses = []
        for x in self.data:
            all_houses.append(self.data[x].data)
        return all_houses

    def get_houses_by_id(self, house_id):
        """
        Searches for the requested house_id as a key in the hashmap/db if it finds it, it will return the dict
        representation. If it fails to find a matching key it will return None.
        """
        try:
            res = self.data[house_id].data
        except KeyError:
            print("pain")
            return None
        return res

    def put_houses_by_id(self, house_id, house_data):
        """
        Searches for requested house_id as a key in the hashmap/db if it finds it, it will take the validated request
        body and replace the old content. If it fails to find the house_id it will create a new object and return its
        dict representation.
        """
        if house_id in self.data.keys():
            self.data[house_id].data = house_data
        else:
            self.data[house_id] = House(house_data, self.host, self.port)
        return self.data[house_id].data
