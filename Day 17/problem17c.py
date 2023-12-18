import time
import heapq

def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")
   
   return lines


def parseInput(lines):
   return [ [ int(i) for i in line] for line in lines ]


def shortestPath(block, start, stop):
   max_distance = len(block) * len(block[0]) * 10
   minheap = []
   visited = set()
   final = []

   heapq.heappush(minheap, (0, start[0], start[1], 'none', 0))

   while (len(minheap)> 0):
      # find node with smallest value that has not been visited         
      current = heapq.heappop(minheap)
      
      if (current[1], current[2], current[3], current[4]) not in visited:
         #print('current node is ' + str(current))
         x, y = current[1], current[2]
         visited.add((current[1], current[2], current[3], current[4]))
         neighbors = [ (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1) ]
         n_direction = [ 'north', 'south', 'west', 'east' ]
         if current[3] == 'north':
            neighbors.pop(1)
            n_direction.pop(1)
            if current[4] < 4:
               neighbors.pop(1)
               n_direction.pop(1)
               neighbors.pop(1)
               n_direction.pop(1)
            elif current[4] == 10:
               neighbors.pop(0)
               n_direction.pop(0)
         elif current[3] == 'south':
            neighbors.pop(0)
            n_direction.pop(0)
            if current[4] < 4:
               neighbors.pop(1)
               n_direction.pop(1)
               neighbors.pop(1)
               n_direction.pop(1)
            elif current[4] == 10:
               neighbors.pop(0)
               n_direction.pop(0)
         elif current[3] == 'east':
            neighbors.pop(2)
            n_direction.pop(2)
            if current[4] < 4:
               neighbors.pop(0)
               n_direction.pop(0)
               neighbors.pop(0)
               n_direction.pop(0)
            elif current[4] == 10:
               neighbors.pop(2)
               n_direction.pop(2)
         elif current[3] == 'west':
            neighbors.pop(3)
            n_direction.pop(3)
            if current[4] < 4:
               neighbors.pop(0)
               n_direction.pop(0)
               neighbors.pop(0)
               n_direction.pop(0)
            elif current[4] == 10:
               neighbors.pop(2)
               n_direction.pop(2)
         for n_i in range(len(neighbors)):
            n_x, n_y = neighbors[n_i]
            if (0 <= n_x < len(block)) and (0 <= n_y < len(block[0])):
               n = neighbors[n_i]
               if current[3] == n_direction[n_i]:
                  neighbor = (n[0], n[1], current[3], current[4] + 1)
               else:
                  neighbor = (n[0], n[1], n_direction[n_i], 1)

               
               if neighbor not in visited:
                  #print('checking neighbor ' + str(neighbor))
                  #print('heat sink of neighbor = ' + str(block[neighbor[0]][neighbor[1]]))
                  distance = current[0] + block[neighbor[0]][neighbor[1]]
                  #print('distance to neighbor = ' + str(distance))
                  heapq.heappush(minheap, (distance, neighbor[0], neighbor[1], neighbor[2], neighbor[3]))
                  if (neighbor[0], neighbor[1]) == stop:
                     final.append((distance, neighbor[0], neighbor[1], neighbor[2], neighbor[3]))
                        
   return final

      
if __name__ == '__main__':
   start_time = time.time()
   lines = readFile("input17b.txt")
   block = parseInput(lines)
   start = (0, 0)
   stop = (len(block) - 1, len(block[0]) - 1)
   final = shortestPath(block, start, stop)
   final.sort()
   print('final = ' + str(final[0][0]))
   print("--- %s seconds ---" % (time.time() - start_time))

   
