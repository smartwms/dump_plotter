# Python program emulating positioning systems
import numpy
import math

p_a = [1, 1]
print("Beacon A location: ", p_a)

p_b = [3, 2]
print("Beacon B location: ", p_b)

p_c = [2, 3]
print("Beacon C location: ", p_c)

d_a = int(input("Input RSSI in dbm from A point: "))
d_b = int(input("Input RSSI in dbm from B point: "))
d_c = int(input("Input RSSI in dbm from C point: "))

ref_power = -45
attenuation_factor = 4
## estimated_distance =  pow(10.0, ((rssi - (A))/-(10 * n)));
## A = -45dbm -> experimental value of reference point power 1m distance
## n = 4 -> experimental value attenuation factor of envirnment
## 2m = -57dbm
## 3m = -64dbm 

d_a = pow(10.0, ((d_a - ref_power)/(-10 * attenuation_factor)))
d_b = pow(10.0, ((d_b - ref_power)/(-10 * attenuation_factor)))
d_c = pow(10.0, ((d_c - ref_power)/(-10 * attenuation_factor)))

print("Distance in m from Beacon A: ", d_a)
print("Distance in m from Beacon B: ", d_b)
print("Distance in m from Beacon C: ", d_c)

theta_a = int(input("Input AoA in degrees from A Beacon: "))
theta_b = int(input("Input AoA in degrees from B Beacon: "))

##Start calculations

##RSSI
matrix_1 = numpy.array([[2 * (p_a[0] - p_c[0]) , 2 * (p_a[1] - p_c[1])], [2 * (p_b[0] - p_c[0]) , 2 * (p_b[1] - p_c[1])]])
matrix_2 = numpy.array([[p_a[0] ** 2 - p_c[0] ** 2 + p_a[1] ** 2 - p_c[1] ** 2 + d_c ** 2 - d_a ** 2], 
                [p_b[0] ** 2 - p_c[0] ** 2 + p_b[1] ** 2 - p_c[1] ** 2 + d_c ** 2 - d_b ** 2]])

matrix_1 = numpy.linalg.inv(matrix_1)                

p_d = numpy.dot(matrix_1,matrix_2)

##Results
print("")
print ("Coordinate of D point using only RSSI : ", numpy.transpose(p_d))
print ("")

#AoA
p_d[0] = (p_b[1] - p_a[1] + p_a[0] * math.tan(math.radians(theta_a)) - p_b[0] * math.tan(math.radians(theta_b))) / (math.tan(math.radians(theta_a)) -  math.tan(math.radians(theta_b)))
p_d[1] = ((p_b[1]/math.tan(math.radians(theta_b))) - (p_a[1]/math.tan(math.radians(theta_a))) + p_a[0] - p_b[0]) / ((1 / math.tan(math.radians(theta_a))) - (1 / math.tan(math.radians(theta_b))))

#Results
print("")
print ("Coordinate of D point using only AoA : ", numpy.transpose(p_d))
print ("")