# -*- mode: python ; coding: utf-8 -*-
import SSH,re,easygui
def shell(exec,Ip):
    return SSH.sssh(exec,Ip)
def active(Ip):
    return SSH.active(Ip)
def Scp(Ip):
    return SSH.SCP(Ip)
def Exec_shell(Ip):
    b=SSH.sssh("sh /zhengshu/jieya.sh",Ip)
    if easygui.ccbox("脚本执行结果,请确认是否有误\t\t\n{}".format(b),"执行脚本"):
        pass
    else:
        ccccccc
def Cat_conf(Ip):
    b=SSH.sssh("ls /shangchuan/ |grep key |head -n20",Ip)
    x=b.strip()
    easygui.msgbox(x+"\t\t\t\t\t","第一次确认 域名+.key")
    b=SSH.sssh("ls /shangchuan/ |grep crt |head -n20",Ip)
    x=b.strip()
    easygui.msgbox(x+"\t\t\t\t\t","第二次确认 域名+.crt")
    b=SSH.sssh('ls /shangchuan/ |grep conf',Ip)
    x=b.strip()
    easygui.msgbox(x+"\t\t\t\t\t","第三次确认 域名+.conf")
    nn=1
    for i in x.split("\n"):
        ff=SSH.sssh("cat /shangchuan/{} |head -n22".format(i),Ip)
        easygui.msgbox(ff ,"第{}次确认  配置文件  {}".format(nn,i))
        nn+=1
def   Restart(Ip):
    SSH.sssh("cp /shangchuan/*.crt /shangchuan/*.key /usr/local/nginx/conf/ ; cp /shangchuan/*.conf /usr/local/nginx/kis/",Ip)
    b=SSH.sssh("/usr/local/nginx/sbin/nginx -t",Ip)
    if easygui.ccbox(b,"配置文件是否 ok"):
        SSH.sssh("/usr/local/nginx/sbin/nginx -s reload",Ip)
    else:
        easygui.msgbox("重新执行脚本","错误")
        SSH.sssh("for i in `ls /shangchuan|grep 'crt\|key'`;do rm -f /usr/local/nginx/conf/$i;done ;for i in `ls /shangchuan|grep conf `;do rm -f /usr/local/nginx/kis/$i;done ",Ip)

def XG_sed(ml,ym,Ip):
    for i in ym:
        print(i)
        if re.findall('http',i):
            pass
        else:
            easygui.msgbox("被修改的域名必须添加http或https","修改域名错误")
            cccccc
    ymm=SSH.sssh('ls /usr/share/nginx/html/',Ip)
    ymmm=ymm.split("\n")
    if ml in ymmm:
        pass
    else:
        easygui.msgbox("{}".format(ymm),"再次确定修改的网站站点  为以下文件夹！")
        cccccc
    pdml="[ -f /usr/share/nginx/html/{}/a.txt  ] ; echo $?".format(ml)
    pd=SSH.sssh(pdml,Ip)
    pd=pd.strip()
    if  str(pd) == "0":
        pass
    else:
        easygui.msgbox("{}   /usr/share/nginx/html/{}/a.txt\n\n\n没有这个文件，无法获取域名!!!".format(Ip,ml), "错误提示")
        cccccc
    jg = SSH.sssh("cat /usr/share/nginx/html/{}/a.txt".format(ml), Ip)
    jg = jg.strip()
    jgym = jg.split("\n")
    if len(jgym) == len(ym):
        if easygui.ccbox("原本域名:\n{}\n\n改为:\n{}".format(jg,"\n".join(ym)),"修改确定"):
            pass
        else:
            cccccc
    else:
        easygui.msgbox("在 {} 输入的域名为{}个,目录下的域名为{}个\n\n现在有域名\n{}\n\n请保持一致！！！ \n\n如果域名不够，拆开一个域名 https 改为 http ".format(ml,len(ym),len(jgym),jg),"错误提示")
        cccccccc
    execc = []
    for i in range(len(jgym)):
        exec_s='find /usr/share/nginx/html/{}/ -type f |xargs  sed -i  "s#{}#{}#g" '.format(ml,jgym[i].strip(),ym[i].strip())
        SSH.sssh(exec_s, Ip)
        execc.append(exec_s)
    cnmd=SSH.sssh("cat /usr/share/nginx/html/{}/a.txt".format(ml),Ip)
    easygui.msgbox("{} 下新域名为\n\n{}".format(ml,cnmd),"修改结束")
    return execc
