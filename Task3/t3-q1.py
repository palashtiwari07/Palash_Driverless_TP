def sorted_coordinates(x,y,coordinates):
    d=[]
    for i in coordinates:
        dist=(i[1] - y)**2 + (i[0] - x)**2
        d.append((dist,i))

    d.sort

    return sorted(d.items())
        
x=int(input("enter x coodrinate of reference point:"))
y=int(input("enter y coordinate of reference point:"))

coordinates=[(0,1),(1,2),(0,3)]

print(sorted_coordinates(x,y,coordinates))