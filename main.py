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
m=int(mY/mX)
if(x1<1):
  b=int(y1-(x1*m2))
  b=str(b)
  print("b ="+ " "+ b)
  b=int(b)
elif(x1>1):
  b=int(Intercept = -1 * (m) * (x2) + y2)
  b=str(b)
  print("b ="+ " "+ b)
  b=int(b)
else:
  b=int(Intercept = -1 * (m) * (x2) + y2)
  b=str(b)
  print("b ="+ " "+ b)
  b=int(b)
# y=mx+b
#B Inverter
if(b>0):
  b=int(b*-1)
  mY=str(mY)
  mX=str(mX)
elif(b<0):
  b=int(b*-1)
  mY=str(mY)
  mX=str(mX)
else:
  b=int(0)
mY=str(mY)
mX=str(mX)
if(b<0):
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x " +  b )
else:
  b=str(b)
  print("y ="+" "+mY +"/"+mX+ "x" + " + " + b )
  