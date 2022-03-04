
from .reader import Reader
from .table import Table

class Page:
  def __init__(self, reader: Reader) -> None:
    self.reader: Reader = reader

  def __generate_one_toc(self, table: Table):
    return \
f"""
<li><a href="#{table.table_id}">{table.table_name}</a></li>
"""


  def generate(self):
    html_string = \
f"""
<div class="gb-c-callout-accessibility gb-u-spacing-double">
	<h2 id="toc">
		On this page: 
	</h2>
	<ul class="page-toc">
"""
    for table in self.reader.tables:
      html_string += self.__generate_one_toc(table)

    html_string += \
"""
	</ul>
</div>

"""
    for table in self.reader.tables:
      html_string += table.html_string()
    
    return html_string