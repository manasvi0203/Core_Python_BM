import matplotlib.pyplot as plt

'''x = [i for i in range(100)]
y = [i for i in range(100)]
x_2 = [i for i in range(100)]
y_2 = [i+2 for i in range(100)]
plt.xlabel("X -->")
plt.ylabel("Y -->")
plt.plot(x,y)
plt.plot(x_2,y_2)
plt.title("X=Y")
plt.legend(["x=y","x+2=y"])
plt.show()'''

x = [1,3,4,2,4,5,100,3]
y = [i for i in range(len(x))]
plt.xlim([0,10])
plt.ylim([0,20])
plt.scatter(x,y, marker="*",color="y")

plt.show()

