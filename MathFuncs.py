from __future__ import annotations
import math

def lerp(start, goal, alpha: float):
    if type(start) != type(goal):
        RuntimeError("start and goal are nonequivalent types")
    else:
        pass

class Vector3D(object):
    def __init__(self, vX: float, vY: float, vZ: float):
        self._x = vX
        self._y = vY
        self._z = vZ

        self._magnitude = math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)))
        self._unit = [self.x / self.magnitude, self.y / self.magnitude, self.z / self.magnitude]

        self.coordinates = [self._x, self._y, self._z]

    
    def multiply(self, multiplier: float | int | Vector3D):
        if type(multiplier) == float or type(multiplier) == int: # scalars
            new_multiplied_coordinates = []

            for CoordIndex in range(0, 3):
                new_multiplied_coordinates.append(self.coordinates[CoordIndex] * multiplier)
            
            self.coordinates = new_multiplied_coordinates
            print(self.coordinates)
        elif type(multiplier) == Vector3D: # vectors
            self.coordinates = [self.x * multiplier.x, self.y * multiplier.y, self.z * multiplier.z]
        else:
            RuntimeError("invalid multiplier, got: " + str(type(multiplier)))


    def divide(self, divisor: int | float | Vector3D):
        if type(divisor) == float or type(divisor) == int: # scalars
            new_divided_coordinates = []
            
            for CoordIndex in range(0, 3):
                new_divided_coordinates.append(self.coordinates[CoordIndex] / divisor)

            self.coordinates = new_divided_coordinates
        elif type(divisor) == Vector3D: # vectors
            self.coordinates = [self.x / divisor.x, self.y / divisor.y, self.z / divisor.z]
        else:
            RuntimeError("invalid divisor type, got: " + str(type(divisor)))
    
    def add(self, vector: Vector3D):
        for coord in range(len(self.coordinates)):
            self.coordinates[coord] += vector.coordinates[coord]

    def subtract(self, vector: Vector3D):
        for coord in range(len(self.coordinates)):
            self.coordinates[coord] -= vector.coordinates[coord]
    
    def dot(self, vector: Vector3D):
        return 

    def cross(self, vector: Vector3D):
        pass

    @property
    def coordinates(self):
        return self._coordinates
    @coordinates.setter
    def coordinates(self, value):
        self._x = value[0]
        self._y = value[1]
        self._z = value[2]

        self._coordinates = value
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z

    @property
    def magnitude(self):
        return math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)))
    
    @property
    def unit(self):
        return [self.y / self.magnitude, self.y / self.magnitude, self.z / self.magnitude]
    

class Vector2D:
    def __init__(self, vX: float, vY: float):
        self._x = vX
        self._y = vY

        self._magnitude = math.sqrt((math.pow(vX, 2), math.pow(vY, 2)))

        self.coordinates = [self.x, self.y]
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self):
        return self.coordinates[1]
    
    @property
    def magnitude(self):
        return self._magnitude
    @magnitude.setter
    def magnitude(self):
        return math.sqrt((math.pow(self.x, 2), math.pow(self.y, 2)))
    

class Matrix3D:
    def __init__(self):
        self.MatrixCoordinates = {
            {"x": 1, "y": 0, "z": 0},
            {"x": 0, "y": 1, "z": 0},
            {"x": 0, "y": 0, "z": 1}
        }
    
    def scalar_multiply():
        pass

    def matrix_multiply():
        pass

class Matrix2D:
    def __init__(self):
        self.MatrixCoordinates = {
            {"x": 1, "y": 0},
            {"x": 0, "y": 1}
        }
    
    def scalar_multiply():
        pass

    def matrix_multiply():
        pass


def round(number: float, index: int):
    pass

def dot(vector_1, vector_2):
    if type(vector_1) != type(vector_2): 
        RuntimeError("attempt to get dot product of nonequivalent types")
    
    return (vector_1.magnitude * vector_2.magnitude) / math.cos()

def cross(vector_1, vector_2):
    pass

arbitrary_vector1 = Vector3D(1, -3, 2)
arbitrary_vector2 = Vector3D(3, 2, 1)

print(arbitrary_vector1.coordinates)
arbitrary_vector1.divide(arbitrary_vector2)
print(arbitrary_vector1.coordinates)

# UNIT VECTOR

print(math.sqrt(arbitrary_vector1.unit))

# DOT PRODUCT
""""
dot_product = arbitrary_vector1.dot(arbitrary_vector2)
print(dot_product)
"""
