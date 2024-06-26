if comp==you:
    return None
 elif comp=="S":
   if you =="g":
      return True
   if you=="w":
      return False
 
 elif comp=="w":
   if you=="s":
      return True
   if you=="g":
      return False

 elif comp=="g":
    if you=="w":
       return True
if you=="s":
    return False

  result-game (comp, you)

 print("comp choosed = ", comp)
 print("you choosed = ",you)

 # results declaration

 if result==None:
 print ("Game is a tie") I            
  
 elif result:
      print("You win !!")

else:
   print("You loose")


#Khushal Sharma