# To calculate slope, put in the x and y values.
x1=input("What is the first X value? ")
x2=input("What is the second X value ")
y1=input("What is the first Y value? ")
y2=input("What is the second Y value? ")
# Inputs are needed so the user can put in any numbers they want
x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)
# Variables cast into integers
mY=int(y2-y1)
mX=int(x2-x1)
m2=int(mY/mX)
if(x1<1):
  b=int(y1-(x1*m2))
elif(x1>1):
  b=int(((x1*m2)-y)*-1)
else:
  b=int(((m2*x1)-y1)*-1)
# y=mx+b
mY=str(mY)
mX=str(mX)
if(b<0):
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x " +  b )
else:
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x" + " + " + b )  
  #3=2/4x + B
  #*2
  #6=b
