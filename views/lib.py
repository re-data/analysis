import os
import pandas as pd
import altair as alt
import io
from bs4 import BeautifulSoup
import random
import string
from pathlib import Path

def random_str(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

class dbt(object):

    @staticmethod
    def write_macro(sql):
        """Write a dbt macro to the macros folder"""

        temp_macro_path = '../macros/temp_macros'
        Path(temp_macro_path).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(temp_macro_path, "temp.sql"), "w") as f:
            f.write(r"""
            {% macro temp_macro_export() %}
                {% set query %}
            """ + sql + r"""
                {% endset %}
                {% set result = run_query(query) %}
                {% do result.to_json('temp_macros_result.json') %}
            {% endmacro %}
            """)

    @staticmethod
    def query(sql):
        dbt.write_macro(sql)
        os.system("dbt run-operation temp_macro_export")
        df = pd.read_json("../temp_macros_result.json")
        return df


class Element(object):
    def head(self):
        return None

    def render(self):
        pass

class Header(Element):
    def __init__(self, text, level=1):
        self.text = text
        self.level = level

    def render(self):
        return f"""
        <h{self.level} class='re_header'>{self.text}</h{self.level}>
        """

class Table(Element):
    def __init__(self, df, fields=None, header=True, limit=50):
        self.df = df
        self.fields = fields
        self.header = header
        self.limit = limit

    def render(self):
        if self.fields:
            df = self.df[self.fields]
        else:
            df = self.df

        if self.limit:
            df = df.head(self.limit)

        html = df.to_html(index=False, header=self.header)

        return f"<div class='re_table'>{html}</div>"

class Plot(Element):
    def __init__(self, df, x=None, y=None, color=None, kind="line", title=None, **kwargs):
        self.df = df
        self.x = x
        self.y = y
        self.color = color
        self.kind = kind
        self.title = title
        self.kwargs = kwargs
        self.chart = self.chart_html()


    def chart_html(self):
        chart = alt.Chart(self.df).mark_line()
        
        if not self.color:
            chart = chart.encode(
                x=self.x,
                y=self.y,
            )
        else:
            chart = chart.encode(
                x=self.x,
                y=self.y,
                column=self.color
            )

        chart_file = io.StringIO("")
        chart.save(chart_file, format="html")
        content = chart_file.getvalue()
        return content

    def head(self):
        soup = BeautifulSoup(self.chart, 'html.parser')
        head = ''.join([str(x) for x in soup.head()])
        return head

    def render(self):
        soup = BeautifulSoup(self.chart, 'html.parser')
        body = soup.body

        random_id = "chart" + random_str(N=15)

        str_div = str(body.find('div'))
        str_div = str_div.replace('vis', random_id)

        script = str(body.find('script'))
        script = script.replace('"#vis"', f'"#{random_id}"')
        script = script.replace("getElementById(\'vis\')", f"getElementById(\'{random_id}\')")
        return str_div + script
        

class Text(Element):
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<div>{self.text}</div>"


class Report(object):
    def __init__(self, name) -> None:
        self.name = name
        self.elements = []

    def write(self, text):
        self.elements.append(Text(text))

    def add(self, element):
        self.elements.append(element)

    def table(self, df, *args, **kwargs):
        self.elements.append(Table(df, *args, **kwargs))

    def plot(self, df, *args, **kwargs):
        self.elements.append(Plot(df, *args, **kwargs))

    def render(self):

        head = ""
        for elements in self.elements:
            if elements.head():
                head += elements.head()

        body = ""

        for element in self.elements:
            body += element.render()

        return "<html><head>{}</head><body>{}</body></html>".format(head, body)

    def save_html(self, file_name="index.html"):
        with open(file_name, "w") as f:
            f.write(self.render())

    def upload(self):
        with open("index.html", "w") as f:
            f.write(self.render())
            os.system(f"re_cloud upload custom --file index.html --name {self.name}")

