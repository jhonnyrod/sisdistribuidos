#!/usr/bin/env python
import web
import json
from collections import Counter

urls = (
    '/index/', 'index'
)

class index:
    def POST(self):
        # How to obtain the name key and then print the value?
        web.header('Content-Type', 'application/json')
        data = web.data()
        my_json = data.decode('utf8').replace("'", '"')
        res=json.loads(my_json)
        print(Counter(res["direccion1"]))
        if (res["direccion1"].isalnum() and res["direccion2"].isalnum() and (len(res["direccion1"]) == 64) and (len(res["direccion2"]) == 64)):
            comp=True
        else:
            comp=False
        resp= json.dumps({"direccion1":res["direccion1"], "direccion2": res["direccion2"],"monto":res["monto"], "comprobador":comp})      
        return resp

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()