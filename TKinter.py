# -*- mode=python ending:utf-8 -*-
#pack：按添加顺序排列组件 bao
#grid：按行列形式排列组件 wangge          ,
#          row=0,column=0 行，列      rowspan占几行，columnspan占几列
#           sticky='w'   w左，e右
#           width=20 宽      height=2 高
#place：允许程序员指定组件的大小和位置 difang
import tkinter
from tkinter import *
from tkinter import ttk
import easygui,time,MYSQL,EXE_SSH,threading
#88
class MY_GUI():

    def __init__(self,xiaoxue,IP):
        self.tkinter=tkinter
        self.xiaoxue=xiaoxue
        self.zhandian=''
        self.wangzhan=''
        self.yuming=''
        self.ptym=''
        self.aa='1'
        self.IP=IP.strip()
        self.TITLE = "88 主域名链接修改 IP:  {}".format(self.IP)
    def XIAOXUE(self):
        self.xiaoxue.title(self.TITLE)
        screenWidth = self.xiaoxue.winfo_screenwidth()      # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()    # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("700x500+{}+{}".format(x,y)) #宽高居中
        #self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg']='#ADD8E6'                    #bg背景颜色 fg字体颜色
        self.xiaoxue.attributes("-alpha", 0.99)       #虚化
        self.xiaoxue.bind("<Control-Key-d>", self.BTN3)         #快捷键事件
        self.xiaoxue.bind("<Control-Key-m>", self.ACM)
        self.xiaoxue.bind("<Control-Key-l>", self.EXIT)
        #self.xiaoxue.attributes("-topmost", -1)        #置顶窗口
        self.xiaoxue.resizable(0, 0)        #固定宽高
        #self.xiaoxue.overrideredirect(True)    #取消边框，慎用

#标签
        self.label1=Label(self.xiaoxue,text="选择站点 :",bg="lightblue",height=1)
        self.label1.grid(row=0,column=0, sticky=W)          #行 列 左粘
        self.label2=Label(self.xiaoxue,text="选择站点里的域名 :",bg="lightblue",height=1)
        self.label2.grid(row=1,column=0, sticky=W)
        self.label3 = Label(self.xiaoxue, text="填写新的替换域名 :", bg="lightblue", height=1)
        self.label3.grid(row=2, column=0, sticky=W)
###站点下拉框
        a = EXE_SSH.shell("ls /usr/share/nginx/html/", self.IP)
        a=a.strip()
        self.zhandian=a.split('\n')
        xVariable = self.tkinter.StringVar()
        self.com = ttk.Combobox(self.xiaoxue, textvariable=xVariable, width=30)
        self.com.grid(row=0, column=1, sticky='w')
        self.com["value"] = tuple(self.zhandian)
        self.com.bind("<<ComboboxSelected>>", self.xiala)
###域名下拉框
        self.yuming=''
        xVariablea = self.tkinter.StringVar()
        self.coma = ttk.Combobox(self.xiaoxue, textvariable=xVariablea, width=30)
        self.coma.grid(row=1, column=1, sticky='w')
        self.coma["value"] = tuple(self.yuming)
        #self.entry1 = Entry(self.xiaoxue,width=30)#,state=NORMAL, validate="focus", validatecommand=self.conceal)   #鼠标点击执行conceal函数，可以隐藏下面图形，玩吧
        #self.entry1.grid(row=0, column=1,sticky='w')
        self.entry2 = Entry(self.xiaoxue,width=30,)#show="~")  # 密码隐藏
        self.entry2.grid(row=1, column=1,sticky='w')
        self.entry3 = Entry(self.xiaoxue, width=63, )
        self.entry3.grid(row=2, column=1,columnspan=4, sticky='w')
 #   def conceal(self):  #由输入框触发方才显示下面图标
 #      pass
#按钮
        self.button1=Button(self.xiaoxue,bg="pink",text="刷新", activebackground='lime', command=self.EXIT, width=10)  #activebackground按下去颜色
        self.button1.grid(row=0, column=2,sticky='w')   #调度EXIT函数
        self.button2=Button(self.xiaoxue,bg="pink",text="连接状态", activebackground='lime',command=self.BIND, width=10)
        self.button2.grid(row=1, column=2,sticky='w')   #调度TISHI函数
        self.button3=Button(self.xiaoxue, bg="pink",text="推送",activebackground='lime',command=self.BF,width=10)  # activebackground按下去颜色
        self.button3.grid(row=0, column=4,sticky='e')   #调度BTN3函数
        self.button4=Button(self.xiaoxue, bg="pink",text="历史操作",activebackground='lime', command=self.BTN4,width=10)
        self.button4.grid(row=1, column=4,sticky='e')   #调度BTN4函数
        #self.button5=Button(self.xiaoxue, bg="pink",text="", activebackground='lime', command=self.BIND,width=10)  # activebackground按下去颜色
        #self.button5.grid(row=0, column=4,columnspan=2)   #调度BTN5函数
       # self.button6=Button(self.xiaoxue, bg="pink",text="所有站点  ",activebackground='lime', command=self.TISHIs,width=10)
        #self.button6.grid(row=1, column=4,columnspan=2)   #调度BTN6函数
        self.button7 = Button(self.xiaoxue, bg="pink", text="替换", activebackground='lime', command=self.SHELL,width=10)
        self.button7.grid(row=2, column=4, sticky='e')  # 调度BTN6函数

