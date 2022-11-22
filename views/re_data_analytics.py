from lib import dbt, Report, Header, Metric, Attachment
import pandas as pd

#df = dbt.query("select * from {{ ref('exceptions_by_day') }} where date >= '2022-11-01'")
#df2 = dbt.query("select * from {{ ref('by_day') }} where date >= '2022-11-01'")

#df.to_csv('df1.csv')
#df2.to_csv('df2.csv')
df = pd.read_csv('df1.csv')
df2 = pd.read_csv('df2.csv')

my_report = Report(name="python_report")

my_report.add(Header("My report", level=1))

my_report.plot(df, x="DATE", y="DISTINCT_USERS", title="My plot")
my_report.table(df, limit=10)

my_report.plot(df2, x="DATE", y="DISTINCT_USERS", dimension="LIBRARY", title="My plot 2")

my_report.add(Attachment("df1.csv"))

# upload, host and share with others with 1 line of code
my_report.add(Metric("My metric", 100))
my_report.generate()

# my_report.upload()

# #########

# dbt_docs = re_data.dbt.docs()
# re_data.upload(dbt_docs, notify={'slack': 'my_channel'})

# dbt_docs = dbt.docs()
# dbt_docs.generate()
# dbt_docs.upload()

# #########

# notebook = re_data.jupyter(path="notebooks/my_notebook.ipynb")
# re_data.upload(notebook)

# #########

