import requests 
from bs4 import BeautifulSoup
import tkinter.messagebox as tmsg
from tkinter import *
import pandas as pd
import os
import time


class Save:
    def getData(self):
        
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like   Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = linkvalue.get()
        req = requests.get(url, headers = headers)
        dataset = {"Name" :[], "Website":[]}
    
        soup = BeautifulSoup(req.text, 'lxml')
    
        with open("link.html","w",encoding = 'utf-8') as f:
            f.write(soup.prettify())
        
        # ahref = soup.find_all("a")   
        # for j in ahref:
        #     print(j.text)
        for name in soup.find_all('a'):
            print(name.text)
            # name = [tr for tr in i ]
            dataset["Name"].append(name.text)
            # print(name.get_text())
            # website = i.get("href")
            # print([website])
            # dataset["Website"].append(website)
            # if len(dataset["Website"]) == len(dataset["Name"]):
            #     break
        
        for i in soup.find_all('a'):
            website = i.get("href")
            print(website)
            dataset["Website"].append(website)
            if len(dataset["Website"]) == len(dataset["Name"]):
                break
            
        
        time.sleep(2)
        statusvar.set("Data Extracted.")
        
        return 0
    def downloadData(self):
        time.sleep(1)
        save_in_pc = tmsg.askquestion("Save File","Do you want to save the extracted file ?")
        print(save_in_pc)
        time.sleep(1)
        if (save_in_pc == "yes"):
            if(not os.path.exists("data")):
                os.mkdir("data")
                os.mkdir("data/content")
                df = pd.DataFrame.from_dict(dataset)
                df.to_excel("data/content/web.xlsx" , index = False)
                
            save_msg = "Your file is saved in your pc."
            tmsg.showinfo("File info",save_msg)
            root.destroy()
            
        else :
            time.sleep(1)
            notsave_msg = "Your File is not save."
            tmsg.showinfo("File info",notsave_msg)
            root.destroy()
        return 0
sfile = Save()



    
    
root = Tk()
root.title("Link Extractor")
root.geometry("600x400")
root.configure(background = "#28282B")
p1 = PhotoImage(file = 'icon.png')
root.iconphoto(False,p1)
root.resizable(False, False)

f1 = Frame(root ,bg = "black", borderwidth = 2 , )
f1.pack(side = TOP , fill = X )

f2 =  Frame(root ,bg = "#28282B" ,borderwidth = 2 ,)
f2.pack(side = TOP, fill = X, pady = 20)

f3 = Frame(root, borderwidth = 6, bg = "#28282B" )
f3.pack(side = TOP , fill = X )

f4 = Frame(root, borderwidth = 6 )
f4.pack(side = BOTTOM , fill = X )


Label(f1, text = "Link Extractor",fg = "white",bg = "black",font=('Helvetica', 20 , "bold" ,)).pack()

Label(f2, text = "Paste your Link here",font=('Helvetica', 10 ),fg = "#FBFCF6", anchor=S, bg ="#28282B" ).grid(row = 0, column = 0,padx = 50,sticky="W")
linkvalue = StringVar()
linkentry= Entry(f2, textvariable = linkvalue, width = 60 ,font=('Helvetica', 10 , "bold" ,"underline")).grid(row = 1, column = 0,padx = 40, pady = 0 )
link_button = Button(f2,text = "Extract", width = 10, command = sfile.getData).grid(row = 1, column = 2)
statusvar = StringVar()
statusvar.set("     ")
sbar = Label(f2, textvariable = statusvar , anchor ="w",font=('Helvetica', 10 ),fg = "#C0C0C0", bg ="#28282B").grid(row = 4, column = 0)
btn = Button(f2, text = "save file", bg = "grey", command = sfile.downloadData).grid(row = 5, column = 0,pady = 20)

Label(f3, text = "- Copy the URL of the website.",font=('Courier', 10  ),bg = "#28282B",fg = "#C0C0C0").grid(row = 0,column = 0,sticky="W")
Label(f3, text = "- Hit the extract button to get all the links related tp that page.",font=('Courier', 10  ),bg = "#28282B",fg = "#C0C0C0").grid(row = 1,column = 0,sticky="W")
Label(f3, text = "- Filter the links as your requirement.",font=('Courier', 10 ),bg = "#28282B",fg = "#C0C0C0").grid(row = 2,column = 0,sticky="W")
Label(f3, text = "- Save the links in your device for further use.",font=('Courier', 10 ),bg = "#28282B",fg = "#C0C0C0").grid(row = 3,column = 0,sticky="W")


Label(f4, text = " © Search more get more ( This is used for research purpose only)",font=('Courier', 10 , "bold" )).pack()




root.mainloop()


    