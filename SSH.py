# -*- mode: python ; coding: utf-8 -*-
import os,easygui
from scp import SCPClient
import paramiko

def sssh(execc,Ip):        #执行shell命令
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #连接时不提示在不在know_hosts
    if not os.path.isfile("id_rsa"):
        easygui.msgbox("没有秘钥", "提示")
        cccccccc
    try:
        private_key=paramiko.RSAKey.from_private_key_file("id_rsa")   #秘钥文件
        ssh.connect(hostname=Ip,port=22,username='root',pkey=private_key)    #秘钥认证
        stdin,stdout,stderr=ssh.exec_command('{}'.format(execc))
        a,b=stdout.read(),stderr.read() 		  
        result= a if a else b
        ssh.close()
        return(result.decode())   #返回命令执行的结果
    except Exception as f:
        return(Ip+"     连接异常")

def active(Ip):           #查看连接状态
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if not os.path.isfile("id_rsa"):
        easygui.msgbox("没有秘钥", "提示")
        cccccccc
    try:
        private_key = paramiko.RSAKey.from_private_key_file("id_rsa")
        ssh.connect(hostname=Ip, port=22, username='root', pkey=private_key)
        ssh.get_transport().is_active()
        ssh.close()
        return (Ip+"    连接正常")
    except Exception as f:
        return (Ip+"    连接异常")

def SCP(Ip):          #上传文件
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if not os.path.isfile("id_rsa"):
        easygui.msgbox("没有秘钥", "提示")
        cccccccc
    private_key = paramiko.RSAKey.from_private_key_file("id_rsa")
    ssh.connect(hostname=Ip, port=22, username='root', pkey=private_key)
    scp = SCPClient(ssh.get_transport(), socket_timeout=15.0)
    if not os.path.isfile("zhengshu.zip"):
        easygui.msgbox("没有zhengshu.zip压缩文件", "提示")
        cccccccc
    scp.put('zhengshu.zip', "/mnt/")
    easygui.msgbox("文件上传完成!","提示")
    ssh.close()