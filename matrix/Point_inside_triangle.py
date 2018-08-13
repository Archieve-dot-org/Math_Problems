#-*- coding: utf-8 -*-
"""
Check if a point is inside a triangle or not
"""
import numpy as np

tri_points = [(1,1),(2,3),(3,1)]

def pisinTri(point,tri_points,echo=False):
    Dx , Dy = point
    A,B,C = tri_points
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    M1 = np.array([ [1      , 1      , 1],
                    [Dx - Bx, Dy - By, 0],
                    [Ax - Bx, Ay - By, 0]
                     ])
    M2 = np.array([ [1      , 1      , 1],
                    [Dx - Ax, Dy - Ay, 0],
                    [Cx - Ax, Cy - Ay, 0]
		         ])
    M3 = np.array([ [1      , 1      , 1],
                    [Dx - Cx, Dy - Cy, 0],
                    [Bx - Cx, By - Cy, 0]
		         ])

    M1 = np.linalg.det(M1)
    M2 = np.linalg.det(M2)
    M3 = np.linalg.det(M3)
    #print(M1,M2,M3)

    if(M1 == 0 or M2 == 0 or M3 ==0):
        if(echo==True): print("Point: ",point," lies on the arms of Triangle")
        return True
    elif((M1 > 0 and M2 > 0 and M3 > 0) or (M1 < 0 and M2 < 0 and M3 < 0)):
        #if products is non 0 check if all of their sign is same
        if(echo==True): print("Point: ",point," lies inside the Triangle")
        return True
    else:
        if(echo==True): print("Point: ",point," lies outside the Triangle")
        return False

print("Vertices of Triangle: ",tri_points)
points = [(0,0),(1,1),(2,3),(3,1),(2,2),(4,4),(1,0),(0,4)]
for c in points:
    pisinTri(c,tri_points,echo=True)
