def sorted_coordinates(x,y,coordinates):
    d=[]
    for i in coordinates:
        dist=(i[1] - y)**2 + (i[0] - x)**2
        d.append((dist,i))
    
    d.sort()
    
    sorted_list=[]
    for i in d:
        sorted_list.append(i[1])
        
    return sorted_list
        
x=int(input("enter x coordinate of reference point:"))
y=int(input("enter y coordinate of reference point:"))

coordinates=[(0,1),(1,2),(0,3)]

print(sorted_coordinates(x,y,coordinates))