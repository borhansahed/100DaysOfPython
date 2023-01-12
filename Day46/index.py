import os


# if(not os.path.exists("data")):
#  os.mkdir("data")

# make unlimited file helpWith python 
# for i in range(0,100):
#  os.mkdir(f"data/Day{i+1}")

# rename file helpWith python

for i in range(0,100):
 os.rename(f"data/s{i+1}", f"data/Tutorial{i+1}")