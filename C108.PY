import random
import plotly.express as px
import plotly.figure_factory as ff
count=[]
dice_result =[]


#to role the number 100 times
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    t= dice1+dice2
    #push the result in the list
    dice_result.append(t)
    count.append(i)
#fig=px.bar(x=dice_result, y=count)
#to creat a normal distrebution curve bell curve
fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.show()
print(count)
print(dice_result)