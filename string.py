class Circle:
    def __init__(self,radious):
        self.radious=radious
    def Area(self):
        self.area=self.radious*self.radious*3.14
        print(self.area)
    def Perimeter(self):
        self.perimeter=self.radious*2*3.1416
        print(self.perimeter)
c1=Circle(5)
c1.Perimeter()
   











