# test if it is even number
i=8
if(i%2):
   print "odd Number"
else:
   print " Even number"

# print even number function

def even():
  eve1=int(raw_input("type an even nuber"))
  eve2=int(raw_input("and type an even nuber"))
  eve3=int(raw_input("and type an even nuber"))
  eve4=int(raw_input("and type an even nuber"))
  if (eve1 % 2==0 & eve2 % 2==0 & eve3 % 2==0 & eve4 % 2 ==0):
      add= eve1 + eve2 + eve3 +eve4
      print add
  else:
      print " odd number"   

# call function  
even()
