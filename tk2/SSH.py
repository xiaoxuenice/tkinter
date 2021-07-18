# -*- mode: python ; coding: utf-8 -*-
import paramiko
#Pwd@LINUX##..
def sssh(execc,Ip):        #Pwd@LINUX##..
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=Ip, port=22, username='root', password="Pwd@LINUX##..", timeout=5)   #秘钥认证
        stdin,stdout,stderr=ssh.exec_command('{}'.format(execc))
        a,b=stdout.read(),stderr.read()
        result= a if a else b
        ssh.close()
        return(result.decode())   #返回命令执行的结果
    except Exception as f:
        return(Ip+str(f))
def active(Ip):           #查看连接状态


    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=Ip, port=22, username='root', password="Pwd@LINUX##..",timeout=5)
        ssh.get_transport().is_active()
        ssh.close()
        return ("ok")
    except Exception as f:
        return (str(f))
