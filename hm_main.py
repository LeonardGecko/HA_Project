import sys
import tkinter
import time
import os
import datetime
doneCountdown = False
y = 0

"""
pyaudioの実装
"""

def drawTopPage(): #一番最初の画面
	root = tkinter.Tk()

	def getIdValue(event):
		value = idBox.get()
		print(value)

	def idCheckFunc(event):
		value = idBox.get()
		if value[:1] == 'A' or value[:1] == 'a' :
			print("A")
			now = datetime.datetime.today()
			date = str(now.year) \
			      + ('0' + str(now.month))[-2:] \
				  + ('0' + str(now.day))[-2:] \
				  + ('0' + str(now.hour))[-2:] \
				  + ('0' + str(now.minute))[-2:] \
				  + ('0' + str(now.second))[-2:]
			os.makedirs('./data/' + value + '/' + date)
			root.destroy()
			draw_APretest_page()
		elif value[:1] == 'B' or value[:1] == 'b':
			print("B")
			now = datetime.datetime.today()
			date = str(now.year) \
			      + ('0' + str(now.month))[-2:] \
				  + ('0' + str(now.day))[-2:] \
				  + ('0' + str(now.hour))[-2:] \
				  + ('0' + str(now.minute))[-2:] \
				  + ('0' + str(now.second))[-2:]
			os.makedirs('./data/' + value + '/' + date)
			root.destroy()
			draw_BPretest_page()

	root.title(u"HumanAugmentation")
	root.geometry("2560x1600")

	Title = tkinter.Label(text =u"Human Augmentation")
	Title.pack()

	idBox = tkinter.Entry()
	idBox.pack()

	Button = tkinter.Button(text =u"Next", width = 10)
	Button.bind("<Button-1>",idCheckFunc)
	Button.pack()




	root.mainloop()

def draw_APretest_page(): #Aの効果測定

    def Goto(event):
        root.destroy()
        draw_Arest_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print('t0 = ' + str(t))
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        if doneCountdown:
	        print(doneCountdown)
	        Button2 = tkinter.Button(text =u"Next", width = 10)
	        Button2.bind("<Button-1>",Goto)
	        Button2.pack()




    root = tkinter.Tk()
    root.title(u"HumanAugmentationA")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationA")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()

    root.mainloop()


def draw_BPretest_page(): #Bの効果測定

    def Goto(event):
        root.destroy()
        draw_Brest_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print('t1 = ' + str(t))
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        if doneCountdown:
	        print(doneCountdown)
	        Button2 = tkinter.Button(text =u"Next", width = 10)
	        Button2.bind("<Button-1>",Goto)
	        Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationB")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationB")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()



    root.mainloop()



def draw_Arest_page(): #A休憩


    def Goto(event):
        root.destroy()
        draw_AMain_page()

    def GoLast(event):
        root.destroy()
        draw_ALasttest_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print('t2 = ' + str(t))
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        global y
        if doneCountdown:
            if y <= 2:
                print('y = ' + str(y))
                Button2 = tkinter.Button(text =u"Next", width = 10)
                Button2.bind("<Button-1>",Goto)
                Button2.pack()
                y += 1

            elif y > 2:
                Button2 = tkinter.Button(text =u"Next", width = 10)
                Button2.bind("<Button-1>",GoLast)
                Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationArest")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationArest")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()



    root.mainloop()

def draw_Brest_page(): #B休憩

    def Goto(event):
        root.destroy()
        draw_BMain_page()

    def GoLast(event):
        root.destroy()
        draw_BLasttest_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print(t)
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)
        global y
        if doneCountdown:
            if y <= 2:
                print('y = ' + str(y))
                Button2 = tkinter.Button(text =u"Next", width = 10)
                Button2.bind("<Button-1>",Goto)
                Button2.pack()
                y += 1

            elif y > 2:
                Button2 = tkinter.Button(text =u"Next", width = 10)
                Button2.bind("<Button-1>",GoLast)
                Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationBrest")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationBrest")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()



    root.mainloop()

def draw_AMain_page(): #Aテスト

    def Goto(event):
        root.destroy()
        draw_Arest_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print('t4 = ' + str(t))
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        if doneCountdown:

            Button2 = tkinter.Button(text =u"Next", width = 10)
            Button2.bind("<Button-1>",Goto)
            Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationAMain")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationAMain")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()



    root.mainloop()

def draw_BMain_page(): #Bテスト

    def Goto(event):
        root.destroy()
        draw_Brest_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print(t)
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        if doneCountdown:

            Button2 = tkinter.Button(text =u"Next", width = 10)
            Button2.bind("<Button-1>",Goto)
            Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationBMain")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationBMain")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()



    root.mainloop()

def draw_ALasttest_page(): #Aの最後の効果測定

    def Goto(event):
        root.destroy()
        draw_final_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print(t)
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        if doneCountdown:
	        print(doneCountdown)
	        Button2 = tkinter.Button(text =u"Next", width = 10)
	        Button2.bind("<Button-1>",Goto)
	        Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationALast")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationALast")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()

    root.mainloop()

def draw_BLasttest_page(): #Bの最後の効果測定

    def Goto(event):
        root.destroy()
        draw_final_page()

    def countdown(event):
        doneCountdown = False
        CoundDownButton.destroy()
        t = 3
        while t >= 1:
            print(t)
            time.sleep(1)
            t -= 1
        print("end")
        doneCountdown = not (doneCountdown)

        if doneCountdown:
	        print(doneCountdown)
	        Button2 = tkinter.Button(text =u"Next", width = 10)
	        Button2.bind("<Button-1>",Goto)
	        Button2.pack()


    root = tkinter.Tk()
    root.title(u"HumanAugmentationBLast")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human AugmentationBLast")
    Title.pack()

    CoundDownButton = tkinter.Button(text =u"Start", width = 10)
    CoundDownButton.bind("<Button-1>",countdown)
    CoundDownButton.pack()

    root.mainloop()

def draw_final_page(): #最終画面→トップ画面へ

    def Goto(event):
        root.destroy()
        drawTopPage()

    root = tkinter.Tk()
    root.title(u"HumanAugmentation")
    root.geometry("2560x1600")
    Title = tkinter.Label(text =u"Human Augmentation")
    Title.pack()

    NextDownButton = tkinter.Button(text =u"Start", width = 10)
    NextDownButton.bind("<Button-1>",Goto)
    NextDownButton.pack()


    root.mainloop()







drawTopPage()
