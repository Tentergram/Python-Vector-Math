from __future__ import annotations
import math

def lerp(start, goal, alpha: float):
    if type(start) != type(goal):
        RuntimeError("start and goal are nonequivalent types")
    else:
        pass

class Vector3D:
    def __init__(self, vX: float, vY: float, vZ: float):
        self._x = vX
        self._y = vY
        self._z = vZ

        self._magnitude = math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)))

        self.coordinates = [self.x, self.y, self.z]
    
    def multiply(self, multiplier: float | int | Vector3D):
        if type(multiplier) == float or type(multiplier) == int: # scalars
            for CoordIndex in range(0, 3):
                self.coordinates[CoordIndex] *= multiplier
        elif type(multiplier) == Vector3D: # vectors
            self.coordinates = [self.x * multiplier.x, self.y * multiplier.y, self.z * multiplier.z]
        else:
            RuntimeError("invalid multiplier, got: " + str(type(multiplier)))


    def divide(self, divisor: int | float | Vector3D):
        if type(divisor) == 'float' or type(divisor) == 'int': # scalars
            for CoordIndex in range(0, 3):
                self.coordinates[CoordIndex] /= divisor
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
        pass

    def cross(self, vector: Vector3D):
        pass

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self.coordinates[2]

    @property
    def magnitude(self):
        return math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)))
    

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
            "Roll": {"x": 1, "y": 0, "z": 0},
            "Pitch": {"x": 0, "y": 1, "z": 0},
            "Yaw": {"x": 0, "y": 0, "z": 1}
        }
    
    def scalar_multiply():
        pass

    def matrix_multiply():
        pass

class Matrix2D:
    def __init__(self):
        self.MatrixCoordinates = {
            "AxisX": {"x": 1, "y": 0},
            "AxisY": {"x": 0, "y": 1}
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

print(arbitrary_vector1.magnitude)
arbitrary_vector1.multiply(2)
print(arbitrary_vector1.magnitude)
