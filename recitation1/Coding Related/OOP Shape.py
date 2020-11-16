class Shape:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name
        
		

class Circle(Shape):
	def __init__(self, name, radius):
		super().__init__(name)
		self.radius = radius
		

	def calc_area(self):
		return 3.14*(self.radius**2)
		

	def calc_perimeter(self):
		return 2*3.14*self.radius
class Rectangle(Shape):
	def __init__(self, name, width, height):
		super().__init__(name)
		self.width = width
		self.height = height

	def calc_area(self):
		return self.width * self.height

	def calc_perimeter(self):
		return 2*(self.width + self.height)

def main():
	circle1 = Circle("fancy", 5)
	print(circle1.calc_area())
	print(circle1.calc_perimeter())

	rectangle1 = Rectangle("lucky", 3, 4)
	print(rectangle1.calc_area())
	print(rectangle1.calc_perimeter())

if __name__ == '__main__':
    main()
	