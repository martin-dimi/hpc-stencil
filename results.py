import matplotlib.pyplot as plt
import numpy as np

file1 = open('results1024.txt', 'r')
file4 = open('results4096.txt', 'r')
file8 = open('results8000.txt', 'r')

file1A = open('resultsISend/result1k.txt', 'r')
file4A = open('resultsISend/result4k.txt', 'r')
file8A = open('resultsISend/result8k.txt', 'r')
test = open('test.txt', 'r')

lines1 = []
lines4 = []
lines8 = []

lines1A = []
lines4A = []
lines8A = []

testLines = []

for cnt, line in enumerate(test):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    testLines.append(number)

test.close()

for cnt, line in enumerate(file1):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    lines1.append(number)

file1.close()

for cnt, line in enumerate(file4):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    lines4.append(number)

file4.close()

for cnt, line in enumerate(file8):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    lines8.append(number)

file8.close()

# //////////////////////

for cnt, line in enumerate(file1A):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    lines1A.append(number)

file1A.close()

for cnt, line in enumerate(file4A):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    lines4A.append(number)

file4A.close()

for cnt, line in enumerate(file8A):
    lineCounter = cnt+1
    number = float(line.strip('\n'))
    lines8A.append(number)

file8A.close()

def getData(lines):
    times = []
    speedup = []
    first = -1
    for cores in range(0, 56):
        average = 0
        for line in range(0, 10):
            offset = cores * 10
            time = lines[line + offset]
            average += time
        average = average/10
        if first == -1: first = average
        times.append(average)
        speedup.append((first / average))

    return np.array(times), np.array(speedup)

times1, speedup1 = getData(lines1)
times4, speedup4 = getData(lines4)
times8, speedup8 = getData(lines8)

times1A, speedup1A = getData(lines1A)
times4A, speedup4A = getData(lines4A)
times8A, speedup8A = getData(lines8A)

for ind, time in enumerate(times8):
    rpc = 8000 // (ind+1)
    left = 8000 % (ind+1)
    print(f'Cores: {ind+1}, time: {time}, increase {speedup8[ind]}, rpc: {rpc}, left: {left}, last: {rpc + left}')


fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ind = np.arange(1, 57, 1)
x=1
ax.plot(ind, speedup1[::x])
ax.plot(ind, speedup4[::x])
ax.plot(ind, speedup8[::x])

ax.scatter(ind, speedup1[::x], label="1024", s=55)
ax.scatter(ind, speedup4[::x], label="4096", s=55)
ax.scatter(ind, speedup8[::x], label="8000", s=55)

# ax.plot(ind, speedup4A[::x])
# ax.scatter(ind, speedup4A[::x], label="ISend-Recv", s=55)


ax.axis([1, 56, 1, 25])
ax.legend(loc="upper left", prop={'size': 18})
ax.set_xlabel('Number of cores', fontsize=12)
ax.set_ylabel('Speedup x', fontsize=12)


ticks = np.arange(0,57, 10)
ticks = np.append(ticks, 56)
ticks[0] = 1
plt.grid()
plt.xticks(ticks)
ax.tick_params(axis='both', which='major', labelsize=16)
# ax.tick_params(axis='both', which='minor', labelsize=14)

plt.savefig('procs.png')

testA = []

for i in range(0, 3):
    av = 0
    for j in range(0, 10):
        av += testLines[i*10 + j]
    av = av / 10
    testA.append(av)