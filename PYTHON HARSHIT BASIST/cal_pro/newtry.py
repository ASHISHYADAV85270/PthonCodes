from tkinter import *
from tkinter import Frame, ttk,filedialog
import tkinter
from pygame import mixer
from PIL import ImageTk,Image
import PIL
import os
from tkinter.messagebox import showinfo
import shutil

root = Tk()
root.title("first tkinter window")
root.geometry("700x700")
root.configure(background="grey")
class first_tk:
    def __init__(self,root):
        self.root = root
        mixer.init()
        
        self.st=os.getcwd() + "\ ".replace(" ","")
        os.chdir(r"D:\CODES\PYTHON HARSHIT BASIST\cal_pro")
        self.open_data={}
        photo=PhotoImage(file="images\\logo.png")
        self.root.iconphoto(False,photo)   #y kese hua
        self.button_frame=ttk.Labelframe(self.root)
        self.button_frame.grid(row=0,column=0,sticky="we")

        self.openfolder_img=self.pic_Resize("images\\open_folder.png",30,30)
        b1=ttk.Button(self.button_frame,image=self.openfolder_img,command=self.openfolder) #open folder
        b1.grid(row=0,column=0)
        
        self.openfile_img=self.pic_Resize("images\\open-file.png",30,30)
        b2=ttk.Button(self.button_frame,image=self.openfile_img,command=self.openfile) #open file
        b2.grid(row=0,column=1,padx=10)

        self.golive_img=self.pic_Resize("images\\go_live_.png",30,30)
        b3=ttk.Button(self.button_frame,image=self.golive_img)
        b3.grid(row=0,column=2,padx=10)



        self.del_img=self.pic_Resize("images\\delete.png",30,30)
        b3_del=ttk.Button(self.button_frame,image=self.del_img)
        b3_del.grid(row=0,column=3,padx=10)



        self.rename_img=self.pic_Resize("images\\rename.png",30,30)
        b3_rename=ttk.Button(self.button_frame,image=self.rename_img,command=self.rename)
        b3_rename.grid(row=0,column=4,padx=10)

        



        self.listbox_frame=Frame(self.root,highlightbackground="black")
        self.listbox_frame.grid(row=1,column=0,sticky="NWS")
        Grid.rowconfigure(self.root,1,weight = 1)
        Grid.columnconfigure(self.root,0,weight = 1)

        self.l_box=Listbox(self.listbox_frame,background="grey")
        self.l_box.grid(sticky="NWS")
        Grid.rowconfigure(self.listbox_frame,0,weight = 1)
        Grid.columnconfigure(self.listbox_frame,0,weight = 1)


        self.musicbox_frame=Frame(self.root,background="grey")
        self.musicbox_frame.grid(row=1,column=2,sticky="nes")
        Grid.rowconfigure(self.root,1,weight=1)
        Grid.columnconfigure(self.root,2,weight = 1)

        
        
        self.badiimage =self.pic_Resize(("images\\bg.PNG"),300,280)
        bgimage=Label(self.musicbox_frame,image=self.badiimage,background="grey")
        bgimage.grid(row=0,column=0,sticky="w")

        self.duration_play=Scale(self.musicbox_frame,from_=0,to=100,length=300,orient="horizontal",background="grey",fg="grey",cursor="circle",activebackground="black",
        )
        self.duration_play.grid(row=1,column=0,sticky=W)

        self.but1_frame=Frame(self.musicbox_frame,background="grey")
        self.but1_frame.grid(row=2,column=0,sticky="w",pady=10)



        self.loop_img=self.pic_Resize("images\\loop.png",30,30)
        b1_loop=ttk.Button(self.but1_frame,image=self.loop_img)
        b1_loop.grid(row=0,column=0)


        self.volume_img=self.pic_Resize("images\\volume.png",30,30)
        b1_volume=ttk.Button(self.but1_frame,image=self.volume_img)
        b1_volume.grid(row=0,column=1,padx=10)
        self.volume_scale=ttk.Scale(self.but1_frame,from_=0.0,to=1.0,value=0.8)
        self.volume_scale.grid(row=0,column=2,padx=5)



        self.but2_frame=Frame(self.musicbox_frame,background="grey")
        self.but2_frame.grid(row=3,column=0,sticky="w",pady=10)


        self.back_img=self.pic_Resize("images\\back.png",30,30)
        b1_back=ttk.Button(self.but2_frame,image=self.back_img)
        b1_back.grid(row=0,column=0)


        self.pause_img=self.pic_Resize("images\\pause.png",30,30)
        b1_pause=ttk.Button(self.but2_frame,image=self.pause_img)
        b1_pause.grid(row=0,column=1,padx=10)

        self.forward_img=self.pic_Resize("images\\forward.png",30,30)
        b1_ford=ttk.Button(self.but2_frame,image=self.forward_img)
        b1_ford.grid(row=0,column=2,padx=10)

        self.stop_img=self.pic_Resize("images\\stop.png",30,30)
        b1_pstop=ttk.Button(self.but2_frame,image=self.stop_img)
        b1_pstop.grid(row=0,column=3,padx=10)


        self.root.mainloop()


    def firsttun(self):
        if os.path.exists(self.st +r"songs"):
            paths=os.listdir(self.st +r"songs")
            for path in paths:
                self.l_box.insert("end",path)
                self.open_data.update({path:self.st+ "songs\ ".replace(" ","") + path})
        else:
            os.mkdir(self.st+ "songs")
        

    def pic_Resize(self,src,widht,height):
        path=Image.open(src)  #iamge path
        im_resized=path.resize((widht,height),Image.ANTIALIAS)
        im_resized=PIL.ImageTk.PhotoImage(im_resized)
        return im_resized


    def openfolder(self):
        f_dir=filedialog.askdirectory(title="Select Folder")
        print(f_dir)
        lis=os.listdir(f_dir)
        for song in lis:
            var=os.path.basename(song)
            if ".mp3" or ".ogg" or ".mod"in var:
                if os.path.exists(self.st+"songs\ ".replace(" ","")+ var)==False:
                    shutil.copy(f_dir+"/"+var, self.st+"songs")
                    self.open_data[var]=f_dir+ r"/" +var      #dic mai  key---var    aur ansewer---path
                    self.l_box.insert(END,var)  #list box mai data dallnai kai liye
      
    # def openfile(self):
    #     f_dir=filedialog.askopenfilenames(title="select file",filetypes=(("MP3",".mp3"),("OGG",".ogg"),("MOD",".mod")) )
    #     for k in f_dir:
    #         for i,j in self.open_data.items(): 
    #             if i==os.path.basename(k):
    #                 showinfo("MADARCHOD PHLE SAI HAI",f"{os.path.basename(i)} is  already present")
    #             else:
    #                 self.open_data[os.path.basename(k)]=k
    #                 self.l_box.insert(END,os.path.basename(k))
      
    def openfile(self):
        f_dir=filedialog.askopenfilenames(title="select file",filetypes=(("MP3",".mp3"),("OGG",".ogg"),("MOD",".mod")) )
        for i in f_dir:
                if os.path.exists(self.st+"songs\ ".replace(" ","")+os.path.basename(i))==False:
                     self.open_data[os.path.basename(i)]=i
                     self.l_box.insert(END,os.path.basename(i))
                     shutil.copy(i, self.st+"songs")
                else:
                    showinfo("MADARCHOD PHLE SAI HAI",f"{os.path.basename(i)} is  already present")


            


       
    def rename(self):
        r_window=Toplevel()
        r_window.geometry("400x300")
        r_window.resizable(False,False)
        Label(r_window,text="ENTER THE RENAME").grid(row=0,column=2)
        r_name=Entry(r_window)
        r_name.grid(row=1,column=2,pady=20)

        r_but=ttk.Button(r_window,text="SAVE",command=lambda:self.save_button(r_window,r_name))
        r_but.grid(row=3,column=2,pady=20)
        r_window.mainloop()

    def save_button(self,window,r_name):
        var=self.l_box.curselection()[0]
        if r_name.get() in self.open_data:
            showinfo("name is already there")
        else:
            data=self.l_box.get(var)
            extension=os.path.splitext(data)[1]
            new_path=self.st 
         
        
        


            


       






abj = first_tk(root)


# kite=Tk()
# kite.title("second screen")
# kite.geometry("400x400")
# obj=first_tk(kite)