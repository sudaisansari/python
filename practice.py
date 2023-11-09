import re
import pandas as pd


chat = """
piaic232
piaic434
piaic567
piaic789
piaic890
piaic123
piaic456
piaic678
piaic901
piaic234
piaic567
piaic789
piaic234
piaic567
piaic890
piaic123
piaic456
piaic678
piaic901
piaic345
asdweeersd
sedf4r4tg4
sddtefy45gvr
34tgf4rgre4
4tg45regt4fcr
4gt4tyt4fe
"""


pattern = """(.*)(\d{3})"""  # \d{2} means number and {2} its lentgh  . means all character except \n * means when do not know lentgh

rows : list[str] = re.findall(pattern, chat)

rows


df = pd.DataFrame(rows, columns=("Institute", "RollNo"))
print(df)

# did above on colab too\