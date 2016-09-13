import sys
print("Length of sys.argv list: ", len(sys.argv))
print("sys.argv[0]: ", sys.argv[0])
print("Listing of sys.argv: ", sys.argv)
for i in range(1,len(sys.argv)):
    print(sys.argv[i])