# 文本框
        self.scroll2 = Scrollbar()  # 滚动条
        self.text1 = Text(self.xiaoxue, width=97, height=17)  #
        self.scroll2.config(command=self.text1.yview)
        self.text1.config(yscrollcommand=self.scroll2.set)
        self.text1.tag_config("tag2", foreground="green" )
        self.text1.tag_config("tag1", foreground="red")
        self.text1.grid(row=3, column=0, columnspan=5)
        self.scroll2.grid(row=3, column=6, columnspan=1, sticky='nsw')
#输出框
        self.scroll1 = Scrollbar()       #滚动条
        self.listbox=Listbox(self.xiaoxue,width=97,selectmode="extended")
        self.scroll1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll1.set)
        self.listbox.grid(row=4,column=0,columnspan=5) #nswe 上下左右
        self.scroll1.grid(row=4,column=6,columnspan=1,sticky="nsw")
        threading.Thread(target=self.zt).start()
        # 选择网站

    def zt(self):
        while True:
            if EXE_SSH.active(self.IP) == 'ok':
                self.button2 = Button(self.xiaoxue, bg="pink", text="连接正常", activebackground='lime', command=self.BIND,
                                      width=10)
                self.button2.grid(row=1, column=2, sticky='w')
            else:
                self.button2 = Button(self.xiaoxue, bg="pink", text="连接异常", activebackground='lime', command=self.BIND,
                                      width=10)
                self.button2.grid(row=1, column=2, sticky='w')

# 选择网站
    def xiala(self,event):
            self.wangzhan=self.com.get()
            self.YM(self.wangzhan)
    def xiala1(self,event):
        self.ptym = self.comb.get()
        b='已选站点: {}    要修改的域名是: {}\n'.format(self.wangzhan,self.ptym)
        self.text1.insert(1.0, b)  # 输出到 listbox
        self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))

    # 选择域名 ###域名下拉框
    def YM(self,wangzhan):
        shh="cat /usr/share/nginx/html/{}/a.txt".format(wangzhan)
        b = EXE_SSH.shell(shh, self.IP)  # 执行shell
        self.yuming = b.split()
        xVariableb = self.tkinter.StringVar()
        self.comb = ttk.Combobox(self.xiaoxue, textvariable=xVariableb, width=30)
        self.comb.grid(row=1, column=1, sticky='w')
        self.comb["value"] = tuple(self.yuming)
        self.comb.bind("<<ComboboxSelected>>", self.xiala1)

        #MYSQL.insert(self.IP, self.TIME(), shh)  # 保存在数据库

        #BTN1
    def EXIT(self):
        self.XIAOXUE()
    def wait(self):
        while True:
            if self.aa == '0':
                time.sleep(0.3)
                self.text1.insert(1.0, "· ", "tag2")
            else:
                self.text1.insert(1.0, "\n推送成功", "tag2")
                self.text1.insert(1.0,
                                  "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                      self.TIME()))

                return 0
    def BF(self):
        self.text1.insert(1.0, "\n等待推送完成", "tag2")
        self.aa='0'
        threading.Thread(target=self.wait).start()
        threading.Thread(target=self.BFF).start()
    def BFF(self):
        #self.text1.insert(1.0, "\n耐心等待推送完成", "tag2")
        exec_s = 'bash /xue/back_nginx1.sh'
        a = EXE_SSH.shell(exec_s, self.IP)
        self.aa='1'
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")

            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), history)
        else:
            self.text1.insert(1.0, "\n" + a, "tag2")
            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            MYSQL.insert(self.IP, self.TIME(), a)

        #BTN3
    def BIND(self):
        threading.Thread(target=self.BIND1).start()
    def BIND1(self):
            easygui.msgbox(EXE_SSH.active(self.IP),"连接状态")    #看ssh连接是否正常
#BTN4
    def BTN4(self):
        threading.Thread(target=self.BTN41).start()
    def BTN41(self):
        if  MYSQL.active()== "ok":
          self.listbox.delete(0, END)  # 从数据库输出到listbox历史执行命令
          for i in MYSQL.select()[-1::-1]:
              self.listbox.insert(END, i)

#执行shell
    def SHELL(self):
        threading.Thread(target=self.SHELL1).start()
    def SHELL1(self):
        xym=self.entry3.get()
        xym=xym.strip()             #执行shell
        ax=self.ptym.strip()
        bx=xym.strip()
        cx=self.wangzhan.strip()
        exec_s = 'sed -i  "s#{}#{}#g" $(grep -rl {} /usr/share/nginx/html/{}/) '.format(ax,bx,ax,cx)
        a=EXE_SSH.shell(exec_s, self.IP)
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")
            self.text1.insert(1.0,"\n{} 旧: {}  新: {}   成功".format(cx,ax,bx),"tag2")
            #self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))
            history = "{} {} {} ".format(self.IP,self.TIME(),exec_s)
            MYSQL.insert(self.IP,self.TIME(),history)                     #保存在数据库
        else:
            self.text1.insert(1.0,"\n"+a,"tag1")
            self.text1.insert(1.0, "\n{} 旧: {}  新: {}   失败".format(cx,ax,bx),"tag1")
            #self.text1.insert(1.0, "\n"+exec_s,"tag1")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), a)
        # 事件
    def BTN3(self, event):  # 事件触发删除历史命令
        if easygui.ccbox("你确定要删除本地和数据库的历史记录吗?"):
            pass
        else:
            return
        MYSQL.delete()
# 事件
    def ACM(self, event):
        if MYSQL.active() == "ok":
            easygui.msgbox("数据库连接成功，操作历史可以保存到数据库！！","提示")
        else:
            easygui.msgbox("数据库连接失败！！","提示")
#TIME
    def TIME(self):
        return(time.strftime("%m-%d %H:%M:%S", time.localtime(time.time())))
