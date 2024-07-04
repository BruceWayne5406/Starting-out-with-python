import matplotlib.pyplot as plt

#constructing a line chart

x1=[1,2,3,4] #creating points (1,5),(2,6),(3,7),(4,8) on the graph
y1=[5,6,7,8]

x2=[5,6,7,8]# creating points (5,9),(6,10),(7,11),(8,12) on the graph
y2=[9,10,11,12]

plt.plot(x1,y1,label="line1",color="black",linestyle="dashed",linewidth=3,marker="o",markerfacecolor="red")
plt.plot(x2,y2,label="line2")

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("my graph")
plt.legend() #indicates which line has which color


#now constructing a bar chart

left=[1,2,3,4,5]
height=[10,11,23,36,4]

tick_label=["one","two","three","four","five"]
plt.bar(left,height,tick_label=tick_label,width=0.8,color=["blue","orange"])
plt.xlabel("X axis")
plt.ylabel("Y axis")


plt.show()