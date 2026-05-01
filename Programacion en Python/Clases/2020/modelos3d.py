def row(self, x0, y0, z0, w, h, d):
    x, y, z = x0, y0, z0
    X, Y, Z = x + w, y + h, z + d
    cubes = []
    for n in range(3):
        cube = [x, y, z, X, Y, Z]
        cubes.append(cube)
        z, Z = z + d, Z + d
    return cubes

def divide(self, bbox, depth):
        if depth == 0:
            self.retainedCubes.append(bbox)
            return []
        x0, y0, z0, x1, y1, z1 = bbox
        w = float(x1 - x0) / 3
        h = float(y1 - y0) / 3
        d = float(z1 - z0) / 3

        x, y, z = x0, y0, z0
        cubes = []
        for layer in range(3):
            x = x0
            for rows in range(3):
                cubes.extend(self.row(x, y, z, w, h, d))
                x = x + w
            y = y + h
        cubes = self.delete(cubes)
        # Recursion________________
        for cube in cubes:
            self.divide(cube, depth - 1)
        return cubes