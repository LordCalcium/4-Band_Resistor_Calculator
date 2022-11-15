import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

class resistor:
    def __init__(self,B4WIN):
        self.B4WIN = B4WIN
        self.B4WIN.geometry('500x700')
        self.B4WIN.config(bg='gray20')
        self.B4WIN.maxsize(500,700)
        self.B4WIN.minsize(500,700)

        var1 = StringVar()
        #int1 = IntVar()
        var2 = StringVar()
        #int2 = IntVar()
        var3 = StringVar()
        int3 = StringVar()

        var4 = StringVar()
        str4 = StringVar()

        var5 = StringVar()
        var6 = StringVar()
        var7 = StringVar()


        var1.set("")
        #int1.set(0)

        var2.set("")
        #int2.set(0)

        var3.set("")
        int3.set("")

        var4.set("")
        #str4.set(0)

        var5.set("")
        var6.set("")
        var7.set("")


        def iExit():
            iExit = tkinter.messagebox.askyesno("4-Band Resistor Calculator","Confirm if you want to exit?")
            if iExit > 0:
                B4WIN.destroy()
                return

        def iClear():
            iClear = tkinter.messagebox.askyesno("4-Band Resistor Calculator","Confirm if you want to clear all calculation?")
            if iClear > 0:
                var1.set("")
                #int1.set("")
                var2.set("")
                #int2.set("")
                var3.set("")
                int3.set("")
                var4.set("")
                str4.set("")
                var5.set("")
                var6.set("")
                var7.set("")
                return

        def Band1_Black():
            var1.set("0")
            #int1.set(0)
        def Band1_Brown():
            var1.set("1")
            #int1.set(1)
        def Band1_Red():
            var1.set("2")
            #int1.set(2)
        def Band1_Orange():
            var1.set("3")
            #int1.set(3)
        def Band1_Yellow():
            var1.set("4")
            #int1.set(4)
        def Band1_Green():
            var1.set("5")
            #int1.set(5)
        def Band1_Blue():
            var1.set("6")
            #int1.set(6)
        def Band1_Violet():
            var1.set("7")
            #int1.set(7)
        def Band1_Gray():
            var1.set("8")
            #int1.set(8)
        def Band1_White():
            var1.set("9")
            #int1.set(9)


# ======================================================================================================================
        def Band2_Black():
            var2.set("0")
            #int2.set(0)
        def Band2_Brown():
            var2.set("1")
            #int2.set(1)
        def Band2_Red():
            var2.set("2")
            #int2.set(2)
        def Band2_Orange():
            var2.set("3")
            #int2.set(3)
        def Band2_Yellow():
            var2.set("4")
            #int2.set(4)
        def Band2_Green():
            var2.set("5")
            #int2.set(5)
        def Band2_Blue():
            var2.set("6")
            #int2.set(6)
        def Band2_Violet():
            var2.set("7")
            #int2.set(7)
        def Band2_Gray():
            var2.set("8")
            #int2.set(8)
        def Band2_White():
            var2.set("9")
            #int2.set(9)

# ======================================================================================================================
        def Band3_Black():
            var3.set("1Ω")
            int3.set(1)
        def Band3_Brown():
            var3.set("10Ω")
            int3.set(10)
        def Band3_Red():
            var3.set("100Ω")
            int3.set(100)
        def Band3_Orange():
            var3.set("1K Ω")
            int3.set(1000)
        def Band3_Yellow():
            var3.set("10K Ω")
            int3.set(1000)
        def Band3_Green():
            var3.set("100K Ω")
            int3.set(10000)
        def Band3_Blue():
            var3.set("1M Ω")
            int3.set(100000)
        def Band3_Violet():
            var3.set("10M Ω")
            int3.set(1000000)
        def Band3_Gray():
            var3.set("100M Ω")
            int3.set(10000000)
        def Band3_White():
            var3.set("1G Ω")
            int3.set(100000000)
        def Band3_Gold():
            var3.set("0.1Ω")
            int3.set(0.1)
        def Band3_Silver():
            var3.set("0.01Ω")
            int3.set(0.01)

