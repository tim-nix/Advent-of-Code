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

   return seed_vals
   

def get_map(line):
   values = line.split()
   dst = int(values[0])
   src = int(values[1])
   rng = int(values[2])

   return (src, dst, rng)


if __name__ == '__main__':
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

   print('Generating locations.')
   locations = []
   for s in seeds:
      t = s
      for m1 in map_set:
         found = False
         for m2 in m1:
            if not found and (t >= m2[0]) and (t < m2[0] + m2[2]):
               found = True
               t = m2[1] + (t - m2[0])

      locations.append(t)

   #print(locations)
   print('minimum location = ' + str(min(locations)))
