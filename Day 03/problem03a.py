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
   lines = readFile("input3b.txt")

   foundNumbers = []
   for index in range(len(lines)):
      line = lines[index]
      done = False
      first = 0
      last = 0
      while not done:
         # find first digit
         while (first < len(line)) and (not line[first].isdigit()):
            first += 1
            
         if first >= len(line):
            done = True
         else:
            # find last digit
            last = first
            while (last < len(line)) and (line[last].isdigit()):
               last += 1
               
            # look all around for symbol
            nearSymbol = False
            for i in range(index - 1, index + 2):
               for j in range(first - 1, last + 1):
                  if (i >= 0) and (i < len(lines)) and (j >= 0) and (j < len(line)):
                     if (not lines[i][j].isdigit()) and (lines[i][j] != '.'):
                        nearSymbol = True

            # if symbol found, pull out number and add to list
            if nearSymbol:
               number = ''
               for i in range(first, last):
                  number += line[i]
               foundNumbers.append(int(number))
               
            # continue until end of line is reached
            first = last + 1

   print(foundNumbers)
   print('sum = ' + str(sum(foundNumbers)))

   
   
        
    
        
