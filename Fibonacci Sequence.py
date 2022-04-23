#Program to display the Fibonacci sequence up to the n-th term 
nterms=int(input("Enter the number of terms"))


#the first two terms
n1, n2=0, 1
count=0


#check if the number of terms is valid 
if nterms<=0:
    print("Please enter a positive interger")


#if there is only one term, return n1
elif nterms==1:
    print("Fibonacci Sequence upto", nterms,":" )
    print(n1)


    #generate Fibonacci sequence
else:
        print("Fibonacci sequence:")
        while count<nterms:
            print(n1)
            nth=n1 + n2


            #update th evalues
            n1 = n2
            n2 = nth
            count+=1
        