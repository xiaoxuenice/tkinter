# -*- mode: python ; coding: utf-8 -*-
import os,easygui
import paramiko

def sssh(execc,Ip):        #执行shell命令
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #连接时不提示在不在know_hosts
    if not os.path.isfile("id_rsa"):
        easygui.msgbox("没有秘钥", "提示")
        return
    try:
        private_key=paramiko.RSAKey.from_private_key_file("id_rsa")   #秘钥文件
        ssh.connect(hostname=Ip,port=22,username='root',pkey=private_key,timeout=3)    #秘钥认证
        stdin,stdout,stderr=ssh.exec_command('{}'.format(execc))
        a,b=stdout.read(),stderr.read()
        result= a if a else b
        ssh.close()
        return(result.decode())   #返回命令执行的结果
    except Exception as f:
        return("error"+Ip+str(f))

def active(Ip):           #查看连接状态
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if not os.path.isfile("id_rsa"):
        easygui.msgbox("没有秘钥", "提示")
        return
    try:
        private_key = paramiko.RSAKey.from_private_key_file("id_rsa")
        ssh.connect(hostname=Ip, port=22, username='root', pkey=private_key,timeout=3)
        ssh.get_transport().is_active()
        ssh.close()
        return (Ip+"    连接正常")
    except Exception as f:
        return (Ip+"    连接异常")
