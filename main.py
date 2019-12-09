# To calculate slope, put in the x and y values.
x1=int(input("What is the first X value? "))
x2=int(input("What is the second X value "))
y1=int(input("What is the first Y value? "))
y2=int(input("What is the second Y value? "))
# Inputs are needed so the user can put in any numbers they want
mY=int(y2-y1)
mX=int(x2-x1)
m=int(mY/mX)
b=int(m*(-1)*x1+y1)
print(b)
# y=mx+b
#B Inverter
#if(b>0):
  #b=int(b*1)
  #mY=str(mY)
  #mX=str(mX)
#elif(b<0):
  #b=int(b*-1)
  #mY=str(mY)
  #mX=str(mX)
#else:
  #b=int(0)
#mY=str(mY)
#mX=str(mX)
#if(b<0):
# b=str(b)
#print("y ="+" "+mY +"/"+mX+ "x " +  b )
#else:
 # b=str(b)
  #print("y ="+" "+mY +"/"+mX+ "x" + " + " + b )