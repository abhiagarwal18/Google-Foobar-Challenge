

def shortest(shortx, shorty, maze):
    width = len(maze[0])
    height = len(maze)
    matrix = [[None for i in range(width)] for i in range(height)]
    matrix[shortx][shorty] = 1

    array = [(shortx, shorty)]
    while array:
        x, y = array.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          nextx, nexty = x + i[0], y + i[1]
          if 0 <= nextx < height and 0 <= nexty < width:
            if matrix[nextx][nexty] is None:
                matrix[nextx][nexty] = matrix[x][y] + 1
                if maze[nextx][nexty] == 1 :
                  continue
                array.append((nextx, nexty)) 
                  
    return matrix

def solution(maze):
  width = len(maze[0])
  height = len(maze)
  x1 = shortest(0, 0, maze)
  x2 = shortest(height-1, width-1, maze)
  matrix = []

  value = 2 ** 32-1
  for i in range(height):
      for j in range(width):
          if x1[i][j] and x2[i][j]:
              value = min(x1[i][j] + x2[i][j] - 1, value)
  return value
