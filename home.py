print("\n")
for row in range(29):
    for col in range(56):
        if row==1 and (col==8 or col==35 or col==37) or row==2 and (col==7 or col==34 or col==38):
            print("*",end="")
        elif row==3 and (col==6 or col==33 or col==39) or row==4 and (col==5 or col==32 or col==40):
            print("*",end="")
        elif row==5 and (col==4 or col==31 or col==41) or row==6 and (col==3 or col==30 or col==42):
            print("*",end="")
        elif row==7 and (col==2 or col==29 or col==43) or row==8 and (col==1 or col==28 or col==44):
            print("*",end="")
        elif row==9 and (col==0 or col==27 or col==45) or row==10 and  (col==26 or col==46):
            print("*",end="")
        elif row==11 and  (col==25 or col==47) or row==12 and  (col==24 or col==48):
            print("*",end="")   
        elif row==0 and(col>8 and col<37):
            print("*",end="")
        elif row==1 and(col>8 and col<36):
            print("*",end="")
        elif row==2 and(col>7 and col<35):
            print("*",end="")    
        elif row==3 and(col>6 and col<34):
            print("*",end="")
        elif row==4 and(col>5 and col<33):
            print("*",end="")
        elif row==5 and(col>4 and col<32):
            print("*",end="")
        elif row==6 and(col>3 and col<31):
            print("*",end="")
        elif row==7 and(col>2 and col<30):
            print("*",end="")
        elif row==8 and(col>1 and col<29):
            print("*",end="")   
        elif row==9 and(col>0 and col<27):
            print("*",end="")
        elif (col==0 or col==27 or col==45) and(row>9 and row<24):
            print("*",end="")
        elif (col==8 or col==18) and(row>14 and row<20):
            print("*",end="")
        elif (col==9 and row==14) or (col==17 and row==14) or (col==10 and row==13) or (col==16 and row==13) or (row==12 and(col>11 and col<15)): 
            print("*",end="")
        elif (col>7 and col<19) and (row==20 or row==15):
            print("*",end="")
        elif (col==31 or col==41) and(row>11 and row<24):
            print("*",end="")
        elif row==11 and (col==32 or col==40) or row==10 and (col==33 or col==39) or row==9 and(col>34 and col<38):
            print("*",end="")
        elif ((row==24 ) and(col>=0 and col<51)) or ((row==25 ) and(col>=0 and col<51)) or ((row==26 ) and(col>=0 and col<51)) :
            print("*",end="")
        else:
            print(" ",end="")
    print()        





            
    

