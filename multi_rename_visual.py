#coding:utf-8
from tkinter import *
from tkinter import filedialog
import os
import re

class MR(object):
    def __init__(self, title):
        self.win = Tk()
        self.win.title(title)
        self.win.geometry('320x150')
        self.create_widgets()

    def rename(self, path, old, new, check=False):
        path.replace('\\', '/')
        filenames = os.listdir(path)
        new_name = ''
        for filename in filenames:
            if check is True:
                new_name = re.sub(old, new, filename)
            else:
                new_name = filename.replace(old, new)
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
        
    
    def btn_onclick(self):
        path = self.path_entry.get()
        old = self.pattern_entry.get()
        new = self.target_entry.get()
        self.rename(path, old, new, check=self.check_var.get() == 'y')

    def select_path(self):
        path_dialog = filedialog.Directory(self.win)
        path = path_dialog.show()
        self.path_entry.insert(0, path)
        # path_value.go()



    def create_widgets(self):
        Label(self.win, text='请输入文件路径:').grid(column=0, row=0, padx=5, pady=0)
        self.path_entry = Entry(self.win)
        self.path_entry.grid(column=1, row=0, padx=5, pady=0)
        Button(self.win, text='选择路径', command=self.select_path).grid(column=2, row=0)
        
        
        Label(self.win, text='要修改的字符:').grid(column=0, row=1, padx=5, pady=0)
        self.pattern_entry = Entry(self.win)
        self.pattern_entry.grid(column=1, row=1, padx=5, pady=0)
        self.check_var = StringVar()
        self.re_check = Checkbutton(self.win, text='正则', onvalue="y", offvalue="n", variable = self.check_var)
        self.re_check.grid(column=2, row=1)
        self.re_check.select()
        
        
        Label(self.win, text='修改后的字符:').grid(column=0, row=2, padx=5, pady=0)
        self.target_entry = Entry(self.win)
        self.target_entry.grid(column=1, row=2, padx=5, pady=0)

        self.btn = Button(self.win, text='修改', command=self.btn_onclick, width=10).grid(column=1, row=3, rowspan=2)
        # self.btn.configure(width=30)




if __name__ == '__main__':
    m = MR('改名v0.1')
    m.win.mainloop()