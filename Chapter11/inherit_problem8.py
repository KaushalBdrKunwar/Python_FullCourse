#Write len() method to print the vector

class Vector:
    def __init__(self, list):
        self.l = list
    
    def __len__(self):
        return len(self.l)


v1 = Vector([1, 2, 3])
print(len(v1))