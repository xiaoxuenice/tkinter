import pymysql
def insert(ip,timee,argg):
  mydb = pymysql.connect(host="112.175.69.101",user="root",passwd="Pwd@123456",database="python",ssl={"ssl":""})
  a = mydb.cursor()
  try:
    argg=argg.replace('"','\\"')
    argg=argg.replace("'","\\'")
    a.execute('insert into shell(ip,time,message) values("{}","{}","{}");'.format(ip,timee,argg))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def select():
  mydb = pymysql.connect(host="112.175.69.101",user="root",passwd="Pwd@123456",database="python",ssl={"ssl":""})
  a = mydb.cursor()
  a.execute('select concat(ip,"  ",time," ",message)  from shell;')
  b=a.fetchall()
  c=[]
  for i in range(len(b)):
    c.append(b[i][0])
  return c
def delete():
  mydb = pymysql.connect(host="112.175.69.101",user="root",passwd="Pwd@123456",database="python",ssl={"ssl":""})
  a = mydb.cursor()
  try:
    a.execute("delete from shell")
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def active():
  try:
      pymysql.connect(host="112.175.69.101",user="root",passwd="Pwd@123456",database="python",ssl={"ssl":""})
      return "ok"
  except Exception as f:
      return "error"
