X, Y, N = list(map(int, input().split()))
#input
data = input()

#split data and turn into integer
intdata = [int(i) for i in data.split(" ")]

#dictionary
##create
dict = {'key':'values'}
##update
dict.update({'key':'value'})
##access
dict['keys']
dict['keys'][0:1]

mylist =[]
#list
#get unique value in list
myset = set(mylist)
#sorted set
myset_sorted = sorted(set(mylist))

#Recursive example
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1) #recursion here
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#list to string ' '
" ".join(str(e) for e in list)

#======Common Mistakes====
#1. Programming before done read_string1
#2. Need to parse the meaning question, dont get bagged down in the excessive verbosity
#3. READ -> PARSE IN NOTES AS COMMAND -> USE PSEUDO CODE
#4. Not all input must be used