#99-1
class MY_GUI1():

    def __init__(self,xiaoxue,IP):
        self.tkinter=tkinter
        self.xiaoxue=xiaoxue
        self.zhandian=''
        self.wangzhan=''
        self.yuming=''
        self.ptym=''
        self.aa='1'
        self.IP=IP.strip()
        self.TITLE = "99-1 MASTER域名链接推送 IP: {}".format(self.IP)
    def XIAOXUE(self):
        self.xiaoxue.title(self.TITLE)
        screenWidth = self.xiaoxue.winfo_screenwidth()      # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()    # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("700x500+{}+{}".format(x,y)) #宽高居中
        #self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg']='#ADD8E6'                    #bg背景颜色 fg字体颜色
        self.xiaoxue.attributes("-alpha", 0.99)       #虚化
        self.xiaoxue.bind("<Control-Key-d>", self.BTN3)         #快捷键事件
        self.xiaoxue.bind("<Control-Key-m>", self.ACM)
        self.xiaoxue.bind("<Control-Key-l>", self.EXIT)
        #self.xiaoxue.attributes("-topmost", -1)        #置顶窗口
        self.xiaoxue.resizable(0, 0)        #固定宽高
        #self.xiaoxue.overrideredirect(True)    #取消边框，慎用

#标签
        self.label1=Label(self.xiaoxue,text="选择站点 :",bg="lightblue",height=1)
        self.label1.grid(row=0,column=0, sticky=W)          #行 列 左粘
        self.label2=Label(self.xiaoxue,text="选择站点里的域名 :",bg="lightblue",height=1)
        self.label2.grid(row=1,column=0, sticky=W)
        self.label3 = Label(self.xiaoxue, text="填写新的替换域名 :", bg="lightblue", height=1)
        self.label3.grid(row=2, column=0, sticky=W)
###站点下拉框
        a = EXE_SSH.shell("ls /usr/share/nginx/html/", self.IP)
        a=a.strip()
        self.zhandian=a.split('\n')
        xVariable = self.tkinter.StringVar()
        self.com = ttk.Combobox(self.xiaoxue, textvariable=xVariable, width=30)
        self.com.grid(row=0, column=1, sticky='w')
        self.com["value"] = tuple(self.zhandian)
        self.com.bind("<<ComboboxSelected>>", self.xiala)
###域名下拉框
        self.yuming=''
        xVariablea = self.tkinter.StringVar()
        self.coma = ttk.Combobox(self.xiaoxue, textvariable=xVariablea, width=30)
        self.coma.grid(row=1, column=1, sticky='w')
        self.coma["value"] = tuple(self.yuming)
        #self.entry1 = Entry(self.xiaoxue,width=30)#,state=NORMAL, validate="focus", validatecommand=self.conceal)   #鼠标点击执行conceal函数，可以隐藏下面图形，玩吧
        #self.entry1.grid(row=0, column=1,sticky='w')
        self.entry2 = Entry(self.xiaoxue,width=30,)#show="~")  # 密码隐藏
        self.entry2.grid(row=1, column=1,sticky='w')
        self.entry3 = Entry(self.xiaoxue, width=63, )
        self.entry3.grid(row=2, column=1,columnspan=4, sticky='w')
 #   def conceal(self):  #由输入框触发方才显示下面图标
 #      pass
#按钮
        self.button1=Button(self.xiaoxue,bg="pink",text="刷新", activebackground='lime', command=self.EXIT, width=10)  #activebackground按下去颜色
        self.button1.grid(row=0, column=2,sticky='w')   #调度EXIT函数
        self.button2=Button(self.xiaoxue,bg="pink",text="连接状态", activebackground='lime',command=self.BIND, width=10)
        self.button2.grid(row=1, column=2,sticky='w')   #调度TISHI函数
        self.button3=Button(self.xiaoxue, bg="pink",text="推送",activebackground='lime',command=self.BF,width=10)  # activebackground按下去颜色
        self.button3.grid(row=0, column=4,sticky='e')   #调度BTN3函数
        self.button4=Button(self.xiaoxue, bg="pink",text="历史操作",activebackground='lime', command=self.BTN4,width=10)
        self.button4.grid(row=1, column=4,sticky='e')   #调度BTN4函数
        #self.button5=Button(self.xiaoxue, bg="pink",text="", activebackground='lime', command=self.BIND,width=10)  # activebackground按下去颜色
        #self.button5.grid(row=0, column=4,columnspan=2)   #调度BTN5函数
       # self.button6=Button(self.xiaoxue, bg="pink",text="所有站点  ",activebackground='lime', command=self.TISHIs,width=10)
        #self.button6.grid(row=1, column=4,columnspan=2)   #调度BTN6函数
        self.button7 = Button(self.xiaoxue, bg="pink", text="替换", activebackground='lime', command=self.SHELL,width=10)
        self.button7.grid(row=2, column=4, sticky='e')  # 调度BTN6函数

# 文本框
        self.scroll2 = Scrollbar()  # 滚动条
        self.text1 = Text(self.xiaoxue, width=97, height=17)  #
        self.scroll2.config(command=self.text1.yview)
        self.text1.config(yscrollcommand=self.scroll2.set)
        self.text1.tag_config("tag2", foreground="green" )
        self.text1.tag_config("tag1", foreground="red")
        self.text1.grid(row=3, column=0, columnspan=5)
        self.scroll2.grid(row=3, column=6, columnspan=1, sticky='nsw')
