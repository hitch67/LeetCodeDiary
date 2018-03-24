s = "PAYPALISHIRING"

nrow = 3
cell_size = (nrow-1) * 2

#for i in range((len(s)/cell_size) + 1)

output = ""

for i in range(nrow):
    step = 0
    while(step * cell_size + i < len(s)):
        output += s[step*cell_size + i]
        if  step*cell_size + i + (nrow - 1 - i) * 2 < len(s) and i != 0 and i != nrow - 1:
            output += s[step*cell_size + i + (nrow - 1 - i) * 2]
        step += 1

print output
print s
