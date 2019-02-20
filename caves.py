import random, time

def countNeighbors(theMap, row, col):
  count = 0
  for y in [row-1, row, row+1]:
    for x in [col-1, col, col+1]:
      if theMap[y][x]:
        count += 1
  return count

def addBorders(theMap, rows, cols):
  for row in rows:
    for col in [0, len(cols)-1]:
      theMap[row][col] = True
  for col in cols:
    for row in [0, len(rows)-1]:
      theMap[row][col] = True


rows = range(75)
cols = range(100)
delay = .1


caveMap = [[random.randint(1, 100) < 48 for col in cols]
    for row in rows]
addBorders(caveMap, rows, cols)

iteration = 0
while True:
    iteration += 1
    changed = False


    nextMap = [[False for col in cols] for row in rows]
    addBorders(nextMap, rows, cols)


    for row in rows[1:len(rows)-1]:
        for col in cols[1:len(cols)-1]:
          count = countNeighbors(caveMap, row, col)
          # Modify the current cell
          if caveMap[row][col] == True and count >= 4:
            nextMap[row][col] = True
          if caveMap[row][col] == False and count >= 5:
            nextMap[row][col] = True
            changed = True


    caveMap = nextMap

    if not changed:
        break
