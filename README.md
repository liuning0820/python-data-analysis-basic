
# Python Data Analysis Learning Path

```sh
pip install -r .\requirements.txt
```

## Pandas

```py
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Save ndarray to disk
arr = np.arange(10)
np.save('saved_npy_array',arr)
arr2= np.load('saved_npy_array.npy')

# Read csv using pandas
result = pd.read_csv('examples/ex6.csv')

# Draw 2D chart
import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.arange(10))

# Plot with pandas

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()



```

### Example: USDA Food Composition Databases

Executes below script in ipython terminal

```py
import numpy as np
import pandas as pd
import json
db = json.load(open('datasets/usda_food/database.json'))
len(db)
db[0]
db[0].keys()
db[0]['nutrients']
db[0]['nutrients'][:7]
type(db[0]['nutrients'])

from pandas import DataFrame
nutrients = DataFrame(db[0]['nutrients'])
nutrients[0:7]
# value_counts 查看营养类别的分布情况
pd.value_counts(nutrients.group)

# 汇总所有营养数据做分析
nutrients = []
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id']= rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)
nutrients = nutrients.drop_duplicates()
```

## 数据可视化：Matplotlib

[Matplotlib](https://github.com/matplotlib/matplotlib) is a Python 2D plotting library which produces publication quality figures 
in a variety of formats and interactive environments across platforms.

## 数据可视化: Echarts

```shell script
pip install pyecharts
```





