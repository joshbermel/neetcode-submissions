class TimeMap:

    def __init__(self):
        

    # key and value pairs where the key is the key and the value is an array
    # to set, go to that key, find the val, and append to array
    # to get, go to that key, find that timestamp (position in array) and
    # return that value
    # the array for my key needs to be as large as the timestamp I am
    # setting a value at


    # make the default value something that values can't be set to
    # like $

        self.d = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        # if that key isn't there yet
        if key not in self.d:
            # create a new empty array
            self.d[key] = ["$"] * (timestamp + 1)
            # set the first entry as the value at slot timestamp
            self.d[key][timestamp] = value
            return
        # elsewise, key already exists
        # set the value at the timestamp slot
        size_diff = timestamp - len(self.d[key]) + 1
        if size_diff > 0:
            for i in range(size_diff):
                self.d[key].append("$")
        self.d[key][timestamp] = value
 
    # if we ask for a timestamp that is not stored yet but bigger than 
    # any time stamp stored yet then we just return the value at the 
    # biggest time step
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        if timestamp > len(self.d[key]) - 1:
            return self.d[key][-1]

        if self.d[key][timestamp] == "$":
            val = timestamp
            while self.d[key][val] == "$":
                if val == 0:
                    return ""
                val -= 1
            return self.d[key][val]
        

        return self.d[key][timestamp]

        
