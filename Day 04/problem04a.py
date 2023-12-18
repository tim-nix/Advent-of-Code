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
   lines = readFile("input4b.txt")
   points = []
   for line in lines:
      # Eliminate header
      card = line.split(':')
      
      # Split into winning numbers and numbers
      card2 = card[1].split('|')
      winning = card2[0].split()
      numbers = card2[1].split()
      
      # Turn each into a set
      win_set = set(winning)
      num_set = set(numbers)
      
      # Determine size of intersection
      matches = len(win_set.intersection(num_set))

      # Calculate score
      if matches > 0:
         points.append(2 ** (matches - 1))
           
   print(points)
   print('points = ' + str(sum(points)))
        
