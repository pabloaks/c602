import random
import matplotlib.pyplot as plt

num_pts = 1000

xs = list()
ys = list()
xb = list()
yb = list()

cc = 0
pis = list()
for i in range(1,num_pts+1):
    x = (random.random()-0.5)*2
    y = (random.random()-0.5)*2
    if x**2 + y**2 <= 1:
        xs.append(x)
        ys.append(y)
        cc += 1
    else:
        xb.append(x)
        yb.append(y)
    pis.append(cc/i*4)
    
plt.scatter(xs,ys,alpha=0.1,c='red')
plt.scatter(xb,yb,alpha=0.1,c='grey')
plt.show()
print(cc/num_pts*4)
plt.plot(pis)
plt.show()
