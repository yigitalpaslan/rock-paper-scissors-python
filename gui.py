import tkinter as tk
from tkinter import ttk
from tkinter import *
from logic import RandomChoice
from tkinter import messagebox
import sys 
import pygame


class App(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.minsize(750,600)
        self.resizable(False,False)
        self.title("Rock Scissor Paper")
        self.iconbitmap("favicon.ico")
        pygame.mixer.init()
        pygame.mixer.music.load("assests\music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.countdown_sound = pygame.mixer.Sound("assests\\arcade_countdown.mp3")
        self.countdown_sound.set_volume(0.5)
        self.choose_sound = pygame.mixer.Sound("assests\\u_s026io00zm-beep-401570.mp3")
        self.choose_sound.set_volume(0.2)
        self.win_sound = pygame.mixer.Sound("assests\\cartoon-music-game-sfx-arcade-game-victory-chime-489761.mp3")
        self.win_sound.set_volume(0.7)
        self.lose_sound = pygame.mixer.Sound("assests\\lose_sound.mp3")
        self.lose_sound.set_volume(0.8)
        self.draw_sound = pygame.mixer.Sound("assests\\draw_sound.mp3")
        self.draw_sound.set_volume(0.7)
        self.rock_image = PhotoImage(file=r"assests\rock _image.png").subsample(3,3)
        self.paper_image = PhotoImage(file=r"assests\490-4906131_rock-paper-scissors-.png").subsample(3,3)
        self.sci_image = PhotoImage(file=r"assests\sciscp (1).png").subsample(3,3)
        self.logic = RandomChoice()
        self.app_window()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.challenge1_done= False
        self.timeout_id = None
        
    def app_window(self): 
        self.style = ttk.Style()
        self.style.configure("gray.TFrame",background="#0c192e")
        self.main_frame = ttk.Frame(self,style= "gray.TFrame",width=750,height=200)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(fill="both")
        self.result_label = ttk.Label(self.main_frame, text="Click start to play !",font=("Comic Sans MS",25),background="#0c192e",foreground="lightblue")
        self.result_label.pack(expand=True)

        self.selection_frame = ttk.Frame(self,style= "gray.TFrame",width=750,height=200)
        self.selection_frame.pack_propagate(False)
        self.selection_frame.pack(side="bottom")

        self.counter_frame = ttk.Frame(self, style="gray.TFrame",width=750, height=200)
        self.counter_frame.pack_propagate(False)
        self.counter_frame.pack(side="top")
        self.counter_label = ttk.Label(self.counter_frame,text=f"Your Score: {self.logic.user_counter}\nComputer's Score: {self.logic.comp_counter}\nDraw: {self.logic.draw_counter}",
                                       font=("Comic Sans MS",12),background="#0c192e",foreground="lightblue")
        self.counter_label.pack(expand=True)
        self.challenge_label = ttk.Label(self.main_frame,text=f"{6*" "}Challenge\n{22*"-"}\n{" "}Achieve 10 win !{6*" "}",font=("Comic Sans MS",10),background="#0c192e",foreground="lightgreen")
        self.challenge_label.pack(anchor="ne")

        self.rock = tk.Button(self.selection_frame, text="Rock", height=100, width=100,state="disabled",command= lambda: self.game("Rock") ) #ROCK
        self.rock.config(image=self.rock_image)
        self.rock.pack(side="left",padx=50,pady=50)
        self.paper = tk.Button(self.selection_frame, height=100 ,width=100,state="disabled", command= lambda: self.game("Paper")) #paper
        self.paper.config(image=self.paper_image)
        self.paper.pack(side="left",padx=120,pady=50)
        self.sci = tk.Button(self.selection_frame, height=100, width= 100,state="disabled", command= lambda: self.game("Scissor")) # SCİSSOR
        self.sci.config(image=self.sci_image)
        self.sci.pack(side="right",padx=50,pady=50)
        self.start_button = tk.Button(self.main_frame,text=" S T A R T ",font=("Times New Roman",12,"bold"),bg="#93c0cc",command=self.start_game)
        self.start_button.pack(expand=True)
        self.mute_button = tk.Button(self.main_frame, state= "normal", command= self.mute_music)
        self.mute_button.config(text="Mute",font=("Comic Sans MS",10,"bold"),bg="#93c0cc")
        self.mute_button.place(x=15,y=15)

    def start_game(self):
        self.start_button.config(state="disabled")
        self.result_label.config(font=("Comic Sans MC",25))
        self.rock.config(state="disabled")
        self.paper.config(state="disabled")
        self.sci.config(state="disabled")
        self.timer_loop(3)
    
    def timer_loop(self,time):
        if time > 0:
            self.result_label.config(text=str(time),font=("Comic Sans MS",25))
            self.after(1000,self.timer_loop,time-1)      
            self.countdown_sound.play()

        else:
            time_text= "C H O O S E !"
            self.result_label.config(text=time_text,font=("Comic Sans MS",25))
            self.rock.config(state="normal")
            self.paper.config(state="normal")
            self.sci.config(state="normal")
            self.choose_sound.play()
            self.timeout_id = self.after(2000,self.timeout_func)

    def timeout_func(self):
        time_error = messagebox.showwarning(title="F A I L",message="You haven't choose anything :(\nPlease try again !")
        self.result_label.config(text="Click start to play !",font=("Comic Sans MS",25))
        self.start_button.config(state="normal")
        self.rock.config(state="disabled")
        self.paper.config(state="disabled")
        self.sci.config(state="disabled")
        
    def game(self,users_choice):
        comp_choice = self.logic.get_computer_choice()
        result = self.logic.compare(users_choice,comp_choice)
        if result == "You Won :)":
            self.win_sound.play()
        elif result == "You Lose :(":
            self.lose_sound.play()
        elif result == "Draw":
            self.draw_sound.play()
        new_text = f"Computer: {comp_choice} | Result: {result}"
        self.result_label.config(font=("Comic Sans MS",20))
        self.result_label.config(text=new_text)
        new_score = f"Your Score: {self.logic.user_counter}\nComputer's Score: {self.logic.comp_counter}\nDraw: {self.logic.draw_counter}"
        self.counter_label.config(text=new_score)
        self.rock.config(state="disabled")
        self.paper.config(state="disabled")
        self.sci.config(state="disabled")
        self.start_button.config(state="normal")
        if self.timeout_id is not None:
            self.after_cancel(self.timeout_id)
            self.timeout_id = None
        self.challenge_success1()

    def challenge_success1(self):
            if self.challenge1_done or self.logic.user_counter!=10:
                return
            success_box = messagebox.showinfo(title="C O N G R A T İ L A T İ O N S !",message="You've complete the challenge :)")
            change_challenge = f"{6*" "}Challenge\n{22*"-"}\n~Achieve 30 win !{6*" "}"
            self.challenge_label.config(text=change_challenge)
            self.challenge1_done = True
    def mute_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.mute_button.config(text="Unmute")
        else:    
            pygame.mixer.music.unpause()
            self.mute_button.config(text="Mute")
    
    def close(self):
        self.destroy()
        sys.exit()