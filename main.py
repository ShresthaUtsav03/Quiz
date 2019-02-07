


from tkinter import *
from tkinter import messagebox #gui of box 
import json
import random


class ProgramGUI:

    def __init__(self,master):
        
        self.master = master
        master.title("Quizle")
        master.minsize(width=400,height=150)
        frame = Frame(master)
        frame.pack()
       
        try:
            with open('data.txt','r') as data_file:
                self.data = json.load(data_file)
        except:
            print("Missing/Invalid file")
            master.destroy()
            return    

        if len(self.data)<5:
            messagebox.showerror("Error","Insufficient number of questions")
            master.destroy()
            return
       
        self.user_score = 0
        self.no_of_question_answered = 0
        self.correct_question = 0
        self.instance = 0
        self.diff_level_value = 0

        self.diifficulty_level = Label(frame)
        self.diifficulty_level.grid(row=1,columnspan=2,padx=20,pady=10)

        self.question = Label(frame)
        self.question.grid(row=2,columnspan=2,padx=20,pady=10)

        self.question_entry = Entry(frame)
        self.question_entry.grid(row=3)
        
        self.button = Button(frame,text="Submit Answer",command=self.checkAnswer)
        self.button.grid(row=3,column=1)
    
        self.question_status = Label(frame)
        self.question_status.grid(row=4,columnspan=2,padx=20,pady=10)

        self.loadQuestion()



       
    def loadQuestion(self):
        
        self.question_entry.focus_set()
        if self.instance == 0:
            
            self.current_question_set = random.sample(self.data,5)
        
        question = random.choice(self.current_question_set)
            
        self.current_question = question['question']
        self.diff_level_value = int(question['diff_level'])

        if(int(question['diff_level'])>=4):

            self.diifficulty_level.grid(row=1,columnspan=2,padx=20,pady=10)

            self.diifficulty_level.config(text="This is a hard one - good luck!",fg="blue")
        else:
            self.diifficulty_level.grid_forget()
            
        self.question.config(text=self.current_question)
        self.question_status.config(text="%s/%s questions answered correctly"%(self.correct_question,self.no_of_question_answered))
        self.question_answer  = question['answer']
        
        self.current_question_set.remove(question)
        
        print(self.current_question_set)

    def checkAnswer(self):
        
        self.no_of_question_answered += 1
        if type(self.question_entry.get()) == str:
            user_answer = str(self.question_entry.get()).lower()
        else:
            user_answer = self.question_entry.get()

        if user_answer in self.question_answer:
            self.correct_question +=1
            self.user_score +=self.diff_level_value*2
            messagebox.showwarning("Correct","You are correct!")
        else:
            messagebox.showerror("Incorrect","Sorry,that was incorrect!")
        
        print('ques',self.no_of_question_answered)
        if self.no_of_question_answered == 5:
            print('yo:',self.no_of_question_answered)
            messagebox.showwarning("Final Score","Game Over \n Final Score: %s \n\n Thanks for playing" %(self.user_score))
            self.master.destroy()
        else:
            self.instance +=1
            self.question_entry.delete(0, 'end')
            self.loadQuestion()



#addtional code
            
root = Tk()
gui = ProgramGUI(root)
root.mainloop()
