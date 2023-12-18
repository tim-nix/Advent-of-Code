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


def get_seeds(line):
   seeds = line.split(':')
   seeds = seeds[1].split()
   seed_vals = [ int(seed) for seed in seeds ]
   seed_pairs = []
   for i in range(0, len(seed_vals), 2):
      seed_pairs.append((seed_vals[i], seed_vals[i + 1]))
      

   return seed_pairs
   

def get_map(line):
   values = line.split()
   dst = int(values[0])
   src = int(values[1])
   rng = int(values[2])

   return (src, dst, rng)


if __name__ == '__main__':
   lower_bound = 0
   upper_bound = 100000000000
   
   lines = readFile("input5b.txt")
   seeds = get_seeds(lines[0])

   print('Generating mappings.')
   map_set = []
   mapping = []
   for i in range(1, len(lines)):
      line = lines[i]
      if line == '':
         if len(mapping) > 0:
            map_set.append(mapping)
      elif 'map' in line:
         mapping = []
      else:
         mapping.append(get_map(line))

   map_set.append(mapping)

   seed_ranges = [ (s, s + r) for s, r in seeds ]
   #print(seed_ranges)

   print('Converting map.')
   # convert map_set format and merge maps
   locations = []
   for m1 in map_set:
      start  = [ (lower_bound, upper_bound, 0) ]
      for m2 in m1:
         # convert (initial, mapped, range) to (lower, upper, offset)
         lower = m2[0]
         upper = m2[0] + m2[2] - 1
         offset = m2[1] - lower

         #print('inserting ' + str(m2))

         new_locations = []
         # check for overlaps
         for minimum, maximum, shift in start:
            #print('parsing ' + str((minimum, maximum, shift)))
            if (lower <= minimum) and (upper >= maximum):
               new_locations.append((minimum, maximum, shift + offset))
            elif (lower == minimum) and (upper < maximum):
               new_locations.append((minimum, upper, shift + offset))
               new_locations.append((upper + 1, maximum, shift))
            elif (lower > minimum) and (lower < maximum) and (upper >= maximum):
               new_locations.append((minimum, lower - 1, shift))
               new_locations.append((lower, maximum, shift + offset))
            elif (lower > minimum) and (upper < maximum):
               new_locations.append((minimum, lower - 1, shift))
               new_locations.append((lower, upper, shift + offset))
               new_locations.append((upper + 1, maximum, shift))
            elif (lower < minimum) and (upper >= minimum) and (upper < maximum):
               new_locations.append((minimum, upper, shift + offset))
               new_locations.append((upper + 1, maximum, shift))
            elif (upper < minimum) or (lower > maximum):
               new_locations.append((minimum, maximum, shift))
            elif (lower == maximum):
               new_locations.append((minimum, maximum - 1, shift))
               new_locations.append((maximum, maximum, shift + offset))
            elif (upper == minimum):
               new_locations.append((minimum, minimum, shift + offset))
               new_locations.append((minimum + 1, maximum, shift))
            else:
               print('found unresolved case')
               print('m2 = ' + str(m2))
               print('location = ' + str((minimum, maximum, shift)))
               print('lower = ' + str(lower) + ' and upper = ' + str(upper))
               print('minimum = ' + str(minimum) + ' and maximum = ' + str(maximum))

         start = new_locations
      locations.append(start)
      #print(locations)
      #print()

   print('Mapping seeds.')
   final = []
   round_num = 1
   for min_seed, max_seed in seed_ranges:
      print('Calculating round ' + str(round_num) + ' of ' + str(len(seed_ranges)) + ' rounds.')
      round_num += 1
      for i in range(min_seed, max_seed):
         loc = i
         #print('seed = ' + str(loc))
         for mapping in locations:
            for lower, upper, shift in mapping:
               #print((lower, upper, shift))
               if (loc >= lower) and (loc <= upper):
                  #print('bounding found')
                  loc = loc + shift
                  #print('new value = ' + str(loc))
                  break
            
         final.append(loc)
      print('smallest so far = ' + str(min(final)))

   #print(final)
   print(min(final))
         
               
