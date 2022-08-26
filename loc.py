class loc_reader:
    
    def read(self,code):
        lines = code.splitlines()
        loc = 0
    
        multicmnt = False
        for line in lines:
            first = True
            haschar = False
            shouldcnt = True
            counted = False
            index = 0
            while index < len(line):
                index+=1
                if line[index-1] != " ":
                    if line[index-1] == "#":
                        break
                    elif line[index-1] == "'":
                        if len(line) > index+1:
                            if line[index] == "'" and line[index+1] == "'":
                                multicmnt = not multicmnt
                                index +=2
                            elif not counted and not multicmnt and first:
                                loc +=1
                                counted = True
                    elif not counted and not multicmnt and first:
                        loc +=1
                        counted = True
                        
                    first = False
        return loc