class TestMath:
    #function called everytime an object is created to allow the class initialize the object's attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test_add(self):
        return self.x + self.y

    def test_subtract(self):
        return self.x - self.y

    def test_milutiply(self):
        return self.x * self.y
