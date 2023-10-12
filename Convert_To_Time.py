
Time=int(input("Enter Time In Seconds:"))
Time_H=int(Time/3600)
Time_M=int((Time-Time_H*3600)/60)
Time_S=Time-(Time_H*3600)-(Time_M*60)

print(f"The Time You Enter Is(hh:mm:ss)= {Time_H}:{Time_M}:{Time_S}")
