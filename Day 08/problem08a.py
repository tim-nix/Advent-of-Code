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
      


if __name__ == '__main__':
   lines = readFile("input8b.txt")
   steps, desert_map = parseInput(lines)
   print(len(desert_map))

   location = 'AAA'
   num_steps = 0
   while location != 'ZZZ':
      for step in steps:
         #print('current location = ' + location)
         #print('step = ' + step)
         #print('map[' + location + '] = ' + str(desert_map[location]))
         #print()
         if step == 'L':
            location = desert_map[location][0]
         elif step == 'R':
            location = desert_map[location][1]
         else:
            print('Error: unknown step: ' + step)
         num_steps += 1
         print('steps so far = ' + str(num_steps))
         if location == 'ZZZ':
            print('found the end')
            break

   print('number of steps = ' + str(num_steps))
