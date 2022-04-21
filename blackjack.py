from tkinter.font import Font
from tkinter import *
from PIL import ImageTk, Image
from korta import *

zetonai = 1000 #zetonu global variable

class Langas:
    def __init__(self, master):
        self.master = master

        font1 = Font(family='Iosevka Extended',
                    size=22,
                    weight='bold')

        self.img = Image.open('fonas.png')
        self.img_res = self.img.resize((768, 428), Image.Resampling.LANCZOS)
        self.fonas = ImageTk.PhotoImage(self.img_res)

        self.canvas = Canvas(master, width=768, height=428) #kuriamas canvas
        self.canvas.pack(fill='both', expand=True)

        self.canvas.create_image(0, 0, image=self.fonas, anchor='nw')

        self.canvas.create_text(100, 50, text='BLACKJACK \ncard game', font=font1)

        self.new_game = Button(self.canvas, text='New Game', command=self.loadlangas2, borderwidth=0, highlightthickness=0, bg='white') #kuriami mygtukai
        self.quit = Button(self.canvas, text='Quit', command=self.close, borderwidth=0, highlightthickness=0)

        self.new_game_canvas = self.canvas.create_window(50, 200, 
                                            anchor='nw', 
                                            window=self.new_game) #mygtukas iterpiamas i Canvas
        self.quit_canvas = self.canvas.create_window(50, 300, 
                                            anchor='nw', 
                                            window=self.quit)
    
    def loadlangas2(self):
        self.top = Toplevel()
        self.top.geometry('400x600')
        self.top.configure(bg='#00B401')
        self.top.title("Game")
        self.app = Langas2(self.top)

    
    def close(self):
        quit()


