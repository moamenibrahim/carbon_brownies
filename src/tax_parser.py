
import pandas as pd
import rossum

extracted = rossum.document('invoice.pdf')
# max score only:
df = pd.DataFrame.from_dict(extracted['fields'])
idx = df.groupby('name')['score'].idxmax()
print(df.iloc[idx][['name', 'value']].to_string(index=False))
