import scipy.stats as stats



sum = 0
for i in range(3,31):
    for j in range(1,31):
        sum += stats.poisson.pmf(j, 0.2)**i
sum2 = 0
for i in range(1,31):
    for j in range(3,31):
        sum2 += stats.poisson.pmf(j,0.2)**i
print(sum2)
