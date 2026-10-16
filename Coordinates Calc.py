import math
print("Coordinate Calculator")

#define functions to calculate the Magnitude, Distance,Unit vector,Midpoint 

#define a function to calculate the midpoint between two points 

def midpoint(point1,point2):
    return(
    (point1[0] + point2[0])/2,
    +(point1[1] + point2[1])/2 ,+ (point1[2]+ point2[2])/2
    )
    
#define a function that calculate the Magnitude of a point 

def magnitude(point):
    x ,y, z = point
    return(
    math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
    )

#define a function to calculate the distance between two points 
def distance(point1,point2):
    return(
    math.sqrt(( point2[0] - point1[0])**2 +
    (point2[1] - point1[1])**2 +
    (point2[2] - point1[2])**2
    )
    )
# define a function to find the unit vector of a point
def unit_vector(point):
    mag = magnitude(point)
    if mag == 0 :
        return None
    return (
    point[0]/mag,
    point[1]/mag,
    point[2]/mag
    )
    
    

# Create input field to collect values of the coordinate

 #create input field to collect values of the first point
 
 
print(" Enter the coordinates for point 1") 
x = float(input("Enter X1: "))
y = float(input("Enter Y1: "))
z = float(input("Enter Z1: "))
point1 = [x,y,z]

# create input field to collect values of the second point 
print(" Enter the coordinates of point 2")
x2 = float(input("Enter X2: "))
y2 = float(input("Enter Y2: "))
z2 = float(input("Enter Z2: "))
point2 = [x2,y2,z2]

# Create an input field for users to select type of operation they want to do 

print("Select an operation")
print("""
M - Midpoint between the  points 
D - Distance between the points 
A- Magnitude of a point 
U- Unit vector of a point 
C - Cancel
""")

operation_type = input("Enter your choice: ").strip() .lower()
print("")
# create an if/else statement to contain varying choice of users 

if operation_type == "m" :
    print(f"The Midpoint is: " , midpoint(point1,point2))
elif operation_type == "d" :
    print(f"The Distance is: ", distance(point1,point2))
elif operation_type == "a" :
   print('''Select the point you want to find the Magnitude
    A for point 1 
    B for point 2
   ''')
   
   option = input("Select either A or B: ").lower()
   if option == "a" :
           print("The magnitude of Point 1: " , magnitude(point1))
   elif option == "b" :
       print ("The Magnitude of point 2: " , magnitude(point2))
   else :
        print("Invalid option ")
        
elif operation_type == "u" :
     print("""Select the point you want to find the unit vector of 
     A for point 1
    B for point 2"""
     )
     option2 = input("Select either A or B: ").lower()
     if option2 == "a":
       print("The Unit vector:" ,unit_vector(point1))
     elif option2 == "b":
       print("The Unit vector:" ,unit_vector(point2))
     else :
      print("Invalid option")

elif operation_type == "c":
       print(" Program closed")

else :
    print("Invalid operation type")


   
   
   
   
   
   