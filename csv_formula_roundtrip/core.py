import json,math
from .common import number,integer,identifier
import csv,io
def dangerous(s):return s.lstrip(' \ufeff').startswith(('=','+','-','@','\t','\r','\n'))
def run(d):
 rows=d['rows']
 if not isinstance(rows,list)or len(rows)>5000 or any(not isinstance(r,list)or len(r)>100 for r in rows):raise ValueError('rows')
 safe=[];changes=[]
 for i,row in enumerate(rows):
  r=[]
  for j,value in enumerate(row):
   if not isinstance(value,str)or len(value)>10000:raise ValueError('cell')
   risk=dangerous(value);r.append("'"+value if risk else value)
   if risk:changes.append(dict(row=i,column=j,reason='formula_like_prefix'))
  safe.append(r)
 stream=io.StringIO(newline='');csv.writer(stream).writerows(safe);encoded=stream.getvalue();decoded=list(csv.reader(io.StringIO(encoded,newline='')))
 return dict(csv=encoded,roundtrip_matches=decoded==safe,changed_cells=changes,original_preserved_in_input=True,mitigation='leading_apostrophe_for_formula_like_text')
