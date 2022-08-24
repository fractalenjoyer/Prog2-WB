import time
print((lambda x: f"{int(x//60+2):02}:{int(x%60):02}")(((10**100)%(24*60) + time.time()/60)%(24*60)))