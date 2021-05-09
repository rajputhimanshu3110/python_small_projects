low_limit = int(input("Enter Low limit: "))
max_limit = int(input("Enter Max limit: "))
p_c =0
prime = 0

for i in  range(low_limit,max_limit,1):
    for j in range(2,i,1):
        prime = 0
        if i%j == 0:
            prime += 1
            p_c +=1
            break
    if prime == 0 and i != 1:
        print(i)
    j=2
print()
print(f"There are total {max_limit-p_c-low_limit} prime numbers")