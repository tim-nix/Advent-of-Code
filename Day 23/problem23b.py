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


def processTrails(trails):
   new_trails = []
   for x in range(len(trails)):
      new_trails.append([])
      for y in range(len(trails[x])):
         if trails[x][y] == '#':
            new_trails[x].append('#')
         else:
            new_trails[x].append('.')

   return new_trails


# Find the longest hiking path by following the current
# path as long as it does not branch.  If the path
# branches, then recurse down each path and choose the
# longest path.
def findLongestHike(trails, current, stop, old_visited, top):
   #print()
   #print('current = ' + str(current))
   #print('shortcuts = ' + str(shortcuts))
      
   # Make a copy of the visited set to allow for
   # backtracking at higher recursion levels.
   visited = set()
   for val in old_visited:
      visited.add(val)

   # Test each possible neighbor location from the
   # current location
   deltas = [ (0, -1), (0, 1), (-1, 0), (1, 0) ]
   toVisit = [ current ]
   path = set()
   last = current
   # If there is only one path, then follow it.
   while len(toVisit) == 1:
      x, y = toVisit.pop(0)
      #print('looking at ' + str((x, y)))
      visited.add((x, y))
      path.add((x, y))
      
      if (x, y) == stop:
         #print('found the end')
         return path

      elif ((x, y) in shortcuts) and (shortcuts[(x, y)][0] not in visited):
         path_end, sc_path = shortcuts[(x, y)]
         #print('shortcut found from ' + str((x, y)) + ' to ' + str(path_end))
         toVisit.append(path_end)
         path = path.union(sc_path)

      else:
         for delta_x, delta_y in deltas:
            if ((0 <= (x + delta_x) < len(trails)) and
                (0 <= (y + delta_y) < len(trails[x]))):
               if (((x + delta_x, y + delta_y) not in visited) and
                   (trails[x + delta_x][y + delta_y] != '#')):
                  toVisit.append((x + delta_x, y + delta_y))

      if len(toVisit) == 1:
         last = (x, y)

   # If there are no more paths, then return to the
   # higher recursion level
   if len(toVisit) == 0:
      #print('dead end at ' + str((x, y)) + '; returning 0')
      return set()

   if (len(path) > 1) and (current not in shortcuts):
      #print('adding shortcut from ' + str(current) + ' to ' + str(last))
      shortcuts[current] = (last, path.copy())
      shortcuts[last] = (current, path.copy())
      
   # If there are multiple paths from the current location,
   # then follow each recursively.  Afterwards, choose the
   # longest path and return it.
   from_here = set()
   #print('toVisit = ' + str(toVisit))
   if top:
      print('at the top toVisit = ' + str(toVisit))
      
   for p in toVisit:
      if top:
         print('following path ' + str(p))
      new_path = findLongestHike(trails, p, stop, visited, False)
      if len(new_path) > len(from_here):
         from_here = new_path

   return path.union(from_here)


shortcuts = dict()

if __name__ == '__main__':
   # Read in the file and organize the data
   trails = readFile("input23b.txt")

   # Define the start and stop points
   start = (0, 1)
   stop = (len(trails) - 1, len(trails) - 2)

   #print('process trails')
   # Get rid of steep slopes
   #trails = processTrails(trails)
   
   print('find longest path')
   # Find the longest hiking path
   path = findLongestHike(trails, start, stop, set(), True)

   #print(path)
   #print('len(path) = ' + str(len(path)))

   # Print out the resulting distance
   print('distance = ' + str(len(path) - 1))
   
   
   
   