# ======================================================================================================================

        def Band4_Brown():
            var4.set("±1%")
            str4.set(0.01)
        def Band4_Red():
            var4.set("±2%")
            str4.set(0.02)
        def Band4_Orange():
            var4.set("±0.05%")
            str4.set(0.0005)
        def Band4_Yellow():
            var4.set("±0.02%")
            str4.set(0.0002)
        def Band4_Green():
            var4.set("±0.5%")
            str4.set(0.005)
        def Band4_Blue():
            var4.set("±0.25%")
            str4.set(0.0025)
        def Band4_Violet():
            var4.set("±0.10%")
            str4.set(0.0010)
        def Band4_Gray():
            var4.set("±0.05%")
            str4.set(0.005)
        def Band4_Gold():
            var4.set("±5%")
            str4.set(0.05)
        def Band4_Silver():
            var4.set("±10%")
            str4.set(0.1)
#=======================================================================================================================

        def number_format(num):
            num = float('{:.3g}'.format(num))
            magnitude = 0
            while abs(num) >= 1000:
                magnitude += 1
                num /= 1000.0
            return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'G', 'T'][magnitude])

# =======================================================================================================================
        def CalculateResistor():
            mix = int(var1.get() + var2.get()) * float(int3.get())
            fin = number_format(mix) + "Ω " + var4.get()
            var5.set(fin)
            mincal = mix - (mix * float(str4.get()))
            maxcal = mix + (mix * float(str4.get()))
            var6.set(mincal)
            var7.set(maxcal)




# ======================================================================================================================

        TitleLabel = Label(B4WIN,text="4-Band Resistor Calculator",bg='gray20',fg='white',relief=RIDGE,font=('arial 20 bold')).place(x=65,y=20)

        row1Label = Label(B4WIN,text='1st Band',bg='gray20',fg='white',relief=RIDGE,font=('arial 10 bold')).place(x=60,y=60)
        row2Label = Label(B4WIN, text='2nd Band', bg='gray20', fg='white', relief=RIDGE, font=('arial 10 bold')).place(x=160, y=60)
        row3Label = Label(B4WIN, text='Multiplier', bg='gray20', fg='white', relief=RIDGE, font=('arial 10 bold')).place(x=260, y=60)
        row4Label = Label(B4WIN, text='Tolerance', bg='gray20', fg='white', relief=RIDGE, font=('arial 10 bold')).place(x=360, y=60)

# =============================================================================================================================
        self.blaColor1 = Button(B4WIN,width=10,text='Black(0)',bg='black',fg='white',command=Band1_Black).place(x=50,y=80)
        self.blaColor2 = Button(B4WIN, width=10, text='Black(0)', bg='black', fg='white',command=Band2_Black).place(x=152, y=80)
        self.blaColor3 = Button(B4WIN, width=10, text='Black(1Ω)', bg='black', fg='white',command=Band3_Black).place(x=252, y=80)
        self.blaColor4 = Button(B4WIN, width=10, text='', bg='black', fg='white',state=DISABLED).place(x=355, y=80)
#=============================================================================================================================
        self.broColor1 = Button(B4WIN, width=10, text='Brown(1)', bg='saddle brown', fg='white',command=Band1_Brown).place(x=50, y=110)
        self.broColor2 = Button(B4WIN, width=10, text='Brown(1)', bg='saddle brown', fg='white',command=Band2_Brown).place(x=152, y=110)
        self.broColor3 = Button(B4WIN, width=10, text='Brown(10Ω)', bg='saddle brown', fg='white',command=Band3_Brown).place(x=252, y=110)
        self.broColor4 = Button(B4WIN, width=10, text='Brown(±1%)', bg='saddle brown', fg='white',command=Band4_Brown).place(x=355, y=110)
#=============================================================================================================================
        self.redColor1 = Button(B4WIN,width=10,text='Red(2)',bg='red',fg='black',command=Band1_Red).place(x=50,y=140)
        self.redColor2 = Button(B4WIN, width=10, text='Red(2)', bg='red', fg='black',command=Band2_Red).place(x=152, y=140)
        self.redColor3 = Button(B4WIN, width=10, text='Red(100Ω)', bg='red', fg='black',command=Band3_Red).place(x=252, y=140)
        self.redColor4 = Button(B4WIN, width=10, text='Red(±2%)', bg='red', fg='black',command=Band4_Red).place(x=355, y=140)
