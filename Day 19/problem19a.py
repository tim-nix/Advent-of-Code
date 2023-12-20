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
   index = lines.index('')
   workflow = lines[:index]
   ratings_str = lines[index + 1:]

   workflow_dict = dict()
   for w in workflow:
      instruct = w.split('{')
      name = instruct[0]
      checks = instruct[1][:-1].split(',')
      for c_i in range(len(checks)):
         if ':' in checks[c_i]:
            compare, next_step = checks[c_i].split(':')
            var = compare[0]
            operator = compare[1]
            value = int(compare[2:])
            checks[c_i] = (var, operator, value, next_step)
      
      workflow_dict[name] = checks

   ratings = []
   for r in ratings_str:
      # chop off the surrounding curly braces and
      # split string into list by commas
      r_lst = r[1:-1].split(',')
      
      # convert it into tuple of integers
      xmas_lst = []
      for xmas in r_lst:
         xmas_lst.append(int(xmas.split('=')[1]))
      ratings.append(tuple(xmas_lst))
      
   return (workflow_dict, ratings)

      
if __name__ == '__main__':
   lines = readFile("input19b.txt")
   workflow, ratings = parseInput(lines)
   var = dict()
   sum_accepted = 0
   
   for r in ratings:
      var['x'] = r[0]
      var['m'] = r[1]
      var['a'] = r[2]
      var['s'] = r[3]

      current = 'in'
      while (current != 'A') and (current != 'R'):
         #print('current = ' + current)
         #print('workflow[current] = ' + str(workflow[current]))
         for rule in workflow[current]:
            #print('rule = ' + str(rule))
            if type(rule) == str:
               #print('nothing fit, so final case')
               current = rule
               break
            elif rule[1] == '>':
               #print('comparing ' + rule[0] + ' = ' + str(var[rule[0]]) + ' > ' + str(rule[2]))
               if var[rule[0]] > rule[2]:
                  #print('comparison passed')
                  current = rule[3]
                  break
            elif rule[1] == '<':
               #print('comparing ' + rule[0] + ' = ' + str(var[rule[0]]) + ' < ' + str(rule[2]))
               if var[rule[0]] < rule[2]:
                  #print('comparison passed')
                  current = rule[3]
                  break
               
      if current == 'A':
         sum_accepted += sum(r)
   print('sum of accepted ratings = ' + str(sum_accepted))
   
   
