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
   time = lines[0].split(':')
   distance = lines[1].split(':')

   time = time[1].replace(" ", "")
   distance = distance[1].replace(" ", "")

   results = (int(time), int(distance))
   
   return results


def calcDistance(b_time, t_time):
   run_time = t_time - b_time
   distance = run_time * b_time

   return distance


if __name__ == '__main__':
   lines = readFile("input6b.txt")
   time, goal = parseInput(lines)

   wins = [ calcDistance(i, time) > goal for i in range(time) ]
   output = wins.count(True)

   print('output = ' + str(output))
   
