from random import choice

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
   graph = dict()
   for line in lines:
      node, edges = line.split(':')
      edges = edges.lstrip().split(' ')
      if node not in graph:
         graph[node] = edges
      else:
         graph[node].extend(edges)
         
      for edge in edges:
         if edge not in graph:
            graph[edge] = [ node ]
         else:
            graph[edge].append(node)

   nodes = list(graph.keys())
   
   am = [ [ 0 for j in range(len(nodes)) ] for i in range(len(nodes)) ]
   for i in range(len(nodes)):
      for n in graph[nodes[i]]:
         j = nodes.index(n)
         am[i][j] = 1
         am[j][i] = 1

   return am


def genEdges(graph):
   edges = set()

   for i in range(len(graph) - 1):
      for j in range(i + 1, len(graph[i])):
         if graph[i][j] > 0:
            edges.add((i, j))

   return list(edges)


def findCut(graph):
   edges = genEdges(graph)
   for i in range(len(edges) - 2):
      print('testing ' + str(i) + ' of ' + str(len(edges) - 2))
      # remove edge1
      graph[edges[i][0]][edges[i][1]] = 0
      graph[edges[i][1]][edges[i][0]] = 0

      for j in range(i + 1, len(edges) - 1):
         # remove edge1
         graph[edges[j][0]][edges[j][1]] = 0
         graph[edges[j][1]][edges[j][0]] = 0

         for k in range(j + 1, len(edges)):
            # if you disconnect the wire between hfx/pzl,
            # the wire between bvb/cmg, and the wire
            # between nvd/jqt,
               
            graph[edges[k][0]][edges[k][1]] = 0
            graph[edges[k][1]][edges[k][0]] = 0
            
            # test if connected
            sizes = getComponentSizes(graph)
               
            if (len(sizes) == 2) and (1 not in sizes):
               print('component sizes = ' + str(sizes))
               print('result = ' + str(sizes[0] * sizes[1]))
               return

            # add edges back
            graph[edges[k][0]][edges[k][1]] = 1
            graph[edges[k][1]][edges[k][0]] = 1

         # add edges back
         graph[edges[j][0]][edges[j][1]] = 1
         graph[edges[j][1]][edges[j][0]] = 1

      # add edges back
      graph[edges[i][0]][edges[i][1]] = 1
      graph[edges[i][1]][edges[i][0]] = 1

   print('Nothing found.')


def getComponentSizes(graph):
   nodes = [ i for i in range(len(graph)) ]
   sizes = []
   
   while len(nodes) > 0:
      toVisit = [ nodes[0] ]
      visited = set()
      visited.add(nodes[0])
      nodes.pop(0)
      while len(toVisit) > 0:
         current = toVisit.pop(0)
         for neighbor in range(len(graph[current])):
            if (graph[current][neighbor] > 0) and (neighbor not in visited):
               toVisit.append(neighbor)
               visited.add(neighbor)
               if neighbor in nodes:
                  nodes.remove(neighbor)

      sizes.append(len(visited))

   return sizes

if __name__ == '__main__':
   # Read in the file and organize the data.
   lines = readFile("input25b.txt")

   graph = parseInput(lines)

   # Generate the graph split into two
   # components.
   graph = findCut(graph)

   
   
   
               
   

   
