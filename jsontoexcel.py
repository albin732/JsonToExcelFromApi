import requests
import tablib
import json


class jsonexcel:

    def convert():
        request_url = 'https://5f717a7064a3720016e60748.mockapi.io/students/students'
        data = requests.get(request_url)
        json_string = json.dumps(json.loads(data.text))
#         print(json_string)

        ds = tablib.Dataset()
        ds.json = json_string
#         print(ds)
        with open('jsontoexcel.xlsx', 'wb') as f:
            f.write(ds.export('xlsx'))

    convert()