# =============================================================================================================================
        self.ongColor1 = Button(B4WIN,width=10,text='Orange(3)',bg='orange',fg='black',command=Band1_Orange).place(x=50,y=170)
        self.ongColor2 = Button(B4WIN, width=10, text='Orange(3)', bg='orange', fg='black',command=Band2_Orange).place(x=152, y=170)
        self.ongColor3 = Button(B4WIN, width=10, text='Orange(1KΩ)', bg='orange', fg='black',command=Band3_Orange).place(x=252, y=170)
        self.ongColor4 = Button(B4WIN, width=10, text='Oran(±0.05%)', bg='orange', fg='black',command=Band4_Orange).place(x=355, y=170)
# =============================================================================================================================
        self.yelColor1 = Button(B4WIN,width=10,text='Yellow(4)',bg='yellow',fg='black',command=Band1_Yellow).place(x=50,y=200)
        self.yelColor2 = Button(B4WIN, width=10, text='Yellow(4)', bg='yellow', fg='black',command=Band2_Yellow).place(x=152, y=200)
        self.yelColor3 = Button(B4WIN, width=10, text='Yellow(10KΩ)', bg='yellow', fg='black',command=Band3_Yellow).place(x=252, y=200)
        self.yelColor4 = Button(B4WIN, width=10, text='Yello(±0.02%)', bg='yellow', fg='black',command=Band4_Yellow).place(x=355, y=200)
# =============================================================================================================================
        self.greColor1 = Button(B4WIN, width=10, text='Green(5)', bg='forest green', fg='black',command=Band1_Green).place(x=50,y=230)
        self.greColor2 = Button(B4WIN, width=10, text='Green(5)', bg='forest green', fg='black',command=Band2_Green).place(x=152, y=230)
        self.greColor3 = Button(B4WIN, width=10, text='Green(100KΩ)', bg='forest green', fg='black',command=Band3_Green).place(x=252, y=230)
        self.greColor4 = Button(B4WIN, width=10, text='Green(±0.5%)', bg='forest green', fg='black',command=Band4_Green).place(x=355, y=230)
# =============================================================================================================================
        self.bluColor1 = Button(B4WIN, width=10, text='Blue(6)', bg='blue', fg='white',command=Band1_Blue).place(x=50,y=260)
        self.bluColor2 = Button(B4WIN, width=10, text='Blue(6)', bg='blue', fg='white',command=Band2_Blue).place(x=152, y=260)
        self.bluColor3 = Button(B4WIN, width=10, text='Blue(1MΩ)', bg='blue', fg='white',command=Band3_Blue).place(x=252, y=260)
        self.bluColor4 = Button(B4WIN, width=10, text='Blue(±0.25%)', bg='blue', fg='white',command=Band4_Blue).place(x=355, y=260)
# =============================================================================================================================
        self.vioColor1 = Button(B4WIN, width=10, text='Violet(7)', bg='dark violet', fg='white',command=Band1_Violet).place(x=50,y=290)
        self.vioColor2 = Button(B4WIN, width=10, text='Violet(7)', bg='dark violet', fg='white',command=Band2_Violet).place(x=152, y=290)
        self.vioColor3 = Button(B4WIN, width=10, text='Violet(10MΩ)', bg='dark violet', fg='white',command=Band3_Violet).place(x=252, y=290)
        self.vioColor4 = Button(B4WIN, width=10, text='Violet(±0.10%)', bg='dark violet', fg='white',command=Band4_Violet).place(x=355, y=290)
# =============================================================================================================================
        self.graColor1 = Button(B4WIN, width=10, text='Gray(8)', bg='slate gray', fg='white',command=Band1_Gray).place(x=50, y=320)
        self.graColor2 = Button(B4WIN, width=10, text='Gray(8)', bg='slate gray', fg='white',command=Band2_Gray).place(x=152, y=320)
        self.graColor3 = Button(B4WIN, width=10, text='Gray(100MΩ)', bg='slate gray', fg='white',command=Band3_Gray).place(x=252,y=320)
        self.graColor4 = Button(B4WIN, width=10, text='Gray(±0.05%)', bg='slate gray', fg='white',command=Band4_Gray).place(x=355,y=320)
