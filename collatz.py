lengths=[]
def collatz(i): # generate longest collatz sequence
    global lengths
    if i not in lengths:
        if i%2==0:
            lengths[i]=collatz(i/2)+1
        else:
            lengths[i]=collatz((3*i+1)/2)+2
    return lengths[i]
def longest_collatz(n):
    largest_collatz_number=1
    longest_sequence=1
    global lengths
    lengths={1:1}
    for i in range(2,n):
        if collatz(i)>longest_sequence:
            largest_collatz_number=i
            longest_sequence=collatz(i)
    return largest_collatz_number,longest_sequence

print(longest_collatz(200))