import mysql.connector,time
def insert(ip,timee,argg):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
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
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  a.execute('select concat(ip,"  ",time," ",message)  from shell;')
  b=a.fetchall()
  c=[]
  for i in range(len(b)):
    c.append(b[i][0])
  return c
def delete():
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  try:
    a.execute("delete from shell")
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def I_already(timee):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  try:
    a.execute('insert into already(time) values("{}");'.format(timee))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def S_already():
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  a.execute("select time  from already;")
  return (a.fetchall())
def active():
  try:
      mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
      return "ok"
  except Exception as f:
      return "error"