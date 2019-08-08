class CSVLabelPlugin:
   def input(self, filename):
      f = open(filename, 'r')
      self.params = dict()
      for line in f:
         stuff = line.split('\t')
         self.params[stuff[0]] = stuff[1].strip()


   def run(self):
      g = open(self.params['inputfile'], 'r')
      self.contents = ""
      pos = 0
      for line in g:
         if (pos == 0):
            line = "\"\"," + line
         else: 
            line = self.params['label'] + str(pos) + "," + line
         self.contents += line
         pos += 1

   def output(self, filename):
      g = open(filename, 'w')
      g.write(self.contents)
