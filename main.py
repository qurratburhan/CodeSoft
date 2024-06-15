
import customtkinter as c
from tkinter import messagebox, Listbox

class App:
    def __init__(self, gry):
        self.gry = gry
        self.gry.title("To-Do List")
        self.tasks = []

        self.frame = c.CTkFrame(master=gry)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.task_entry = c.CTkEntry(master=self.frame, placeholder_text="Enter a new task",bg_color="white",fg_color= "black")
        self.task_entry.pack(pady=10)
        self.add_button = c.CTkButton(master=self.frame, text="Add Task", command=self.add_task, fg_color="#AB4E52", text_color="white")
        self.add_button.pack(pady=8)

        self.task_listbox = Listbox(master=self.frame, bg="white", fg="black", )
        self.task_listbox.pack(pady=10, fill="both", expand=True)


        self.update_button = c.CTkButton(master=self.frame, text="Update Task", command=self.update_task, fg_color="#905D5D", text_color="white")
        self.update_button.pack(pady=0, side="left")

        self.delete_button = c.CTkButton(master=self.frame, text="Delete Task", command=self.delete_task, fg_color="#905D5D", text_color="white")
        self.delete_button.pack(pady=3, side="right")

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert("end", task)
            self.task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Trigger", "enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Trigger", "select a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks[selected_task_index] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.task_entry.delete(0, "end")
            else:
                messagebox.showwarning("Trigger", "Tasknotentered.")
        except IndexError:
            messagebox.showwarning("Trigger", "Task not selected.")

if __name__ == "__main__":
    box = c.CTk()
    app = App(box)
    box.mainloop()
