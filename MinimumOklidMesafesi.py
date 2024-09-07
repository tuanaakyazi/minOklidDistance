

def euclideanDistance (tuple1, tuple2):
    a, b = tuple1
    c, d = tuple2
    distance = ((a-c)**2 + (b-d)**2)**0.5  
    return distance



points = [(4,6), (8,2), (5,9), (9,8)]
distances = []

for i in range(len(points)-1):
    for j in range(i+1, len(points)) :
        conclusion = euclideanDistance(points[i], points[j])
        print(conclusion)
        distances.append(conclusion)
        
smallest = distances[0]
for i in range(1, len(distances)):
    if distances[i]< smallest:
        smallest = distances[i]
        
print(" The smallest distance is ", smallest)
 


