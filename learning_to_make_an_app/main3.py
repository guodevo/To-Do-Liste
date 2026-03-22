import tkinter as tk
import os


class ToDoApp:

    def __init__(self, window):
        self.window = window
        self.window.title("ToDoApp")
        
        
        self.frame_for_button = tk.Frame(self.window)
        self.frame_for_button.pack(side="bottom", pady=20, padx=10)


        self.top_frame_for_tasks = tk.Frame(self.window,)
        self.top_frame_for_tasks.pack(side= "top", pady=5, fill= "both", expand=True,)
       
        self.button()
        self.delete_1_task_button()
        self.delete_all_button()
        self.display_the_Task = tk.Listbox(self.top_frame_for_tasks,)
        with open("learning_to_make_an_app/data.txt", 'r') as data:
            display_saved_data = data.readlines()
        for task in display_saved_data:
            self.display_the_Task.insert(tk.END, task)
        self.display_the_Task.pack(fill="x",)
        self.entry_open = False
        self.entry = None




    def delete_1_task_button(self):
        self.delete_1_task_button = tk.Button(self.frame_for_button, fg='blue', bg="green", font=("Ariel", 20), text= "Delete clicked task", command=self.delete_selected_task)
        self.delete_1_task_button.grid(row = 0, column = 1, padx= 50)

    def delete_selected_task(self):
        selected = self.display_the_Task.curselection()
        if selected:
            
            index = selected[0]
            task_to_be_deleted = self.display_the_Task.get(index)
            print(task_to_be_deleted)
            with open("learning_to_make_an_app/data.txt", 'r') as data:
               tasks = []
               for task in data:
                   tasks.append(task.strip())
            if task_to_be_deleted in tasks:
                   tasks.remove(task_to_be_deleted)
                   with open("learning_to_make_an_app/data.txt", 'w') as file:
                        for task in tasks:
                            file.write(task + "\n")
                       
            self.display_the_Task.delete(selected[0])

                
    
    


    def button(self):
        self.button = tk.Button(self.frame_for_button, font=("Ariel", 30), text="Click to add new task", command=self.add_task)
        
        self.button.grid(row= 0, column=0)

    def delete_all_button(self):
        self.delete_all_button = tk.Button(self.frame_for_button, text="delete all", font=("Ariel", 15),bg="red", fg="blue", padx=5, command= self.delete_all)
        self.delete_all_button.grid(row= 0, column = 2, padx = 5 )

    def delete_all(self):
        with open("learning_to_make_an_app/data.txt", 'w'):
            pass
        self.display_the_Task.delete(0, tk.END)

    def save_task(self, ):
        with open("learning_to_make_an_app/data.txt", 'a') as file:
            user_input = self.entry.get()
            if user_input != "":
                file.write(user_input + "\n")
                self.entry.delete(0, tk.END)
    
    def display_task(self,):
            with open("learning_to_make_an_app/data.txt", 'r') as data:
                tasks = data.readlines()
                self.display_the_Task.delete(0, tk.END)
                for task in tasks:
                    self.display_the_Task.insert(tk.END, task.strip())
                    print(task.strip())
        
    def on_click(self, event):
        self.save_task()
        self.display_task()
        

    
    def add_task(self):
        
        if self.entry_open == False:
            self.entry = tk.Entry(self.window, font=("Ariel", 30), fg="black", bg="grey")
            self.entry.bind("<Return>", self.on_click)
            
            self.entry.pack()
            self.entry_open = True
        else:
            self.entry.destroy()
            self.entry_open = False
            self.entry = None
        
        



window = tk.Tk()
app = ToDoApp(window)
window.mainloop()