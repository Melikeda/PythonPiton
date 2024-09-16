import math

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (3, 5), (8, 1)]

# Öklid Mesafesi İçin Fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonucu Yazdırma
print(f"Noktalar arasındaki minimum Öklid mesafesi: {min_distance:.2f}")









