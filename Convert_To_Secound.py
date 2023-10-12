#Python String split() Method Syntax
#Syntax : str.split(separator, maxsplit)
#Parameters :
#separator: This is a delimiter. The string splits at this specified separator. 
    #If is not provided then any white space is a separator.
#maxsplit: It is a number, which tells us to split the string into maximum of provided number of times.
    # If it is not provided then the default is -1 that means there is no limit.
#Returns : Returns a list of strings after breaking the given string by the specified separator. from[0] to [n]


Time=input("Enter Time:\nTime Format (hh:mm:ss): ")
Time_Split=Time.split(":")
Time_To_Secounds=int(Time_Split[0])*3600+int(Time_Split[1])*60+int(Time_Split[2])
print(f"The Time You Enter = {Time_To_Secounds} Seconds.")