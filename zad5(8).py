import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other_point):
        """
        Dodaje współrzędne punktów
        """
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        new_z = self.z + other_point.z
        return Point3D(new_x, new_y, new_z)

    def distance_to(self, other_point):
        """
        Oblicza odległość między dwoma punktami
        """
        distance = math.sqrt((self.x - other_point.x)**2 + 
                             (self.y - other_point.y)**2 + 
                             (self.z - other_point.z)**2)
        return distance
    
    
    
    
    # Importowanie klasy Point3D z modułu point3d
from point3d import Point3D

# Tworzenie dwóch punktów
point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)

# Dodawanie punktów
result_point = point1.add(point2)
print("Wynik dodawania punktów:", result_point.x, result_point.y, result_point.z)

# Obliczanie odległości między punktami
distance = point1.distance_to(point2)
print("Odległość między punktami:", distance)