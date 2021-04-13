import time
inisialwhile = time.time()
k = 0
while (k<5):
    print("This is Manan While")
    k+=1
print("while loop ran in", time.time() - inisialwhile , "Seconds")

inisialfor = time.time()
for i in range(5):
    print("This is Manan For")
print("while loop ran in", time.time() - inisialwhile, "Seconds")