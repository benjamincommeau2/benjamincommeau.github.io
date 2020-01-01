import sys
import string
import numpy as np
#filename=sys.argv[1]
mycharacters=[l for l in string.printable]
xbad=mycharacters[99]
del mycharacters[99]
del mycharacters[98]
del mycharacters[97]
del mycharacters[95]
print((mycharacters))
fo=open(sys.argv[1])
filecharacters=[c for c in fo.read()]
#filecharacters.append(xbad)
fo.close()
diff=np.setdiff1d(np.array(filecharacters),np.array(mycharacters),assume_unique=True).tolist()
print(diff)
for i in range(len(filecharacters)):
  if(filecharacters[i]=='\t'):
    filecharacters[i]=' ';
diff=np.setdiff1d(np.array(filecharacters),np.array(mycharacters),assume_unique=True).tolist()
print(diff)
filestring=''.join(filecharacters)
filewrite=open('new_'+sys.argv[1],'w')
filewrite.write(filestring)
filewrite.close()
