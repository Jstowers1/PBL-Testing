# To calculate slope, put in the x and y values.
x1=int(input("What is the first X value? "))
x2=int(input("What is the second X value "))
y1=int(input("What is the first Y value? "))
y2=int(input("What is the second Y value? "))
# Inputs are needed so the user can put in any numbers they want
m=int(y2-y1)/(x2-x1)
mY=(y2-y1)
mX=(x2-x1)
mY=str(mY)
mX=str(mX)
b=int(-1*(m)*(x2)+y2)
if(b<0):
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x " +  b)
else:
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x" + " + " + b)