def solution(wallpaper):
    answer = []
    minx, maxx, miny, maxy = 51, 0, 51,0
    
    row = len(wallpaper)
    col = len(wallpaper[0])

    for x in range(row):
        for y in range(col):
            if wallpaper[x][y] == "#":
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)


    return [minx, miny, maxx+1, maxy+1]