#输出框
        self.scroll1 = Scrollbar()       #滚动条
        self.listbox=Listbox(self.xiaoxue,width=97,selectmode="extended")
        self.scroll1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll1.set)
        self.listbox.grid(row=4,column=0,columnspan=5) #nswe 上下左右
        self.scroll1.grid(row=4,column=6,columnspan=1,sticky="nsw")
        threading.Thread(target=self.zt).start()
        # 选择网站

    def zt(self):
        while True:
            if EXE_SSH.active1(self.IP) == 'ok':
                self.button2 = Button(self.xiaoxue, bg="pink", text="连接正常", activebackground='lime', command=self.BIND,
                                      width=10)
                self.button2.grid(row=1, column=2, sticky='w')
            else:
                self.button2 = Button(self.xiaoxue, bg="pink", text="连接异常", activebackground='lime', command=self.BIND,
                                      width=10)
                self.button2.grid(row=1, column=2, sticky='w')

# 选择网站
    def xiala(self,event):
            self.wangzhan=self.com.get()
            self.YM(self.wangzhan)
    def xiala1(self,event):
        self.ptym = self.comb.get()
        b='已选站点: {}    要修改的域名是: {}\n'.format(self.wangzhan,self.ptym)
        self.text1.insert(1.0, b)  # 输出到 listbox
        self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))

    # 选择域名 ###域名下拉框
    def YM(self,wangzhan):
        shh="cat /software/{}/tag.txt".format(wangzhan)
        b = EXE_SSH.shell1(shh, self.IP)  # 执行shell
        self.yuming = b.split()
        xVariableb = self.tkinter.StringVar()
        self.comb = ttk.Combobox(self.xiaoxue, textvariable=xVariableb, width=30)
        self.comb.grid(row=1, column=1, sticky='w')
        self.comb["value"] = tuple(self.yuming)
        self.comb.bind("<<ComboboxSelected>>", self.xiala1)

        #MYSQL.insert(self.IP, self.TIME(), shh)  # 保存在数据库

        #BTN1
    def EXIT(self):
        self.XIAOXUE()
    def wait(self):
        while True:
            if self.aa == '0':
                time.sleep(0.3)
                self.text1.insert(1.0, "· ", "tag2")
            else:
                self.text1.insert(1.0, "\n推送成功", "tag2")
                self.text1.insert(1.0,
                                  "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                      self.TIME()))

                return 0
    def BF(self):
        self.text1.insert(1.0, "\n等待推送完成", "tag2")
        self.aa='0'
        threading.Thread(target=self.wait).start()
        threading.Thread(target=self.BFF).start()
    def BFF(self):
        #self.text1.insert(1.0, "\n耐心等待推送完成", "tag2")
        exec_s = '/usr/bin/ansible -m shell -a "bash /software/1手动同步.sh" China'
        a = EXE_SSH.shell1(exec_s, self.IP)
        self.aa='1'
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")

            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), history)
        else:
            self.text1.insert(1.0, "\n" + a, "tag2")
            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            MYSQL.insert(self.IP, self.TIME(), a)

        #BTN3
    def BIND(self):
        threading.Thread(target=self.BIND1).start()
    def BIND1(self):
            easygui.msgbox(EXE_SSH.active1(self.IP),"连接状态")    #看ssh连接是否正常
#BTN4
    def BTN4(self):
        threading.Thread(target=self.BTN41).start()
    def BTN41(self):
        if  MYSQL.active()== "ok":
          self.listbox.delete(0, END)  # 从数据库输出到listbox历史执行命令
          for i in MYSQL.select()[-1::-1]:
              self.listbox.insert(END, i)
     # else:
      #  with open("a.js",'r') as f:     #查看json文件,输出历史执行命令
       #     js=json.load(f)
      #  self.listbox.delete(0,END)
      #  for i in js:
       #     self.listbox.insert(END,i)

#执行shell
    def SHELL(self):
        threading.Thread(target=self.SHELL1).start()
    def SHELL1(self):
        xym=self.entry3.get()
        xym=xym.strip()             #执行shell
        ax=self.ptym.strip()
        bx=xym.strip()
        cx=self.wangzhan.strip()
        exec_s = 'sed -i  "s#{}#{}#g" $(grep -rl {} /software/{}/) '.format(ax,bx,ax,cx)
        a=EXE_SSH.shell1(exec_s, self.IP)
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")
            self.text1.insert(1.0,"\n{} 旧: {}  新: {}   成功".format(cx,ax,bx),"tag2")
            #self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))
            history = "{} {} {} ".format(self.IP,self.TIME(),exec_s)
            MYSQL.insert(self.IP,self.TIME(),history)                     #保存在数据库
        else:
            self.text1.insert(1.0,"\n"+a,"tag1")
            self.text1.insert(1.0, "\n{} 旧: {}  新: {}   失败".format(cx,ax,bx),"tag1")
            #self.text1.insert(1.0, "\n"+exec_s,"tag1")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), a)
        # 事件
    def BTN3(self, event):  # 事件触发删除历史命令
        if easygui.ccbox("你确定要删除本地和数据库的历史记录吗?"):
            pass
        else:
            return
        MYSQL.delete()
# 事件
    def ACM(self, event):
        if MYSQL.active() == "ok":
            easygui.msgbox("数据库连接成功，操作历史可以保存到数据库！！","提示")
        else:
            easygui.msgbox("数据库连接失败！！","提示")
#TIME
    def TIME(self):
        return(time.strftime("%m-%d %H:%M:%S", time.localtime(time.time())))
