# -*- mode: python ; coding: utf-8 -*-
import ssh,re,easygui
def shell(exec,Ip):
    return ssh.sssh(exec,Ip)
def active(Ip):
    return ssh.active(Ip)
def Scp(Ip):
    return ssh.SCP(Ip)
def Exec_shell(Ip):
    b=ssh.sssh("sh /zhengshu/jieya.sh",Ip)
    if easygui.ccbox("脚本执行结果,请确认是否有误\t\t\n{}".format(b),"执行脚本"):
        pass
    else:
        ccccccc

def Cat_conf(Ip):
    b=ssh.sssh("ls /shangchuan/ |grep key |head -n20",Ip)
    x=b.strip()
    easygui.msgbox(x+"\t\t\t\t\t","第一次确认 域名+.key")
    b=ssh.sssh("ls /shangchuan/ |grep crt |head -n20",Ip)
    x=b.strip()
    easygui.msgbox(x+"\t\t\t\t\t","第二次确认 域名+.crt")
    b=ssh.sssh('ls /shangchuan/ |grep conf',Ip)
    x=b.strip()
    easygui.msgbox(x+"\t\t\t\t\t","第三次确认 域名+.conf")
    nn=1
    for i in x.split("\n"):
        ff=ssh.sssh("cat /shangchuan/{} |head -n22".format(i),Ip)
        easygui.msgbox(ff ,"第{}次确认  配置文件  {}".format(nn,i))
        nn+=1
def   Restart(Ip):
    ssh.sssh("cp /shangchuan/*.crt /shangchuan/*.key /usr/local/nginx/conf/ ; cp /shangchuan/*.conf /usr/local/nginx/kis/",Ip)
    b=ssh.sssh("/usr/local/nginx/sbin/nginx -t",Ip)
    if easygui.ccbox(b,"配置文件是否 ok"):
        ssh.sssh("/usr/local/nginx/sbin/nginx -s reload",Ip)
    else:
        easygui.msgbox("重新执行脚本","错误")
        ssh.sssh("for i in `ls /shangchuan|grep 'crt\|key'`;do rm -f /usr/local/nginx/conf/$i;done ;for i in `ls /shangchuan|grep conf `;do rm -f /usr/local/nginx/kis/$i;done ",Ip)
def Exec_sed(ml,ym,Ip):
    ml=ml.strip()
    ym=ym.strip()
    if re.findall('http',ym):
        pass
    else:
        easygui.msgbox("被修改的域名必须添加http或https","修改域名错误")
        cccccc
    ymm=ssh.sssh('ls /usr/share/nginx/html/',Ip)
    ymmm=ymm.split("\n")
    if ml in ymmm:
        pass
    else:

        easygui.msgbox("{}".format(ymm),"再次确定修改的网站站点  为以下文件夹！")
        cccccc
    pdml="[ -f /usr/share/nginx/html/{}/a.txt  ] ; echo $?".format(ml)
    pd=ssh.sssh(pdml,Ip)
    pd=pd.strip()
    if  str(pd) == "0":
        pass
    else:
        easygui.msgbox("{}   /usr/share/nginx/html/{}/a.txt\n\n\n没有这个文件，无法获取域名!!!".format(Ip,ml), "错误提示")
        cccccc

    one=ssh.sssh("cat /usr/share/nginx/html/{}/a.txt".format(ml),Ip)
    one=one.strip()
    if easygui.ccbox("{}\n\n之前的域名: {}\n修改为域名: {}".format(ml,one,ym), "修改确定"):
        pass
    else:
        cccccc
    exec_s='find /usr/share/nginx/html/{}/ -type f |xargs  sed -i  "s#{}#{}#g" '.format(ml,one,ym)
    ssh.sssh(exec_s, Ip)
    cnmd=ssh.sssh("cat /usr/share/nginx/html/{}/a.txt".format(ml),Ip)
    easygui.msgbox("{} 下新域名为\n\n{}".format(ml,cnmd),"修改结束")
    return exec_s
