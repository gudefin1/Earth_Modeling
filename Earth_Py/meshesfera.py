def quad():
    vertices = [
        (1, 1, 0), (-1 , 1, 0),(-1, -1, 0), (1, -1 ,0)
    ]


    faces = [
        (1,2,3),(3,4,1)
    ]
    
    uvtextures= [
        (1.0, 0.0),(0.0, 0.0),(0.0 , 1.0),(1.0 , 1.0)
    ]

    return vertices, faces ,uvtextures

def spere():
    return