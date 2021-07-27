def SwapFileData():
     swap1 = input("Enter 1st file name to Swap:-  ")
     swap2 = input("Enter 2nd file name to Swap:-  ")
     
     with open(swap1, 'r') as a:
         read_a = a.read()
     
     with open(swap2, 'r') as b:
         read_b = b.read()

     with open(swap1, 'w') as a:
         a.write(read_b)

     with open(swap2, 'w') as b:
         b.write(read_a)


SwapFileData()
