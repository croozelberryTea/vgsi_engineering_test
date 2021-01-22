from models.house import House


class Database:
    def __init__(self, host, port):
        """Database class just reads the file from the example on initialization"""
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

        # update the data to use a model for ease of use
        for x in tmp:
            self.data[x[0]] = House(x, self.host, self.port)
        print(self.data)

    def get_houses_all(self):
        all_houses = []
        for x in self.data:
            all_houses.append(self.data[x].data)
        print(self.data)
        return all_houses

    def get_houses_by_id(self, house_id):
        return self.data[house_id].data

    def put_houses_by_id(self, house_id, house_data):
        self.data[house_id].data = house_data
        print(self.data)
        return self.data[house_id].data
