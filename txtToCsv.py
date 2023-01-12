import pandas as pd

read_file = pd.read_csv(r' <<YOUR TXT PATH ORIGIN>>)
read_file.to_csv(r' <<>YOUR CSV PATH DESTINY>', index=None)
