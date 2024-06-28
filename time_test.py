# import time module
import time

#import dataframe modules
import polars as pl
import pandas as pd

# store iteration start timestamp
start = time.time()

#selecting with only requred rows and going foreward with the operation
df_panads = pd.read_csv("C:/Users/Saurav/Desktop/data/test.csv", 
                        delimiter= ',' , usecols=['Col1', 'Co2', 'col3'], chunksize=300)
# store iteration end timestamp
end = time.time()
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      round((end-start) * 10**3), "ms")
#The time of execution of above program is : 0.001 ms

# store iteration start timestamp
start = time.time()

df_polar = pl.read_csv("C:/Users/Saurav/Desktop/data/test.csv")

# store iteration end timestamp
end = time.time()
    
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      round((end-start) * 10**3), "ms")

#The time of execution of above program is : 3 ms

# store iteration start timestamp
start = time.time()
df_polar_batched = pl.read_csv_batched("C:/Users/Saurav/Desktop/data/test.csv")
# store iteration end timestamp
end = time.time()
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      round((end-start) * 10**3), "ms")

#The time of execution of above program is : 1 ms
