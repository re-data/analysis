from lib import dbt, Report, Header, Metric

df = dbt.query("select * from {{ ref('exceptions_by_day') }} where date >= '2022-11-01'")
#df2 = dbt.query("select * from {{ ref('by_day') }}")
df2 = df

my_report = Report(name="python_report")

my_report.add(Header("My report", level=2))

my_report.plot(df, x="DATE", y="DISTINCT_USERS", title="My plot")
my_report.table(df, limit=10)

my_report.plot(df2, x="DATE", y="DISTINCT_USERS", color="LIBRARY", title="My plot 2")

# upload, host and share with others with 1 line of code
my_report.add(Metric("My metric", 100))
my_report.save_html()
#my_report.upload()

# #########

# dbt_docs = re_data.dbt.docs()
# re_data.upload(dbt_docs, notify={'slack': 'my_channel'})

# #########

# notebook = re_data.jupyter(path="notebooks/my_notebook.ipynb")
# re_data.upload(notebook)

# #########

