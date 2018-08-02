import pandas as pd
import numpy as np
session = 1
temp_df = pd.DataFrame(columns=["session", "trial"])
temp_df = temp_df.set_index(["session", "trial"])
for trial in range(1, 10):
    arr = np.random.rand(3)

    for x in range(len(arr)):
        temp_df.at[(1, trial), "vote_" + "{:03}".format(x)] = arr[x] 

print(temp_df)
temp_df.loc[(1, "avg"), :] = [1,2,3]
print(temp_df)
