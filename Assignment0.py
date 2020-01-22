import linecache
import math
# open sequence1 file
CH01 = open('CH01.fa')
readCH01 = CH01.read();


# get rid of the first line in the file
retrieved_line = linecache.getline('CH01.fa', 1)
len_of_first = len(retrieved_line)
sequence1 = readCH01[len_of_first:]

# output the length of sequence1
len_of_sequence1 = len(sequence1)
print("length of sequence1 is:", len_of_sequence1)

#open sequence2 file
CH02 = open('CH02.fa')
readCH02 = CH02.read()


#get rid of the second line in the file
retrieved_line=linecache.getline('CH02.fa',1)
len_of_first=len(retrieved_line)
sequence2=readCH02[len_of_first:]
len_of_sequence2=len(sequence2)
print("length of sequence2 is:",len_of_sequence2)

#set t value
t=3
print("t value is:",t)
CH01.close()
CH02.close()

#write the cleared sequence to an output file
outputFile=open("output.txt","w")
outputFile.write(sequence1)
outputFile.close()

#get rid of the endline in the output.txt file
newList=[]
with open('output.txt') as f:
    for line in f:
        line=line.rstrip()
        newList.append(line)

#combining the nucleotide segements into a continuing sequence
combination="".join(newList)
list = []
count=0
start=0
numIteration=0
stop=len_of_sequence2
numOfString=len_of_sequence1/len_of_sequence2
isWholeNum=False
#calculate the number of times sequence1 can be divided by
#the length of sequence2
if(numOfString%len_of_sequence2==0):
    isWholeNum=True
if isWholeNum:
    numIteration=numOfString
else:
    numIteration=int(numOfString)+1

#slicing the continuing sequence based on the length of sequence2
for x in range(numIteration):
    slice_object=slice(start, stop)
    start+=len_of_sequence2
    stop+=len_of_sequence2
    list.append(combination[slice_object])


probability=(len_of_sequence2/len_of_sequence1)*t
#expected probability
print("expected probability",probability)
#observe frequency
print("observe frequency",list.count(sequence2))






