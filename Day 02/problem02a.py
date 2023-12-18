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

def parseInput(values):
   results = []
   for v in values:
      # First, get rid of the game header
      p1 = v.split(':')
      # Next, break up the game into each 'showing'
      p2 = p1[1].split(';')
      game = []
      for p3 in p2:
         p4 = p3.split(',')
         showings = []
         for p5 in p4:
            p6 = p5.strip()
            p7 = p6.split(' ')
            game.append((int(p7[0]), p7[1]))
            
      results.append(game)

   return results

if __name__ == '__main__':
   values = readFile("input2b.txt")
   games = parseInput(values)

   maxStones = { "red":12, "green":13, "blue":14 }
   valids = []
   for g in games:
      valid = True
      for number, color in g:
         #print('color: ' + color + ' and number = ' + str(number))
         if number > maxStones[color]:
            valid = False

      valids.append(valid)
         
   sum = 0
   for v in range(len(valids)):
      if valids[v]:
         sum += v + 1

   print('sum = ' + str(sum))
   
        
    
        
