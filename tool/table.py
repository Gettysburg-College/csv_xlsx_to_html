from typing import List, Dict

class Table:
  def __init__(self, table_name: str, table_id: str, rows: List[Dict[str, str]]) -> None:
    self.table_name: str = table_name
    self.table_id: str = table_id
    self.rows: List[Dict[str, str]] = rows

  def __generate_one_row(self, student: Dict[str, str]):
    return \
f"""
<tr>
  <th data-label="Last Name" scope="row">{student["Last Name"]}</th>
  <td data-label="First Name">{student["First Name"]}</td>
</tr>
"""

  def html_string(self):
    html_string = \
f"""
<h2 id="{self.table_id}">
	{self.table_name}
</h2>
<table class="dcf-table dcf-table-responsive dcf-table-bordered dcf-table-striped dcf-w-100%">
  <thead>
		<tr>
			<th data-label="Last Name" scope="col">Last Name</th>
			<th data-label="First Name" scope="col">First Name</th>
		</tr>
	</thead>
  <tbody>
"""
    for student in self.rows:
      html_string += self.__generate_one_row(student)
    
    html_string += \
"""
  </tbody>
</table>

"""
    return html_string
    
  