from math import sin, cos, pi

m = 101                                     # must have an odd number of elements, be careful of indexing
fc = .14                                    # cutoff frequincy
h = []                                     

for i in range(m):
    if(i-m/2 == 0):
        h.append(2*pi*fc)

    if(i-m/2 != 0):
        h.append(sin(2*pi*fc * (i-m/2)) / (i-m/2))
        h[i] = h[i] * (0.54 - 0.46*cos(2*pi*i/m))
    
for i in range(m):                          # normalize the filter
    h[i] = h[i]/sum(h)
    
for i in range(m):                              # convert to high pass filter
    h[i] = h[i] * -1
h[int((m-1)/2)] = h[int((m-1)/2)] + 1

file = open('header.h', 'w')                
file.write("const double FILTER[" + str(m) + "] = \n")
file.write("{")

for i in range(m):
    file.write(str(h[i]))
    if(i != m-1):
        file.write(', ')
    if((i+1) % 4 == 0):
        file.write('\n')

file.write('}')

file.close()