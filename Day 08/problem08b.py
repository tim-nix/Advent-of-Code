from math import gcd

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
   desert_map = {}
   steps = list(lines[0])
   for index in range(2, len(lines)):
      direction = lines[index].split('=')
      start = direction[0].strip()
      choices = direction[1].split(',')
      left = choices[0][2:]
      right = choices[1][1:4]

      desert_map[start] = (left, right)

   return (steps, desert_map)


def genStart(locations):
   start = []
   for loc in locations:
      #print(loc)
      if loc[2] == 'A':
        start.append(loc)

   return start


if __name__ == '__main__':
   lines = readFile("input8b.txt")
   steps, desert_map = parseInput(lines)
   print(len(desert_map))

   locations = genStart(desert_map.keys())
   print(locations)
   cycles = []
   for location in locations:
      num_steps = 0
      done = False
      loc = location
      while not done:
         for step in steps:
            if step == 'L':
               loc = desert_map[loc][0]
            elif step == 'R':
               loc = desert_map[loc][1]
            else:
               print('Error: unknown step: ' + step)
            num_steps += 1
            if loc[2] == 'Z':
               print('found the end in ' + str(num_steps) + ' steps.')
               cycles.append(num_steps)
               done = True
               break

   print('cycles = ' + str(cycles))
   lcm = 1
   for i in cycles:
      lcm = lcm * i // gcd(lcm, i)

   print('number of steps = ' + str(lcm))
