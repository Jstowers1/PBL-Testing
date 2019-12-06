# To calculate slope, put in the x and y values.
#User inputs
x1=input("What is the first X value? ")
x2=input("What is the second X value ")
y1=input("What is the first Y value? ")
y2=input("What is the second Y value? ")
# Inputs are needed so the user can put in any numbers they want
#String to integer translation
x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)
# Variables cast into integers.
#Calculations
if(y1<0):
  mY=int((y2+y1))
  mX=int((x2+x1))
elif(x1<0):
  mY=int((y2-y1))
  mX=int((x2+x1))
elif(y1<0 & x1<0):
  mY=int((y2-y1))
  mX=int((x2-x1))
else:
  mY=int((y2-y1))
  mX=int((x2-x1))

m=float(mY/mX)

print(m)

if(x1<1) :
  b=int((x1*m)+y1)
  m=str(m)
elif(x1>1) :
  b=int((x1*m)- y1)
  m=str(m)
else: 
  b=int(y1-m)
  m=str(m)
# y=mx+b

mY=str(mY)
mX=str(mX)

if(b<0):
  b=str(b)
  print("y ="+" "+ mY + "/"+ mX +"x " + b)
else:
  b=str(b)
  print("y ="+" "+ mY + "/"+ mX +"x" + " + " + b )  