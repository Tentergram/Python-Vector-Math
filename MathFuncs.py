from __future__ import annotations
import math

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
            
            return Vector3D(*new_multiplied_coordinates)
        elif type(multiplier) == Vector3D: # vectors
            return Vector3D(*[self.x * multiplier.x, self.y * multiplier.y, self.z * multiplier.z])
        else:
            RuntimeError("invalid multiplier, got: " + str(type(multiplier)))


    def divide(self, divisor: int | float | Vector3D):
        if type(divisor) == float or type(divisor) == int: # scalars
            new_divided_coordinates = []
            
            for CoordIndex in range(0, 3):
                new_divided_coordinates.append(self.coordinates[CoordIndex] / divisor)

            return Vector3D(*new_divided_coordinates)
        elif type(divisor) == Vector3D: # vectors
            return Vector3D(*[self.x / divisor.x, self.y / divisor.y, self.z / divisor.z])
        else:
            RuntimeError("invalid divisor type, got: " + str(type(divisor)))
    
    def add(self, vector: Vector3D):
        added_coordinates = []

        for coord in range(len(self.coordinates)):
            added_coordinates.append(self.coordinates[coord] + vector.coordinates[coord])
        
        return Vector3D(*added_coordinates)

    def subtract(self, vector: Vector3D):
        subtracted_coordinates = []

        for coord in range(len(self.coordinates)):
            subtracted_coordinates.append(self.coordinates[coord] - vector.coordinates[coord])
       
        return Vector3D(*subtracted_coordinates)
    
    def dot(self, vector: Vector3D):
        return (self.x * vector.x) + (self.y * vector.y) + (self.z * vector.z)

    def cross(self, vector: Vector3D):
        return Vector3D(
            (self.y * vector.z) - (self.z * vector.y),
            (self.z * vector.x) - (self.x * vector.z),
            (self.x * vector.y) - (self.y * vector.x)
        )

    def lerp(self, vector: Vector3D, alpha: int | float):
        return self.add((vector.subtract(self)).multiply(alpha))

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
        return Vector3D(
            self.x / self.magnitude, 
            self.y / self.magnitude, 
            self.z / self.magnitude
        )
    

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

# VECTORS
inputed_vectors = {
    "vectorA": None,
    "vectorB": None
}

for vector_name, _3D_vector in inputed_vectors.items():
    # while True:
    new_vector_input = input("input the coordinates for " + vector_name + ": ")
    new_vector_list = new_vector_input.split()

    for vector_index in range(len(new_vector_list)):
        vector_value = new_vector_list[vector_index]

        try:
            if vector_value.find(".") != -1:
                new_vector_list[vector_index] = float(vector_value)
            else:
                new_vector_list[vector_index] = int(vector_value)
        except:
            print("Coordinate is not a number")
        
        inputed_vectors[vector_name] = new_vector_list

        if vector_index == 2 and vector_name == "vectorB":
            break

arbitrary_vectorA = Vector3D(
    inputed_vectors["vectorA"][0],
    inputed_vectors["vectorA"][1],
    inputed_vectors["vectorA"][2]
)

arbitrary_vectorB = Vector3D(
    inputed_vectors["vectorB"][0],
    inputed_vectors["vectorB"][1],
    inputed_vectors["vectorB"][2]
)

'''
Vector A: <-2, 3 0>
Vector B: <1, 4, 2>
'''

# UNIT VECTORS
arbitrary_vectorA_unit = arbitrary_vectorA.unit
arbitrary_vectorB_unit = arbitrary_vectorB.unit

# LENGTHS
print("LENGTH OF A: " + str(arbitrary_vectorA.magnitude) + " - COORDINATES " + str(arbitrary_vectorA.coordinates))
print("LENGTH OF B: " + str(arbitrary_vectorA.magnitude) + " - COORDINATES " + str(arbitrary_vectorB.coordinates))
print("LENGTH OF UNIT A: " + str(arbitrary_vectorA_unit.magnitude) + " - COORDINATES " + str(arbitrary_vectorA_unit.coordinates))
print("LENGTH OF UNIT B: " + str(arbitrary_vectorA_unit.magnitude) + " - COORDINATES " + str(arbitrary_vectorB_unit.coordinates))

# DOT PRODUCT
dot_product = arbitrary_vectorA.dot(arbitrary_vectorB)
unit_dot_product = arbitrary_vectorA_unit.dot(arbitrary_vectorB_unit)
print("DOT PRODUCT OF A AND B: " + str(dot_product))
print("UNIT DOT PRODUCT OF A AND B: " + str(unit_dot_product))

#CROSS PRODUCT

print("CROSS PRODUCT OF A AND B: " + str(arbitrary_vectorA.cross(arbitrary_vectorB).coordinates))

#LERP
print("VECTOR OF A TO B AT 25%: " + str(arbitrary_vectorA.lerp(arbitrary_vectorB, .25).coordinates))
print("VECTOR OF A TO B AT 50%: " + str(arbitrary_vectorA.lerp(arbitrary_vectorB, .5).coordinates))
