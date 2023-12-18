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
   cards = [ 1 for i in range(len(lines)) ]
   for card in range(len(cards)):
      # Eliminate header
      card2 = lines[card].split(':')
      
      # Split into winning numbers and numbers
      card3 = card2[1].split('|')
      winning = card3[0].split()
      numbers = card3[1].split()
      
      # Turn each into a set
      win_set = set(winning)
      num_set = set(numbers)
      
      # Determine size of intersection
      matches = len(win_set.intersection(num_set))

      if matches > 0:
         for i in range(card + 1, card + matches + 1):
            if i <= len(cards):
               cards[i] += cards[card]
            else:
               print("Error: no matching card")

      print(cards)
      
   print('sum = ' + str(sum(cards)))
        
