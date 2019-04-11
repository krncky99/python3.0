import json
Total_Accounts={
   1000:([9509234143,123456789123,98000],("kailash","kailash99")),
   1001:([6375114650,123456789456,30000],("reshma","reshma99")),
   1002:([9116367779,123456789789,40000],("komal","komal99")),
   1003:([9799066789,969696969696,45000],("chitra","chitra99")),
   1004:([8087432792,969696969695,96000],("neeta","neeta99")),
   1005:([8209953197,969696969694,15000],("yogesh","krncky99"))
        }
fp=open("hello_Accounts.json","w+")
json.dump(Total_Accounts,fp)
fp.close()