#99-2
class MY_GUI2():

    def __init__(self,xiaoxue,IP):
        self.tkinter=tkinter
        self.xiaoxue=xiaoxue
        self.zhandian=''
        self.wangzhan=''
        self.yuming=''
        self.ptym=''
        self.aa='1'
        self.IP=IP.strip()
        self.TITLE = "99-2 MASTER域名链接推送 IP:  {}".format(self.IP)
    def XIAOXUE(self):
        self.xiaoxue.title(self.TITLE)
        screenWidth = self.xiaoxue.winfo_screenwidth()      # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()    # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("700x500+{}+{}".format(x,y)) #宽高居中
        #self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg']='#ADD8E6'                    #bg背景颜色 fg字体颜色
        self.xiaoxue.attributes("-alpha", 0.99)       #虚化
        self.xiaoxue.bind("<Control-Key-d>", self.BTN3)         #快捷键事件
        self.xiaoxue.bind("<Control-Key-m>", self.ACM)
        self.xiaoxue.bind("<Control-Key-l>", self.EXIT)
        #self.xiaoxue.attributes("-topmost", -1)        #置顶窗口
        self.xiaoxue.resizable(0, 0)        #固定宽高
        #self.xiaoxue.overrideredirect(True)    #取消边框，慎用

#标签
        self.label1=Label(self.xiaoxue,text="选择站点 :",bg="lightblue",height=1)
        self.label1.grid(row=0,column=0, sticky=W)          #行 列 左粘
        self.label2=Label(self.xiaoxue,text="选择站点里的域名 :",bg="lightblue",height=1)
        self.label2.grid(row=1,column=0, sticky=W)
        self.label3 = Label(self.xiaoxue, text="填写新的替换域名 :", bg="lightblue", height=1)
        self.label3.grid(row=2, column=0, sticky=W)
###站点下拉框
        a = EXE_SSH.shell("ls /usr/share/nginx/html/", self.IP)
        a=a.strip()
        self.zhandian=a.split('\n')
        xVariable = self.tkinter.StringVar()
        self.com = ttk.Combobox(self.xiaoxue, textvariable=xVariable, width=30)
        self.com.grid(row=0, column=1, sticky='w')
        self.com["value"] = tuple(self.zhandian)
        self.com.bind("<<ComboboxSelected>>", self.xiala)
###域名下拉框
        self.yuming=''
        xVariablea = self.tkinter.StringVar()
        self.coma = ttk.Combobox(self.xiaoxue, textvariable=xVariablea, width=30)
        self.coma.grid(row=1, column=1, sticky='w')
        self.coma["value"] = tuple(self.yuming)
        #self.entry1 = Entry(self.xiaoxue,width=30)#,state=NORMAL, validate="focus", validatecommand=self.conceal)   #鼠标点击执行conceal函数，可以隐藏下面图形，玩吧
        #self.entry1.grid(row=0, column=1,sticky='w')
        self.entry2 = Entry(self.xiaoxue,width=30,)#show="~")  # 密码隐藏
        self.entry2.grid(row=1, column=1,sticky='w')
        self.entry3 = Entry(self.xiaoxue, width=63, )
        self.entry3.grid(row=2, column=1,columnspan=4, sticky='w')
 #   def conceal(self):  #由输入框触发方才显示下面图标
 #      pass
#按钮
        self.button1=Button(self.xiaoxue,bg="pink",text="刷新", activebackground='lime', command=self.EXIT, width=10)  #activebackground按下去颜色
        self.button1.grid(row=0, column=2,sticky='w')   #调度EXIT函数
        self.button2=Button(self.xiaoxue,bg="pink",text="连接状态", activebackground='lime',command=self.BIND, width=10)
        self.button2.grid(row=1, column=2,sticky='w')   #调度TISHI函数
        self.button3=Button(self.xiaoxue, bg="pink",text="推送",activebackground='lime',command=self.BF,width=10)  # activebackground按下去颜色
        self.button3.grid(row=0, column=4,sticky='e')   #调度BTN3函数
        self.button4=Button(self.xiaoxue, bg="pink",text="历史操作",activebackground='lime', command=self.BTN4,width=10)
        self.button4.grid(row=1, column=4,sticky='e')   #调度BTN4函数
        #self.button5=Button(self.xiaoxue, bg="pink",text="", activebackground='lime', command=self.BIND,width=10)  # activebackground按下去颜色
        #self.button5.grid(row=0, column=4,columnspan=2)   #调度BTN5函数
       # self.button6=Button(self.xiaoxue, bg="pink",text="所有站点  ",activebackground='lime', command=self.TISHIs,width=10)
        #self.button6.grid(row=1, column=4,columnspan=2)   #调度BTN6函数
        self.button7 = Button(self.xiaoxue, bg="pink", text="替换", activebackground='lime', command=self.SHELL,width=10)
        self.button7.grid(row=2, column=4, sticky='e')  # 调度BTN6函数

# 文本框
        self.scroll2 = Scrollbar()  # 滚动条
        self.text1 = Text(self.xiaoxue, width=97, height=17)  #
        self.scroll2.config(command=self.text1.yview)
        self.text1.config(yscrollcommand=self.scroll2.set)
        self.text1.tag_config("tag2", foreground="green" )
        self.text1.tag_config("tag1", foreground="red")
        self.text1.grid(row=3, column=0, columnspan=5)
        self.scroll2.grid(row=3, column=6, columnspan=1, sticky='nsw')
#输出框
        self.scroll1 = Scrollbar()       #滚动条
        self.listbox=Listbox(self.xiaoxue,width=97,selectmode="extended")
        self.scroll1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll1.set)
        self.listbox.grid(row=4,column=0,columnspan=5) #nswe 上下左右
        self.scroll1.grid(row=4,column=6,columnspan=1,sticky="nsw")
        threading.Thread(target=self.zt).start()
        # 选择网站

    def zt(self):
        while True:
            if EXE_SSH.active2(self.IP) == 'ok':
                self.button2 = Button(self.xiaoxue, bg="pink", text="连接正常", activebackground='lime', command=self.BIND,
                                      width=10)
                self.button2.grid(row=1, column=2, sticky='w')
            else:
                self.button2 = Button(self.xiaoxue, bg="pink", text="连接异常", activebackground='lime', command=self.BIND,
                                      width=10)
                self.button2.grid(row=1, column=2, sticky='w')

