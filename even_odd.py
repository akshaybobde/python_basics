
def even_odd(x):
    if(x%2==0):
         return (x , " is even number.")
    else:
        return (x," is odd number.")

x = int(input("Please enter any number :"))
y = even_odd(x)
print(y)