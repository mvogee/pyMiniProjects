
# the __ before the variables means they are private
# self refers to the self object
# __init__ is a constructor that can be used for the object initialization

class Shape:

	__sides = 0
	__area = 0.0
	__perimeter = 0.0

	def __init__(self, sides, area, perimeter):
		self.__sides = sides
		self.__area = area
		self.__perimeter = perimeter

	def setSides(self, sides):
		self.__sides = sides

	def getSides(self):
		return (self.__sides)

	def setArea(self, area):
		self.__area = area

	def getArea(self):
		return (self.__area)

	def setPerimeter(self, perimeter):
		self.__perimter = perimeter

	def getPerimeter(self):
		return (self.__perimeter)


class Square(Shape):

	__sidelen = 0.0

	def __init__(self, sidelen):
		self.__sidelen = sidelen
		super(Square, self).__init__(4, self.__sidelen ** 2, self.__sidelen * 4)

	def setSidelen(self, sidelen):
		self.__sidelen = sidelen
		super(Square, self).setArea(self.__sidelen ** 2)
		super(Square, self).setPerimeter(self.__sidelen * 4)

class Rectangle(Shape):
	__length = 0.0
	__height = 0.0

	def __init__(self, length, height):
		self.__length = length
		self.__height = height
		super(Rectangle, self).__init__(4,
									self.__height * self.__length,
									(self.__height * 2) + (self.__length * 2))

	def setHeight(self, height):
		self.__height = height
		super(Rectangle, self).setArea(self.__height * self.__length)
		super(Rectangle, self).setPerimeter((self.__height * 2) + (self.__length * 2))

	def setLength(self, length):
		self.__length = length
		super(Rectangle, self).setPerimeter((self.__height * 2) + (self.__length * 2))
		super(Rectangle, self).setArea(self.__height * self.__length)

# class Triangle(Shape):
# 	__side1 = 0.0
# 	__side2 = 0.0
# 	__side3 = 0.0
#
# 	def __init__(self, side1, side2, side3):
# 		self.__side1 = side1
# 		self.__side2 = side2
# 		self.__side3 = side3
# 		super(Triangle, self).__init__(3, )
#
# 	def setSide(self, sidelen, whichside):
# 		if (whichside == 1):
# 			self.__side1 == sidelen
# 		elif(whichside == 2):
# 			self.__side2 == sidelen
# 		else:
# 			self.__side3 == sidelen
# 		super.setArea =
#
# 	def triArea(slef)


mysquare = Square(5)
print(mysquare.getArea())
mysquare.setSidelen(10)
print(mysquare.getArea())

print()

myrectangle = Rectangle(4, 2)
print(myrectangle.getArea())
myrectangle.setHeight(5)
print(myrectangle.getArea())