# =============================================================================================================================
        self.whiColor1 = Button(B4WIN, width=10, text='White(9)', bg='white', fg='black',command=Band1_White).place(x=50, y=350)
        self.whiColor2 = Button(B4WIN, width=10, text='White(9)', bg='white', fg='black',command=Band2_White).place(x=152, y=350)
        self.whiColor3 = Button(B4WIN, width=10, text='White(1GΩ)', bg='white', fg='black',command=Band3_White).place(x=252, y=350)
        self.whiColor4 = Button(B4WIN, width=10, text='', bg='white', fg='black',state=DISABLED).place(x=355, y=350)
# =============================================================================================================================
        self.golColor1 = Button(B4WIN, width=10, text='', bg='gold', fg='black',state=DISABLED).place(x=50, y=380)
        self.golColor2 = Button(B4WIN, width=10, text='', bg='gold', fg='black',state=DISABLED).place(x=152, y=380)
        self.golColor3 = Button(B4WIN, width=10, text='Gold(0.1Ω)', bg='gold', fg='black',command=Band3_Gold).place(x=252, y=380)
        self.golColor4 = Button(B4WIN, width=10, text='Gold(±5%)', bg='gold', fg='black',command=Band4_Gold).place(x=355, y=380)
# =============================================================================================================================
        self.silColor1 = Button(B4WIN, width=10, text='', bg='silver', fg='black',state=DISABLED).place(x=50, y=410)
        self.silColor2 = Button(B4WIN, width=10, text='', bg='silver', fg='black',state=DISABLED).place(x=152, y=410)
        self.silColor3 = Button(B4WIN, width=10, text='Silver(0.01Ω)', bg='silver', fg='black',command=Band3_Silver).place(x=252, y=410)
        self.silColor4 = Button(B4WIN, width=10, text='Silver(±10%)', bg='silver', fg='black',command=Band4_Silver).place(x=355, y=410)
# ===============================================Indicator Frame===============================================================
        self.txtFirst = Entry(B4WIN,width=8,font=(15),textvariable=var1,state=DISABLED).place(x=50, y=450)
        self.txtSecond = Entry(B4WIN, width=8,font=(15),textvariable=var2,state=DISABLED).place(x=153, y=450)
        self.txtMultiply = Entry(B4WIN, width=8,font=(15),textvariable=var3,state=DISABLED).place(x=253, y=450)
        self.txtTolerance = Entry(B4WIN, width=8,font=(15),textvariable=var4,state=DISABLED).place(x=355, y=450)
        self.txtResistorValue = Entry(B4WIN,width=19,font=(15),state=DISABLED,textvariable=var5).place(x=160, y=550)
        self.txtMinRange = Entry(B4WIN,width=12,font=(15),state=DISABLED,textvariable=var6).place(x=75, y=610)
        self.txtMaxRange = Entry(B4WIN,width=12,font=(15),state=DISABLED,textvariable=var7).place(x=290, y=610)
# ============================================================================================================================
        self.lblResistorValue = Label(text='Resistor Value',bg='gray20',fg='white',relief=RIDGE,font=('arial 12 bold')).place(x=190,y=525)
        self.lblMinRange = Label(text='Min Range',bg='gray20',fg='white',relief=RIDGE,font=('arial 12 bold')).place(x=90, y=580)
        self.lblMaxRange = Label(text='Max Range',bg='gray20',fg='white',relief=RIDGE,font=('arial 12 bold')).place(x=300, y=580)
# =============================================================================================================================
        btnCalculate = Button(B4WIN,text="Calculate",font=(15), width=12,bg='black',fg='white',relief=FLAT,command=CalculateResistor).place(x=190, y=480)
        btnClear = Button(B4WIN,text="Clear",bg='black',fg='white', width=12,relief=FLAT,command=iClear).place(x=35, y=650)
        btnExit = Button(B4WIN, text="Exit", bg='black', fg='white', width=12,relief=FLAT,command=iExit).place(x=355, y=650)

if __name__ == '__main__':
    B4WIN = Tk()
    application = resistor(B4WIN)
    B4WIN.mainloop()



