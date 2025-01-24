import os
from meshesfera import quad

base_dir = "output"

def get_path(filename):
    return os.path.join(base_dir, filename)

def vquad():
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

def write_obj(vertices, faces, uvtex ,filename, mtlfile ="sphere.mtl"):
    with open(get_path(filename), "w" ) as meshfile:
        meshfile.write(f"mtllib {mtlfile}\n")
        for v in vertices:
            meshfile.write(f"v {v[0]} {v[1]} {v[2]}\n")
            for (u, v) in uvtex:
                meshfile.write(f"vt {u} {v}\n")
        meshfile.write("usemtl material_1\n")
        for(a,b,c) in faces:
            meshfile.write(f"f {a} {b} {c}\n")


if __name__ == "__main__":
    v, f, uv = quad()
    write_obj(v, f,uv, "terraplana.obj")