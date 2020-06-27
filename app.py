#Import thư viện
from pysesame import connection

#Thiết lập kết nối, tạo đối tượng (phải có)
con = connection('http://localhost:8080/openrdf-sesame/')
con.use_repository('Course')

#Query 1 biến in ra tất cả mọi thứ thuộc về chủ đề
res=con.query_one_para('Dạng lưu đồ')
for i in res:
     print(i)

#Query 2 biến in ra chủ đề và liên kết của chủ đề 
res=con.query_two_para('Cây','Khái niệm')
for i in res:
    print(i)
