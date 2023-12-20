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


def checkRanges(ranges):
   for i in range(0, len(ranges) - 1, 2):
      if ranges[i + 1] < ranges[i]:
         return False

   return True

   
def findRanges(ranges, current, workflow):
   #print('current = ' + current)
   #print('ranges = ' + str(ranges))

   if current == 'A':
      combos = 1
      for i in range(0, len(ranges) - 1, 2):
         combos *= ranges[i + 1] - ranges[i] + 1
      return combos

   elif current == 'R':
      return 0

   to_add = 0
   total = 0
   for rule in workflow[current]:
      #print('rule = ' + str(rule))
      if type(rule) == str:
         #print('recursive call')
         to_add = findRanges(ranges, rule, workflow)

      elif rule[1] == '>':
         #print('comparator >')
         if rule[0] == 'x':
            good_ranges = (rule[2] + 1, ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7]) 
            bad_ranges = (ranges[0], rule[2], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'm':
            good_ranges = (ranges[0], ranges[1], rule[2] + 1, ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], rule[2], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'a':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], rule[2] + 1, ranges[5], ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], rule[2], ranges[6], ranges[7])
         elif rule[0] == 's':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], rule[2] + 1, ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], rule[2])

         if checkRanges(good_ranges):
            #print('recursive call')
            to_add = findRanges(good_ranges, rule[3], workflow)

      elif rule[1] == '<':
         #print('comparator <')
         if rule[0] == 'x':
            good_ranges = (ranges[0], rule[2] - 1, ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
            bad_ranges = (rule[2], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'm':
            good_ranges = (ranges[0], ranges[1], ranges[2], rule[2] - 1, ranges[4], ranges[5], ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], rule[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'a':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], rule[2] - 1, ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], rule[2], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 's':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], rule[2] - 1)
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], rule[2], ranges[7])

         if checkRanges(good_ranges):
            #print('recursive call')
            to_add = findRanges(good_ranges, rule[3], workflow)

      if checkRanges(bad_ranges):
         ranges = bad_ranges
      else:
         break

      #print('to_add = ' + str(to_add))
      total += to_add

   return total


if __name__ == '__main__':
   lines = readFile("input19b.txt")
   workflow, ratings = parseInput(lines)
   ranges = (1, 4000, 1, 4000, 1, 4000, 1, 4000)
   accepted = findRanges(ranges, 'in', workflow)
   print('accepted = ' + str(accepted))
   
   
