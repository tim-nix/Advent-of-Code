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
   values = readFile("input1b.txt")
   calibrations = list()
   for v in values:
      c = [ x for x in list(v) if x.isdigit() ]
      calibrations.append(int(c[0] + c[-1]))
      
   print(calibrations)
   print(sum(calibrations))
   
        
    
        
