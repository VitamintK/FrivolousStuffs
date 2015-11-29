import random
samples = 25
toss_per_sample = 20

x_bars = []
for i in range(samples):
    toss_total = 0
    for j in range(toss_per_sample):
        toss_total += random.randint(1,6)
    x_bars.append(toss_total/toss_per_sample)

print(*sorted(x_bars), sep='\n')
print('Average of all x_bars is ', sum(x_bars)/samples)
