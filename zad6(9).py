# Importowanie klasy Point3D z modułu point3d
from point3d import Point3D

# Tworzenie kilku punktów w przestrzeni trójwymiarowej
point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)
point3 = Point3D(0, 0, 0)
point4 = Point3D(-1, -2, -3)

# Obliczanie odległości między punktami
distance_1_2 = point1.distance_to(point2)
distance_1_3 = point1.distance_to(point3)
distance_1_4 = point1.distance_to(point4)

# Wyświetlanie wyników
print("Odległość między punktem 1 a punktem 2:", distance_1_2)
print("Odległość między punktem 1 a punktem 3:", distance_1_3)
print("Odległość między punktem 1 a punktem 4:", distance_1_4)