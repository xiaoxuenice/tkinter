# -*- mode=python ending:utf-8 -*-
#pack：按添加顺序排列组件 bao
#grid：按行列形式排列组件 wangge          ,
#           row=0,column=0 行，列      rowspan占几行，columnspan占几列
#           sticky='w'   w左，e右
#           width=20 宽      height=2 高
#place：允许程序员指定组件的大小和位置 difang
from tkinter import *
import easygui,time,MYSQL,json,os,EXE_SSH
class MY_GUI():

    def __init__(self,xiaoxue,IP):
        self.xiaoxue=xiaoxue
        self.IP=IP.strip()
        if   self.IP == "192.168.116.200":
            self.TITLE = "本地服务器  192.168.116.200"
    def XIAOXUE(self):
        self.xiaoxue.title(self.TITLE)
        screenWidth = self.xiaoxue.winfo_screenwidth()      # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()    # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("700x500+{}+{}".format(x,y)) #宽高居中
        #self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg']='#ADD8E6'                    #bg背景颜色 fg字体颜色
        self.xiaoxue.iconbitmap("a.ico")  # 图标
        self.xiaoxue.attributes("-alpha", 0.99)       #虚化
        self.xiaoxue.bind("<Control-Key-d>", self.BTN3)         #快捷键事件
        self.xiaoxue.bind("<Control-Key-m>", self.ACM)
        # self.xiaoxue.attributes("-topmost", -1)        #置顶窗口
        #self.xiaoxue.resizable(0, 0)        #固定宽高
        #self.xiaoxue.overrideredirect(True)    #取消边框，慎用

#标签
        self.label1=Label(self.xiaoxue,text="修改的站点 :",bg="lightblue",height=1)
        self.label1.grid(row=0,column=0, sticky=W)          #行 列 左粘
        self.label2=Label(self.xiaoxue,text="修改为 :",bg="lightblue",height=1)
        self.label2.grid(row=1,column=0, sticky=W)
        self.label3 = Label(self.xiaoxue, text="shell 命令 :", bg="lightblue", height=1)
        self.label3.grid(row=2, column=0, sticky=W)

#输入框
        self.entry1 = Entry(self.xiaoxue,width=30)#,state=NORMAL, validate="focus", validatecommand=self.conceal)   #鼠标点击执行conceal函数，可以隐藏下面图形，玩吧
        self.entry1.grid(row=0, column=1,sticky='w')
        self.entry2 = Entry(self.xiaoxue,width=30,)#show="~")  # 密码隐藏
        self.entry2.grid(row=1, column=1,sticky='w')
        self.entry3 = Entry(self.xiaoxue, width=63, )
        self.entry3.grid(row=2, column=1,columnspan=4, sticky='w')
 #   def conceal(self):  #由输入框触发方才显示下面图标
 #      pass
#按钮
        self.button1=Button(self.xiaoxue,bg="pink",text="Reload",activebackground='lime',command=self.EXIT, width=10)  #activebackground按下去颜色
        self.button1.grid(row=0, column=2,sticky='w')   #调度EXIT函数
        self.button2=Button(self.xiaoxue,bg="pink",text="EXIT", activebackground='lime',command=self.TISHI, width=10)
        self.button2.grid(row=1, column=2,sticky='w')   #调度TISHI函数
        self.button3=Button(self.xiaoxue, bg="pink",text="Status", activebackground='lime', command=self.BIND,width=10)  # activebackground按下去颜色
        self.button3.grid(row=0, column=3,sticky='w')   #调度BTN3函数
        self.button4=Button(self.xiaoxue, bg="pink",text="History",activebackground='lime', command=self.BTN4,width=10)
        self.button4.grid(row=1, column=3,sticky='w')   #调度BTN4函数
        self.button5=Button(self.xiaoxue, bg="pink",text="exec shell", activebackground='lime', command=self.BTN5,width=10)  # activebackground按下去颜色
        self.button5.grid(row=0, column=4,columnspan=2)   #调度BTN5函数
        self.button6=Button(self.xiaoxue, bg="pink",text="exec sed  ",activebackground='lime', command=self.BTN6,width=10)
        self.button6.grid(row=1, column=4,columnspan=2)   #调度BTN6函数
        self.button7 = Button(self.xiaoxue, bg="pink", text="shell", activebackground='lime', command=self.SHELL,width=10)
        self.button7.grid(row=2, column=4, columnspan=2)  # 调度BTN6函数

# 文本框
        self.scroll2 = Scrollbar()  # 滚动条
        self.text1 = Text(self.xiaoxue, width=97, height=17)  #
        self.scroll2.config(command=self.text1.yview)
        self.text1.config(yscrollcommand=self.scroll2.set)
        self.text1.grid(row=3, column=0, columnspan=5)
        self.scroll2.grid(row=3, column=6, columnspan=1, sticky='nsw')