# 选择网站
    def xiala(self,event):
            self.wangzhan=self.com.get()
            self.YM(self.wangzhan)
    def xiala1(self,event):
        self.ptym = self.comb.get()
        b='已选站点: {}    要修改的域名是: {}\n'.format(self.wangzhan,self.ptym)
        self.text1.insert(1.0, b)  # 输出到 listbox
        self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))

    # 选择域名 ###域名下拉框
    def YM(self,wangzhan):
        shh="cat /software/{}/tag.txt".format(wangzhan)
        b = EXE_SSH.shell2(shh, self.IP)  # 执行shell
        self.yuming = b.split()
        xVariableb = self.tkinter.StringVar()
        self.comb = ttk.Combobox(self.xiaoxue, textvariable=xVariableb, width=30)
        self.comb.grid(row=1, column=1, sticky='w')
        self.comb["value"] = tuple(self.yuming)
        self.comb.bind("<<ComboboxSelected>>", self.xiala1)

        #MYSQL.insert(self.IP, self.TIME(), shh)  # 保存在数据库

        #BTN1
    def EXIT(self):
        self.XIAOXUE()
    def wait(self):
        while True:
            if self.aa == '0':
                time.sleep(0.3)
                self.text1.insert(1.0, "· ", "tag2")
            else:
                self.text1.insert(1.0, "\n推送成功", "tag2")
                self.text1.insert(1.0,
                                  "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                      self.TIME()))

                return 0
    def BF(self):
        self.text1.insert(1.0, "\n等待推送完成", "tag2")
        self.aa='0'
        threading.Thread(target=self.wait).start()
        threading.Thread(target=self.BFF).start()
    def BFF(self):
        #self.text1.insert(1.0, "\n耐心等待推送完成", "tag2")
        exec_s = '/usr/bin/ansible -m shell -a "bash /software/1手动同步.sh" web'
        a = EXE_SSH.shell2(exec_s, self.IP)
        self.aa='1'
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")

            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), history)
        else:
            self.text1.insert(1.0, "\n" + a, "tag2")
            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            MYSQL.insert(self.IP, self.TIME(), a)

        #BTN3
    def BIND(self):
        threading.Thread(target=self.BIND1).start()
    def BIND1(self):
            easygui.msgbox(EXE_SSH.active2(self.IP),"连接状态")    #看ssh连接是否正常
#BTN4
    def BTN4(self):
        threading.Thread(target=self.BTN41).start()
    def BTN41(self):
        if  MYSQL.active()== "ok":
          self.listbox.delete(0, END)  # 从数据库输出到listbox历史执行命令
          for i in MYSQL.select()[-1::-1]:
              self.listbox.insert(END, i)
     # else:
      #  with open("a.js",'r') as f:     #查看json文件,输出历史执行命令
       #     js=json.load(f)
      #  self.listbox.delete(0,END)
      #  for i in js:
       #     self.listbox.insert(END,i)

#执行shell
    def SHELL(self):
        threading.Thread(target=self.SHELL1).start()
    def SHELL1(self):
        xym=self.entry3.get()
        xym=xym.strip()             #执行shell
        ax=self.ptym.strip()
        bx=xym.strip()
        cx=self.wangzhan.strip()
        exec_s = 'sed -i  "s#{}#{}#g" $(grep -rl {} /software/{}/) '.format(ax,bx,ax,cx)
        a=EXE_SSH.shell2(exec_s, self.IP)
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")
            self.text1.insert(1.0,"\n{} 旧: {}  新: {}   成功".format(cx,ax,bx),"tag2")
            #self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))
            history = "{} {} {} ".format(self.IP,self.TIME(),exec_s)
            MYSQL.insert(self.IP,self.TIME(),history)                     #保存在数据库
        else:
            self.text1.insert(1.0,"\n"+a,"tag1")
            self.text1.insert(1.0, "\n{} 旧: {}  新: {}   失败".format(cx,ax,bx),"tag1")
            #self.text1.insert(1.0, "\n"+exec_s,"tag1")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), a)
        # 事件
    def BTN3(self, event):  # 事件触发删除历史命令
        if easygui.ccbox("你确定要删除本地和数据库的历史记录吗?"):
            pass
        else:
            return
        MYSQL.delete()
# 事件
    def ACM(self, event):
        if MYSQL.active() == "ok":
            easygui.msgbox("数据库连接成功，操作历史可以保存到数据库！！","提示")
        else:
            easygui.msgbox("数据库连接失败！！","提示")
#TIME
    def TIME(self):
        return(time.strftime("%m-%d %H:%M:%S", time.localtime(time.time())))
