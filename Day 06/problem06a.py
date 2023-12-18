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
   times = lines[0].split(':')
   distances = lines[1].split(':')

   times = times[1].split()
   distances = distances[1].split()

   results = [ (int(times[i]), int(distances[i])) for i in range(len(times)) ]

   return results


def calcDistance(b_time, t_time):
   run_time = t_time - b_time
   distance = run_time * b_time

   return distance


if __name__ == '__main__':
   lines = readFile("input6b.txt")
   results = parseInput(lines)

   output = 1
   for time, goal in results:
      wins = [ calcDistance(i, time) > goal for i in range(time) ]
      output *= wins.count(True)

   print('output = ' + str(output))
   
