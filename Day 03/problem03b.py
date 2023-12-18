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


if __name__ == '__main__':
   lines = readFile("input3a.txt")

   ratios = []
   for y_index in range(len(lines)):
      line = lines[y_index]
      done = False
      x_index = 0
      while not done:
         # find *
         while (x_index < len(line)) and (line[x_index] != '*'):
            x_index += 1

         if x_index >= len(line):
            done = True
         else:
            numbers = []
            # look for two adjacent numbers
            # look top-left
            if ((y_index - 1) >= 0) and ((x_index - 1) >= 0):
               if lines[y_index - 1][x_index - 1].isdigit():
                  first = x_index - 1
                  last = x_index - 1
                  while ((first - 1) >= 0) and (lines[y_index - 1][first - 1].isdigit()):
                     first = first - 1
                  while ((last + 1) < len(line)) and (lines[y_index - 1][last + 1].isdigit()):
                     last = last + 1

                  numbers.append((y_index - 1, first, last))

            # look top
            if ((y_index - 1) >= 0):
               if lines[y_index - 1][x_index].isdigit():
                  first = x_index
                  last = x_index
                  while ((first - 1) >= 0) and (lines[y_index - 1][first - 1].isdigit()):
                     first = first - 1
                  while ((last + 1) < len(line)) and (lines[y_index - 1][last + 1].isdigit()):
                     last = last + 1

                  if (y_index - 1, first, last) not in numbers:
                     numbers.append((y_index - 1, first, last))

            # look top-right
            if ((y_index - 1) >= 0) and ((x_index + 1) < len(line)):
               if lines[y_index - 1][x_index + 1].isdigit():
                  first = x_index + 1
                  last = x_index + 1
                  while ((first - 1) >= 0) and (lines[y_index - 1][first - 1].isdigit()):
                     first = first - 1
                  while ((last + 1) < len(line)) and (lines[y_index - 1][last + 1].isdigit()):
                     last = last + 1

                  if (y_index - 1, first, last) not in numbers:
                     numbers.append((y_index - 1, first, last))

            # look left
            if ((x_index - 1) >= 0):
               if lines[y_index][x_index - 1].isdigit():
                  last = x_index - 1
                  first = x_index - 1
                  while ((first - 1) >= 0) and (lines[y_index][first - 1].isdigit()):
                     first = first - 1

                  if (y_index, first, last) not in numbers:
                     numbers.append((y_index, first, last))

            # look right
            if ((x_index + 1) < len(line)):
               if lines[y_index][x_index + 1].isdigit():
                  first = x_index + 1
                  last = x_index + 1
                  while ((last + 1) < len(line)) and (lines[y_index][last + 1].isdigit()):
                     last = last + 1

                  if (y_index, first, last) not in numbers:
                     numbers.append((y_index, first, last))

            # look bottom-left
            if ((y_index + 1) < len(lines)) and ((x_index - 1) >= 0):
               if lines[y_index + 1][x_index - 1].isdigit():
                  first = x_index - 1
                  last = x_index - 1
                  while ((first - 1) >= 0) and (lines[y_index + 1][first - 1].isdigit()):
                     first = first - 1
                  while ((last + 1) < len(line)) and (lines[y_index + 1][last + 1].isdigit()):
                     last = last + 1

                  numbers.append((y_index + 1, first, last))

            # look bottom
            if ((y_index + 1) < len(lines)):
               if lines[y_index + 1][x_index].isdigit():
                  first = x_index
                  last = x_index
                  while ((first - 1) >= 0) and (lines[y_index + 1][first - 1].isdigit()):
                     first = first - 1
                  while ((last + 1) < len(line)) and (lines[y_index + 1][last + 1].isdigit()):
                     last = last + 1

                  if (y_index + 1, first, last) not in numbers:
                     numbers.append((y_index + 1, first, last))

            # look bottom-right
            if ((y_index + 1) < len(lines)) and ((x_index + 1) < len(line)):
               if lines[y_index + 1][x_index + 1].isdigit():
                  first = x_index + 1
                  last = x_index + 1
                  while ((first - 1) >= 0) and (lines[y_index + 1][first - 1].isdigit()):
                     first = first - 1
                  while ((last + 1) < len(line)) and (lines[y_index + 1][last + 1].isdigit()):
                     last = last + 1

                  if (y_index + 1, first, last) not in numbers:
                     numbers.append((y_index + 1, first, last))
            
            # if found, multiply them together and add to ratios
            print(numbers)
            if len(numbers) == 2:
               y, first, last = numbers[0]
               number1 = ''
               for i in range(first, last + 1):
                  number1 += lines[y][i]
               y, first, last = numbers[1]
               number2 = ''
               for i in range(first, last + 1):
                  number2 += lines[y][i]
               ratios.append(int(number1) * int(number2))

            # continue down the line
            x_index += 1

   print(ratios)
   print('sum = ' + str(sum(ratios)))