class Langas2(Langas):
    def __init__(self, master):

        self.master = master

        self.font1 = Font(family='Iosevka Extended',
                    size=22,
                    weight='bold')
        self.font2 = Font(family='Iosevka Extended',
                    size=18,
                    weight='bold')
        self.font1 = Font(family='Iosevka Extended',
                    size=22,
                    weight='bold')
        self.font3 = Font(family='Iosevka Extended',
                    size=16,
                    weight='bold')
        #krupje labelframe
        self.krupje_frame = LabelFrame(master, bg='#00B401', borderwidth=0)
        self.krupje_frame.pack(fill='x', expand=YES, padx=20)
        self.krupje_img = Image.open('krupje.png')
        self.krupje = ImageTk.PhotoImage(self.krupje_img)

        #krupje pav., pav. ir taskai
        self.krupje_label = Label(self.krupje_frame, image=self.krupje, borderwidth=0)
        self.krupje_label.pack(padx=10, pady=10)
        self.dalintojas_label = Label(self.krupje_frame, text='Dealer', font=self.font1, bg='#00B401')
        self.dalintojas_label.pack(padx=10, pady=10)
        self.pradzios_kortos = pradeti()
        self.dalintojo_taskai = self.pradzios_kortos[1]
        self.zaidejo_taskai = self.pradzios_kortos[4]

        # krupje kortu labelframe
        self.dalint_kort_label = LabelFrame(master, bg='#00B401', borderwidth=0)
        self.dalint_kort_label.pack(fill='x', expand=YES, padx=20)

        # statymas
        self.bet_frame = LabelFrame(master, bg='#00B401', borderwidth=0)
        self.bet_frame.pack(fill='x', expand=YES, padx=20)
        self.bet_label = Label(self.bet_frame, text='Bet:', font=self.font2, bg='#00B401')
        self.bet_label.grid(row=0, column=0, padx=10, pady=10)
        self.bet_entry = Entry(self.bet_frame, bg='#00B401', width=5)
        self.bet_entry.grid(row=0, column=2, pady=10)

        #zaidejo kortu labelframe
        self.zaid_kort_label = LabelFrame(master, bg='#00B401', borderwidth=0)
        self.zaid_kort_label.pack(fill='x', expand=YES, padx=20)

        #dalintojo taskai rodymas
        self.dalintojas_points = Label(self.krupje_frame, text=f'Points: {self.dalintojo_taskai}', font=self.font2, bg='#00B401')
        self.dalintojas_points.pack(padx=10, pady=10)

        #zaidejo labelframe
        self.zaidejas_frame = LabelFrame(master, bg='#00B401', borderwidth=0)
        self.zaidejas_frame.pack(fill='x', expand=YES, padx=20)

        #zaidejo taskai, pav.
        self.zaidejas_points = Label(self.zaidejas_frame, text=f'Points: {self.zaidejo_taskai}', font=self.font2, bg='#00B401')
        self.zaidejas_points.grid(row=0, column=3, padx=10, pady=10)
        self.zaidejas_label = Label(self.zaidejas_frame, text='Player', font=self.font1, bg='#00B401')
        self.zaidejas_label.grid(row=1, column=2, padx=10, pady=10)

        #mygtukai
        self.hit = Button(self.zaidejas_frame, text='HIT', command=self.testi, font=self.font3, borderwidth=0, highlightthickness=0)
        self.hit.grid(row=1, column=3, padx=10, pady=10)
        self.stand = Button(self.zaidejas_frame, text='STAND', command=self.stoti, font=self.font3, borderwidth=0, highlightthickness=0)
        self.stand.grid(row=2, column=3, padx=10, pady=10)

        #zaidejo zetonai
        self.zet_img = Image.open('chips.png')
        self.zet = ImageTk.PhotoImage(self.zet_img)
        self.zet_pav_label = Label(self.zaidejas_frame, image=self.zet, bg='#00B401')
        self.zet_pav_label.grid(row=2, column=0)
        self.zaid_zet = Label(self.zaidejas_frame, text=zetonai, bg='#00B401')
        self.zaid_zet.grid(row=2, column=1)

        #dalintojo korta
        self.image1 = Image.open(f"./cards/{self.pradzios_kortos[0]}.png")
        self.korta1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(self.dalint_kort_label, image=self.korta1, borderwidth=0)
        self.label1.image = self.korta1 #priskirimas, kad kortos nedingtu nuo lango...
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        #zaidejo 2 kortos
        self.image2 = Image.open(f"./cards/{self.pradzios_kortos[2]}.png")
        self.korta2 = ImageTk.PhotoImage(self.image2)
        self.label2 = Label(self.zaid_kort_label, image=self.korta2, borderwidth=0)
        self.label2.image = self.korta2
        self.label2.grid(row=0, column=0, padx=10, pady=10)
        self.image3 = Image.open(f"./cards/{self.pradzios_kortos[3]}.png")
        self.korta3 = ImageTk.PhotoImage(self.image3)
        self.label3 = Label(self.zaid_kort_label, image=self.korta3, borderwidth=0)
        self.label3.image = self.korta3
        self.label3.grid(row=0, column=1, padx=10, pady=10)

        master.protocol("WM_DELETE_WINDOW", kalade_default())
    
    
    def bet(self):
        if self.lost_label.cget('text') == 'LOST':
            statymas = int(self.bet_entry.get())
            self.bet_entry.delete(0, END)
            skirtumas = int(self.zaid_zet.cget('text')) - statymas
            if skirtumas > 0:
                self.zaid_zet.config(text=f'{skirtumas}')
                global zetonai
                zetonai = skirtumas
                self.zaid_zet.config(text=zetonai)

            else:
                self.lost_label.config(text='Game Over')
                zetonai = 0
                self.zaid_zet.config(text=zetonai)

        if self.lost_label.cget('text') == 'WIN':
            statymas = int(self.bet_entry.get())
            self.bet_entry.delete(0, END)
            skirtumas = int(self.zaid_zet.cget('text')) + statymas
            self.zaid_zet.config(text=f'{skirtumas}')
            zetonai = skirtumas
            self.zaid_zet.config(text=zetonai)

    def testi(self):
        self.hit['command'] = self.testi_toliau
        if self.bet_entry.get() == '' or self.bet_entry.get() == 'Need to bet...':
            return self.bet_entry.insert(0, 'Need to bet...')
        if float(self.bet_entry.get()).is_integer() == True:
            self.zaidejas = korta()
            self.image = Image.open(f"./cards/{self.zaidejas[1]}.png")
            self.korta = ImageTk.PhotoImage(self.image)
            self.korta_label = Label(self.zaid_kort_label, image=self.korta, borderwidth=0)
            self.korta_label.image = self.korta
            self.korta_label.grid(row=0, column=2, pady=10, padx=10)
            self.zaidejo_taskai += self.zaidejas[2]
            self.zaidejas_points['text'] = f'Points: {self.zaidejo_taskai}'
            if self.zaidejo_taskai > 21:
                self.lost_label = Label(self.bet_frame, text='LOST', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.bet()
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)
    
    def testi_toliau(self):
        self.hit['command'] = self.testi_toliau2
        if self.bet_entry.get() == '' or self.bet_entry.get() == 'Need to bet...':
            return self.bet_entry.insert(0, 'Need to bet...')
        if float(self.bet_entry.get()).is_integer() == True:
            self.zaidejas1 = korta()
            self.image1 = Image.open(f"./cards/{self.zaidejas1[1]}.png")
            self.korta1 = ImageTk.PhotoImage(self.image1)
            self.korta_label1 = Label(self.zaid_kort_label, image=self.korta1, borderwidth=0)
            self.korta_label1.image = self.korta1
            self.korta_label1.grid(row=0, column=3, pady=10, padx=10)
            self.zaidejo_taskai += self.zaidejas1[2]
            self.zaidejas_points['text'] = f'Points: {self.zaidejo_taskai}'
            if self.zaidejo_taskai > 21:
                self.lost_label = Label(self.bet_frame, text='LOST', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.bet()
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)

    def testi_toliau2(self):
        if self.bet_entry.get() == '' or self.bet_entry.get() == 'Need to bet...':
            return self.bet_entry.insert(0, 'Need to bet...')
        if float(self.bet_entry.get()).is_integer() == True:
            self.zaidejas2 = korta()
            self.image2 = Image.open(f"./cards/{self.zaidejas2[1]}.png")
            self.korta2 = ImageTk.PhotoImage(self.image2)
            self.korta_label2 = Label(self.zaid_kort_label, image=self.korta2, borderwidth=0)
            self.korta_label2.image = self.korta2
            self.korta_label2.grid(row=0, column=4, pady=10, padx=10)
            self.zaidejo_taskai += self.zaidejas1[2]
            self.zaidejas_points['text'] = f'Points: {self.zaidejo_taskai}'
            if self.zaidejo_taskai > 21:
                self.lost_label = Label(self.bet_frame, text='LOST', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.bet()
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)
            
    def stoti(self):
        if self.bet_entry.get() == '' or self.bet_entry.get() == 'Need to bet...':
            return self.bet_entry.insert(0, 'Need to bet...')
        if float(self.bet_entry.get()).is_integer() == True:
            self.krupje_korta = korta()
            self.image = Image.open(f"./cards/{self.krupje_korta[1]}.png")
            self.korta = ImageTk.PhotoImage(self.image)
            self.korta_label = Label(self.dalint_kort_label, image=self.korta, borderwidth=0)
            self.korta_label.image = self.korta
            self.korta_label.grid(row=0, column=1, padx=10, pady=10)
            self.dalintojo_taskai += self.krupje_korta[2]
            self.dalintojas_points['text'] = f'Points: {self.dalintojo_taskai}'

            if self.dalintojo_taskai > self.zaidejo_taskai and self.dalintojo_taskai < 21:
                self.lost_label = Label(self.bet_frame, text='LOST', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.bet()
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)


            elif self.dalintojo_taskai <= 16:
                self.krupje_korta1 = korta()
                self.image1 = Image.open(f"./cards/{self.krupje_korta1[1]}.png")
                self.korta1 = ImageTk.PhotoImage(self.image1)
                self.korta_label1 = Label(self.dalint_kort_label, image=self.korta1, borderwidth=0)
                self.korta_label1.image = self.korta1
                self.korta_label1.grid(row=0, column=2, padx=10, pady=10)
                self.dalintojo_taskai += self.krupje_korta1[2]
                self.dalintojas_points['text'] = f'Points: {self.dalintojo_taskai}'

                if self.dalintojo_taskai > 21 or self.dalintojo_taskai < self.zaidejo_taskai:
                    self.lost_label = Label(self.bet_frame, text='WIN', font=self.font1, bg='#00B401')
                    self.lost_label.grid(row=0, column=1)
                    self.bet()
                    self.stand.grid_forget() # isimam stand mygtuka
                    self.hit.grid_forget()
                    self.bet_entry.grid_forget()
                    self.bet_label.grid_forget()
                    self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                    self.play.grid(row=1, column=3, padx=10, pady=10)


                elif 17 < self.dalintojo_taskai <= 21 and self.dalintojo_taskai > self.zaidejo_taskai:
                    self.lost_label = Label(self.bet_frame, text='LOST', font=self.font1, bg='#00B401')
                    self.lost_label.grid(row=0, column=1)
                    self.bet()
                    self.stand.grid_forget() # isimam stand mygtuka
                    self.hit.grid_forget()
                    self.bet_entry.grid_forget()
                    self.bet_label.grid_forget()
                    self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                    self.play.grid(row=1, column=3, padx=10, pady=10)


            elif 17 < self.dalintojo_taskai <= 21 and self.dalintojo_taskai > self.zaidejo_taskai:
                self.lost_label = Label(self.bet_frame, text='LOST', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.bet()
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)
                

            elif self.dalintojo_taskai < self.zaidejo_taskai or self.dalintojo_taskai > 21:
                self.lost_label = Label(self.bet_frame, text='WIN', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.bet()
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)
                
            elif self.dalintojo_taskai == self.zaidejo_taskai:
                self.lost_label = Label(self.bet_frame, text='DRAW', font=self.font1, bg='#00B401')
                self.lost_label.grid(row=0, column=1)
                self.stand.grid_forget() # isimam stand mygtuka
                self.hit.grid_forget()
                self.bet_entry.grid_forget()
                self.bet_label.grid_forget()
                self.play = Button(self.zaidejas_frame, text='Play Again', command=self.exit, font=self.font3, borderwidth=0, highlightthickness=0)
                self.play.grid(row=1, column=3, padx=10, pady=10)
        
    def exit(self):
        if self.lost_label.cget('text') == 'Game Over':
            global zetonai
            zetonai = 1000
            self.master.destroy()
            Langas.loadlangas2(self)
        else:
            self.master.destroy()
            Langas.loadlangas2(self)

langas = Tk()
app = Langas(langas)
langas.geometry('768x428')
langas.title('BlackJack')

langas.mainloop()