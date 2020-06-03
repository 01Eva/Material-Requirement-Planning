 
def mpr(x,ss,s0, lt):
    #we initialize both gross requierement array and scheduled receipts array
    gr= []
    sr= []
    #we insert our values in both gross requierement array and scheduled receipts array
    for i in range(x):
        gr.append(int(input("insert :")))
    for i in range(x):
        sr.append(int(input("insert scheduled receipts:")))
    
    oh = [0] * x
    nr = [0] * x
    por = [0] * x

    if s0 + ss + sr[0] > gr[0] :
            nr[0]=0
            oh[0]=(s0+sr[0])-gr[0]
    else :
         nr[0]=gr[0]- ( (s0-ss)+sr[0])
         oh[0]=ss

    i=1
    while i < x :
        if oh[(i-1)] + ss + sr[i] > gr[i] :
            nr[i]=0
            oh[i]=(oh[i-1]+sr[i])-gr[i]
        else : 
            nr[i]=gr[i]-((oh[i-1]-ss)+sr[i])
            oh[i]=ss
            por[i-lt]=nr[i]
            sr[i]=por[i-lt]
            
        

        i+=1
    return [gr,sr,oh,nr,por]

# we call our fonction using : number of days/months, security stock, first stock on hand, and LT as entries to our function
print(mpr(8,0,100,3))


 
