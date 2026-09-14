class TimeMap:

    def __init__(self):
       self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage.keys():
            self.storage[key] = []
            
        self.storage[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage.keys():
            return ""
        
        currentList = self.storage[key]

        l, r = 0, len(currentList) -1
        middle = 0

        while l <= r:
            middle = (l+r)//2
            if timestamp == currentList[middle][0]:
                return currentList[middle][1]
            elif timestamp < currentList[middle][0]:
                r = middle - 1
            else:
                l = middle + 1

        middle = (l+r)//2
        if timestamp < currentList[middle][0]:
            return ""
        return currentList[middle][1]