#输出框
        self.scroll1 = Scrollbar()       #滚动条
        self.listbox=Listbox(self.xiaoxue,width=97,selectmode="extended")
        self.scroll1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll1.set)
        self.listbox.grid(row=4,column=0,columnspan=5) #nswe 上下左右
        self.scroll1.grid(row=4,column=6,columnspan=1,sticky="nsw")
        if os.path.isfile("a.js"):
            with open("a.js",'r') as f:
                self.js=json.load(f)        #读取json为self.js
        else:
            self.js=[]                      #第一次先写js变量

#BTN1
    def EXIT(self):
        self.XIAOXUE()
#BTN2
    def TISHI(self):
        easygui.msgbox("走咯。。lalala~",'提示')
        sys.exit(0)

#BTN3
    def BIND(self):
            easygui.msgbox(MYSQL.active(self.IP),"连接状态")    #看ssh连接是否正常
#BTN4
    def BTN4(self):
      if EXE_SSH.active() == "ok":
          self.listbox.delete(0, END)  # 从数据库输出到listbox历史执行命令
          for i in EXE_SSH.select()[-1::-1]:
              self.listbox.insert(END, i)
      else:
        with open("a.js",'r') as f:     #查看json文件,输出历史执行命令
            js=json.load(f)
        self.listbox.delete(0,END)
        for i in js:
            self.listbox.insert(END,i)

#BTN5
    def BTN5(self):
        if easygui.ccbox("你确定要执行证书上传任务吗?","提示"):
            pass
        else:
            ccccccc
        MYSQL.Scp(self.IP)
        MYSQL.Exec_shell(self.IP)
        MYSQL.Cat_conf(self.IP)
        MYSQL.Restart(self.IP)
        aaa=self.IP+" "+self.TIME()+" "+"执行了脚本"   # 执行的命令写入json
        self.js.append(aaa)  # 执行的命令写入json
        with open("a.js", 'w') as f:  # 每次更新保存js变量的json
            json.dump(self.js, f)       # 执行的命令写入json
        EXE_SSH.insert(self.IP,self.TIME(),"执行了脚本")        #执行的命令添加在数据库
#BTN6
    def BTN6(self):         #sed替换按钮
        ml=self.entry1.get()
        ym=self.entry2.get()
        ym=ym.strip()
        if easygui.ccbox("确定域名是以下格式，中间用#号分割，开头结尾不添加。\n\n确定域名个数，单个域名不用写 # \n\n例如:\nhttp://jd.com#http://taobao.com","提示"):
            pass
        else:
            cccccc
        ymm=ym.split("#")
        ymm= [ i for i in ymm if i != '' ]
        aa = MYSQL.XG_sed(ml.strip(), ymm, self.IP)
        print(aa)
        for a in aa:
            print(a)
            EXE_SSH.insert(self.IP, self.TIME(), a)           # 执行的命令添加在数据库
            aaa = self.IP + " " + self.TIME() + " " + a     # 执行的命令写入json
            self.js.append(aaa)                             # 执行的命令写入json
            with open("a.js", 'w') as f:                    # 每次更新保存js变量的json
                json.dump(self.js, f)                       # 执行的命令写入json

#BTN7
    def SHELL(self):
        sh=self.entry3.get()
        sh=sh.strip()
        b=MYSQL.shell(sh,self.IP)                #执行shell
        self.text1.insert(1.0, b)  # 输出到 listbox
        self.text1.insert(1.0, "------------------\n{}\n------------------\n".format(self.TIME()))
        history = "{} {} {} ".format(self.IP,self.TIME(),sh)    # 执行的命令写入json
        self.js.append(history)                                 # 执行的命令写入json
        with open("a.js", 'w') as f:                            # 每次更新保存js变量的json
            json.dump(self.js, f)                                # 执行的命令写入json
        EXE_SSH.insert(self.IP,self.TIME(),sh)                     #保存在数据库
# 事件
    def BTN3(self, event):  # 事件触发删除历史命令
        if easygui.ccbox("你确定要删除本地和数据库的历史记录吗?"):
            pass
        else:
            cccccccc
        self.js = []
        with open("a.js", 'w') as f:  # 每次更新保存js变量的json
                json.dump(self.js, f)
        EXE_SSH.delete()
# 事件
    def ACM(self, event):
        if EXE_SSH.active() == "ok":
            easygui.msgbox("数据库连接成功，操作历史可以保存到数据库！！","提示")
        else:
            easygui.msgbox("数据库连接失败！！","提示")
#TIME
    def TIME(self):
        return(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

if __name__=="__main__":
    IP = easygui.choicebox(
        '本地虚拟服务器    192.168.116.200\n,'选择你需要管理的服务器', ["192.168.116.200"])
    if IP == None:
        sys.exit(1)
    Start=Tk()
    MY_GUI(Start,IP).XIAOXUE()
    Start.mainloop()