import mo_sql_parsing as msp
import queries
import json

file = open("/home/aman/programs/gitrepos/learning/python3/sql_parsing/sql_to_json.json", 'w')
all_jsons = []
for sql in queries.queries:
    json_str = msp.parse(sql)
    all_jsons.append(json_str)

json.dump(all_jsons,file, indent=1)
file.close()  # close the file