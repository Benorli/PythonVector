class Vector(object):
    """ Stores the values of a vector as a tuple. Methods calculate associated values such as direction and magnitude
    and store them as properties."""
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)


        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        if isinstance(other, (Vector, list, tuple)):
            if isinstance(other, Vector):
                if len(self.coordinates) == len(other.coordinates):
                    combined = zip(self.coordinates, other.coordinates)
                    return tuple([x + y for x, y in combined])
                else:
                    raise ValueError('Vectors must have equal dimensions to be added')
            else:
                if len(self.coordinates) == len(other):
                    combined = zip(self.coordinates, other)
                    return tuple([x + y for x, y in combined])
                else:
                    raise ValueError('Vectors must have equal dimensions to be added')
        else:
            raise TypeError('Vectors may only be added to Vectors, lists or tuples')

    def __sub__(self, other):
        if isinstance(other, (Vector, list, tuple)):
            if isinstance(other, Vector):
                if len(self.coordinates) == len(other.coordinates):
                    combined = zip(self.coordinates, other.coordinates)
                    return tuple([x - y for x, y in combined])
                else:
                    raise ValueError('Vectors must have equal dimensions to be subtracted')
            else:
                if len(self.coordinates) == len(other):
                    combined = zip(self.coordinates, other)
                    return tuple([x - y for x, y in combined])
                else:
                    raise ValueError('Vectors must have equal dimensions to be subtracted')
        else:
            raise TypeError('Vectors may only be subtracted from Vectors, lists or tuples')

    def scalar_multiply(self, scalar):
        if isinstance(scalar, (int, float, complex)):
            return tuple(map(lambda x: x*scalar, self.coordinates))
        else:
            raise TypeError('Scalar numeric data type required')

    def get_magnitude(self):
        self.magnitude = sum(map(lambda x: x**2, self.coordinates))**0.5
        return self.magnitude

    def normalize(self):
        if hasattr(self, "magnitude"):
            self.unit = tuple(map(lambda x: x/self.magnitude, self.coordinates))
            return self.unit
        else:
            self.magnitude = sum(map(lambda x: x**2, self.coordinates))**0.5
            self.unit = tuple(map(lambda x: x/self.magnitude, self.coordinates))
            return self.unit