#app
class MY_GUI3():

    def __init__(self,xiaoxue,IP):
        self.tkinter=tkinter
        self.xiaoxue=xiaoxue
        self.zhandian=''
        self.wangzhan=''
        self.yuming=''
        self.ptym=''
        self.aa='1'
        self.IP=IP.strip()
        self.TITLE = "APP 链接推送 IP: {}".format(self.IP)
    def XIAOXUE(self):
        self.xiaoxue.title(self.TITLE)
        screenWidth = self.xiaoxue.winfo_screenwidth()      # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()    # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("700x500+{}+{}".format(x,y)) #宽高居中
        #self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg']='#ADD8E6'                    #bg背景颜色 fg字体颜色
        self.xiaoxue.attributes("-alpha", 0.99)       #虚化
        self.xiaoxue.bind("<Control-Key-d>", self.BTN3)         #快捷键事件
        self.xiaoxue.bind("<Control-Key-m>", self.ACM)
        self.xiaoxue.bind("<Control-Key-l>", self.EXIT)
        #self.xiaoxue.attributes("-topmost", -1)        #置顶窗口
        self.xiaoxue.resizable(0, 0)        #固定宽高
        #self.xiaoxue.overrideredirect(True)    #取消边框，慎用

#标签
        self.label1=Label(self.xiaoxue,text="选择站点 :",bg="lightblue",height=1)
        self.label1.grid(row=0,column=0, sticky=W)          #行 列 左粘
        self.label2=Label(self.xiaoxue,text="选择站点里的域名 :",bg="lightblue",height=1)
        self.label2.grid(row=1,column=0, sticky=W)
        self.label3 = Label(self.xiaoxue, text="填写新的替换域名 :", bg="lightblue", height=1)
        self.label3.grid(row=2, column=0, sticky=W)
###站点下拉框
        a = EXE_SSH.shell("ls /usr/share/nginx/html/", self.IP)
        a=a.strip()
        self.zhandian=a.split('\n')
        self.zhandian=[]
        xVariable = self.tkinter.StringVar()
        self.com = ttk.Combobox(self.xiaoxue, textvariable=xVariable, width=30)
        self.com.grid(row=0, column=1, sticky='w')
        self.com["value"] = tuple(self.zhandian)
        self.com.bind("<<ComboboxSelected>>", self.xiala)
###域名下拉框
        self.yuming=''
        xVariablea = self.tkinter.StringVar()
        self.coma = ttk.Combobox(self.xiaoxue, textvariable=xVariablea, width=30)
        self.coma.grid(row=1, column=1, sticky='w')
        self.coma["value"] = tuple(self.yuming)
        #self.entry1 = Entry(self.xiaoxue,width=30)#,state=NORMAL, validate="focus", validatecommand=self.conceal)   #鼠标点击执行conceal函数，可以隐藏下面图形，玩吧
        #self.entry1.grid(row=0, column=1,sticky='w')
        self.entry2 = Entry(self.xiaoxue,width=30,)#show="~")  # 密码隐藏
        self.entry2.grid(row=1, column=1,sticky='w')
        self.entry3 = Entry(self.xiaoxue, width=63, )
        self.entry3.grid(row=2, column=1,columnspan=4, sticky='w')
 #   def conceal(self):  #由输入框触发方才显示下面图标
 #      pass
#按钮
        self.button1=Button(self.xiaoxue,bg="pink",text="刷新", activebackground='lime', command=self.EXIT, width=10)  #activebackground按下去颜色
        self.button1.grid(row=0, column=2,sticky='w')   #调度EXIT函数

        self.button2=Button(self.xiaoxue,bg="pink",text="连接状态", activebackground='lime',command=self.BIND, width=10)
        self.button2.grid(row=1, column=2,sticky='w')   #调度TISHI函数
        self.button3=Button(self.xiaoxue, bg="pink",text="推送",activebackground='lime',command=self.BF,width=10)  # activebackground按下去颜色
        self.button3.grid(row=0, column=4,sticky='e')   #调度BTN3函数
        self.button4=Button(self.xiaoxue, bg="pink",text="历史操作",activebackground='lime', command=self.BTN4,width=10)
        self.button4.grid(row=1, column=4,sticky='e')   #调度BTN4函数
        #self.button5=Button(self.xiaoxue, bg="pink",text="", activebackground='lime', command=self.BIND,width=10)  # activebackground按下去颜色
        #self.button5.grid(row=0, column=4,columnspan=2)   #调度BTN5函数
       # self.button6=Button(self.xiaoxue, bg="pink",text="所有站点  ",activebackground='lime', command=self.TISHIs,width=10)
        #self.button6.grid(row=1, column=4,columnspan=2)   #调度BTN6函数
        self.button7 = Button(self.xiaoxue, bg="pink", text="替换", activebackground='lime', command=self.SHELL,width=10)
        self.button7.grid(row=2, column=4, sticky='e')  # 调度BTN6函数

# 文本框
        self.scroll2 = Scrollbar()  # 滚动条
        self.text1 = Text(self.xiaoxue, width=97, height=17)  #
        self.scroll2.config(command=self.text1.yview)
        self.text1.config(yscrollcommand=self.scroll2.set)
        self.text1.tag_config("tag2", foreground="green" )
        self.text1.tag_config("tag1", foreground="red")
        self.text1.grid(row=3, column=0, columnspan=5)
        self.scroll2.grid(row=3, column=6, columnspan=1, sticky='nsw')
#输出框
        self.scroll1 = Scrollbar()       #滚动条
        self.listbox=Listbox(self.xiaoxue,width=97,selectmode="extended")
        self.scroll1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll1.set)
        self.listbox.grid(row=4,column=0,columnspan=5) #nswe 上下左右
        self.scroll1.grid(row=4,column=6,columnspan=1,sticky="nsw")
        threading.Thread(target=self.zt).start()
# 选择网站
    def zt(self):
     while True:
        if EXE_SSH.active2(self.IP)  == 'ok':
            self.button2 = Button(self.xiaoxue, bg="pink", text="连接正常", activebackground='lime', command=self.BIND,
                                  width=10)
            self.button2.grid(row=1, column=2, sticky='w')
        else:
            self.button2 = Button(self.xiaoxue, bg="pink", text="连接异常", activebackground='lime', command=self.BIND,
                                  width=10)
            self.button2.grid(row=1, column=2, sticky='w')

    def xiala(self,event):
            self.wangzhan=self.com.get()
            self.YM(self.wangzhan)
    def xiala1(self,event):
        self.ptym = self.comb.get()
        b='已选站点: {}    要修改的域名是: {}\n'.format(self.wangzhan,self.ptym)
        self.text1.insert(1.0, b)  # 输出到 listbox
        self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))

    # 选择域名 ###域名下拉框
    def YM(self,wangzhan):
        shh="cat /software/{}/tag.txt".format(wangzhan)
        b = EXE_SSH.shell2(shh, self.IP)  # 执行shell
        self.yuming = b.split()
        xVariableb = self.tkinter.StringVar()
        self.comb = ttk.Combobox(self.xiaoxue, textvariable=xVariableb, width=30)
        self.comb.grid(row=1, column=1, sticky='w')
        self.comb["value"] = tuple(self.yuming)
        self.comb.bind("<<ComboboxSelected>>", self.xiala1)

        #MYSQL.insert(self.IP, self.TIME(), shh)  # 保存在数据库

        #BTN1
    def EXIT(self):
        self.XIAOXUE()
    def wait(self):
        while True:
            if self.aa == '0':
                time.sleep(0.3)
                self.text1.insert(1.0, "· ", "tag2")
            else:
                self.text1.insert(1.0, "\n推送成功", "tag2")
                self.text1.insert(1.0,
                                  "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                      self.TIME()))

                return 0
    def BF(self):
        self.text1.insert(1.0, "\n等待推送完成", "tag2")
        self.aa='0'
        threading.Thread(target=self.wait).start()
        threading.Thread(target=self.BFF).start()
    def BFF(self):
        #self.text1.insert(1.0, "\n耐心等待推送完成", "tag2")
        exec_s = '/usr/bin/ansible -m shell -a "bash /software/1手动同步.sh" App'
        a = EXE_SSH.shell2(exec_s, self.IP)
        self.aa='1'
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")

            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), history)
        else:
            self.text1.insert(1.0, "\n" + a, "tag2")
            # self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            MYSQL.insert(self.IP, self.TIME(), a)

        #BTN3
    def BIND(self):
        threading.Thread(target=self.BIND1).start()
    def BIND1(self):
            easygui.msgbox(EXE_SSH.active2(self.IP),"连接状态")    #看ssh连接是否正常
#BTN4
    def BTN4(self):
        threading.Thread(target=self.BTN41).start()
    def BTN41(self):
        if  MYSQL.active()== "ok":
          self.listbox.delete(0, END)  # 从数据库输出到listbox历史执行命令
          for i in MYSQL.select()[-1::-1]:
              self.listbox.insert(END, i)
     # else:
      #  with open("a.js",'r') as f:     #查看json文件,输出历史执行命令
       #     js=json.load(f)
      #  self.listbox.delete(0,END)
      #  for i in js:
       #     self.listbox.insert(END,i)

#执行shell
    def SHELL(self):
        threading.Thread(target=self.SHELL1).start()
    def SHELL1(self):
        xym=self.entry3.get()
        xym=xym.strip()             #执行shell
        ax=self.ptym.strip()
        bx=xym.strip()
        cx=self.wangzhan.strip()
        exec_s = 'sed -i  "s#{}#{}#g" $(grep -rl {} /software/{}/) '.format(ax,bx,ax,cx)
        a=EXE_SSH.shell2(exec_s, self.IP)
        if 'error' not in a:
            self.text1.insert(1.0, "\n" + a, "tag2")
            self.text1.insert(1.0,"\n{} 旧: {}  新: {}   成功".format(cx,ax,bx),"tag2")
            #self.text1.insert(1.0, "\n"+exec_s, "tag2")  # 输出到 listbox
            self.text1.insert(1.0, "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(self.TIME()))
            history = "{} {} {} ".format(self.IP,self.TIME(),exec_s)
            MYSQL.insert(self.IP,self.TIME(),history)                     #保存在数据库
        else:
            self.text1.insert(1.0,"\n"+a,"tag1")
            self.text1.insert(1.0, "\n{} 旧: {}  新: {}   失败".format(cx,ax,bx),"tag1")
            #self.text1.insert(1.0, "\n"+exec_s,"tag1")  # 输出到 listbox
            self.text1.insert(1.0,
                              "\n-------------------------------------------------------------------------------------------------\n时间 {} \n".format(
                                  self.TIME()))
            history = "{} {} {} ".format(self.IP, self.TIME(), exec_s)
            MYSQL.insert(self.IP, self.TIME(), a)
        # 事件
    def BTN3(self, event):  # 事件触发删除历史命令
        if easygui.ccbox("你确定要删除本地和数据库的历史记录吗?"):
            pass
        else:
            return
        MYSQL.delete()
# 事件
    def ACM(self, event):
        if MYSQL.active() == "ok":
            easygui.msgbox("数据库连接成功，操作历史可以保存到数据库！！","提示")
        else:
            easygui.msgbox("数据库连接失败！！","提示")
#TIME
    def TIME(self):
        return(time.strftime("%m-%d %H:%M:%S", time.localtime(time.time())))

if __name__=="__main__":
    HO = easygui.choicebox(
        '选择你需要管理的服务器\n', '运维工具', ["99-1", '99-2','APP','88'])
    if HO == '99-1':
        IP = "192.168.1.10"
        Start=Tk()
        MY_GUI1(Start,IP).XIAOXUE()
        Start.mainloop()
