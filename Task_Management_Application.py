"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
StudentId: 151630594
Name:      Najmeh Akbari
Email:     najmeh.akbari@tuni.fi
"""

"""
The given code is a Task Manager application implemented.
It provides a GUI for managing tasks with options for subject, owner, customer, and deadline.
Users can add tasks, view all tasks, and specify actions for each task.
The application includes validation checks for input fields and displays error messages.
It also provides a task summary and allows users to stop the application.
This application allows users to accept or reject tasks through the accept and reject buttons
provided for each task in the task list.
"""
from tkinter import *
from datetime import date
from datetime import datetime
import time


class TaskManager:
    """
    The __init__ method of the TaskManager class initializes the Task Manager application.
    It creates the main application window using Tkinter's Tk class.
    The method sets up various GUI elements such as labels, buttons, and option menus, and assigns them
    to instance variables for later use. It also initializes variables for storing task data and
    sets up error labels to display validation errors.
    Additionally, it configures the initial state of certain GUI elements,
    such as setting default values for option menus and entry fields. Finally,
    it initializes an initial count variable and defines the grid layout for arranging the GUI elements in the main window.
    """

    def __init__(self):
        # Application Explanation Title and Label
        self.__mainWindow = Tk()
        self.__mainWindow.title("Task Manager Application")
        # Application Explanation Title and Label
        self.__applicationExplanation = Label(self.__mainWindow,
                                              text="",
                                              font=('Modern', 14),
                                              justify="left",
                                              fg="#000080")
        # Help Button
        self.__helpUser = Button(self.__mainWindow, command=self.help_user, text="Help")
        self.__helpUser.grid(row=2,column=6)

        # Owner Dropdown
        self.__ownerLabel = Label(self.__mainWindow, text="Task Owner")
        self.__ownerOptions = ["Najmeh", "Masood", "Zahra", "Sara"]
        self.__ownerVar = StringVar(self.__mainWindow)
        self.__ownerVar.set("Select")
        self.__ownerMenu = OptionMenu(self.__mainWindow, self.__ownerVar, *self.__ownerOptions)

        # Subject Dropdown
        self.__subjectLabel = Label(self.__mainWindow, text="Subject")
        self.__subjectOptions = ["Call to ", "Send an email to ", "Meeting with ", "Demo for"]
        self.__subjectVar = StringVar(self.__mainWindow)
        self.__subjectVar.set("Select")
        self.__subjectMenu = OptionMenu(self.__mainWindow, self.__subjectVar, *self.__subjectOptions)

        # Customer Dropdown
        self.__customerLabel = Label(self.__mainWindow, text="Customer")
        self.__customerOptions = ["Oil oy", "Privet oy", "Government", "University"]
        self.__customerVar = StringVar(self.__mainWindow)
        self.__customerVar.set("Select")
        self.__customerMenu = OptionMenu(self.__mainWindow, self.__customerVar, *self.__customerOptions)

        # Deadline Label and Entry Field
        self.__deadlineLabel = Label(self.__mainWindow, text="Due Date")
        self.__deadlineEntry = Entry(self.__mainWindow, width=8)
        self.__deadlineEntry.insert(0, "dd/mm/yy")

        # Add Task Button
        self.__addTaskButton = Button(self.__mainWindow, text="Add Task", command=self.show_tasks)

        # Task Summary Label to provide a clear overview of the total number of tasks.
        self.__taskSumLabel = Label(self.__mainWindow, text="", fg="blue")

        # Store new task and deadline and number of press help button
        self.__tasks = []
        self.__deadline = []
        self.__noticeLabel = []
        self.__count = 0

        # Show Tasks Button
        self.__tasksShowButton = Button(self.__mainWindow, text="Show All Tasks", command=self.keep_task)
        self.__tasksShowLabel = Label(self.__mainWindow, text="")

        # Error Labels
        self.__subjectErrorText = Label(self.__mainWindow, text="", fg="red")
        self.__ownerErrorText = Label(self.__mainWindow, text="", fg="red")
        self.__customerErrorText = Label(self.__mainWindow, text="", fg="red")
        self.__deadlineErrorText = Label(self.__mainWindow, text="", fg="red")
        self.__errorText = Label(self.__mainWindow, text="")

        # Stop Button
        self.__stopButton = Button(self.__mainWindow, text="Stop", command=self.stop)

        # Grids row zero
        self.__applicationExplanation.grid(row=0, column=0, columnspan=7)

        # Grids row 1,2 and 3
        self.__ownerLabel.grid(row=1, column=1)
        self.__ownerMenu.grid(row=2, column=1)
        self.__ownerErrorText.grid(row=3, column=1)

        self.__subjectLabel.grid(row=1, column=2)
        self.__subjectMenu.grid(row=2, column=2)
        self.__subjectErrorText.grid(row=3, column=2)

        self.__customerLabel.grid(row=1, column=3)
        self.__customerMenu.grid(row=2, column=3)
        self.__customerErrorText.grid(row=3, column=3)

        self.__deadlineLabel.grid(row=1, column=4)
        self.__deadlineEntry.grid(row=2, column=4)
        self.__deadlineErrorText.grid(row=3, column=4)

        self.__addTaskButton.grid(row=2, column=5)

        # Grids row 5
        self.__tasksShowLabel.grid(row=5, column=0)
        self.__taskSumLabel.grid(row=6, column=5)
        self.__tasksShowButton.grid(row=5, column=5)
        self.__stopButton.grid(row=5, column=6)

    def start(self):
        """
        This method starts the execution of the application by entering the main event loop.
        """

        self.__mainWindow.mainloop()

    def help_user(self):
        """
        If self.__count is odd display explanation about application.
        If it is even close the explanation
        :return:return explanation or close it.
        """
        # Display the application explanation
        self.__count += 1
        if self.__count % 2 != 0:
            text = "+-----------------------------------------------------------------+\n" \
                   "| 1. New Task: Set all options, then 'Add Task' Button.\t\t|\n" \
                   "| 2. See all tasks: 'Show Tasks' Button.\t\t\t|\n" \
                   "| 3. Quit: 'Stop' Button.\t\t\t\t|\n" \
                   "| 4. Action: Choose one of the options available in the status.\t|\n" \
                   "|\t\t\t\t\t\t|\n"\
                   "+-----------------------------------------------------------------+\n"
        else:
            text = ""
        self.__applicationExplanation.configure(text=text)

    def add_task(self):
        """
        This method adds a new task to the application.
        It retrieves the owner, subject, customer, and deadline information from the respective variables.
        If any of the fields are empty or have the default value "Select", it displays an error message and returns.
        Otherwise, it clears the error messages and proceeds to validate the date format of the deadline.
        If the date format is incorrect, it displays an error message and returns.
        Otherwise, it adds the task to the list of tasks and updates the task summary label.
        Finally, it appends the deadline to the list of deadlines and returns "added" to indicate successful task addition.
        """

        # Retrieve the owner of the task
        owner = self.__ownerVar.get()
        if not owner or owner == "Select":
            self.__ownerErrorText.configure(text="Please select an owner.", foreground="red")
            return
        else:
            self.__ownerErrorText.configure(text="")

        # Retrieve the subject of the task
        subject = self.__subjectVar.get()
        if not subject or subject == "Select":
            self.__subjectErrorText.configure(text="Please select a subject.", foreground="red")
            return
        else:
            self.__subjectErrorText.configure(text="")

        # Retrieve the customer of the task
        customer = self.__customerVar.get()
        if not customer or customer == "Select":
            self.__customerErrorText.configure(text="Please select a customer.", foreground="red")
            return
        else:
            self.__customerErrorText.configure(text="")

        # Retrieve and validate the deadline date
        try:
            deadline = self.__deadlineEntry.get()
            day = datetime.strptime(deadline, '%d/%m/%y')
            days = day.date() - date.today()
        except ValueError:
            self.__deadlineErrorText.configure(text="Wrong date format.", foreground="red")
            return
        self.__deadlineErrorText.configure(text="")

        # Add the task to the list of tasks and update the task summary label
        self.__tasks.append(subject + " " + customer + " (Owner: " + owner + ")")
        self.__taskSumLabel.configure(text=str(len(self.__tasks)) + " tasks have been assigned.")

        # Append the deadline to the list of deadlines
        self.__deadline.append(deadline)

        # Return "added" to indicate successful task addition
        return "added"

    def keep_task(self):
        """
            This method displays the tasks and their details in the application window.

            It defines two inner functions, `accept_task` and `reject_task`, which handle the actions of accepting and rejecting a task respectively.
            The tasks and their details are displayed using labels and buttons in a grid layout.
            The `accept_task` and `reject_task` functions are assigned as command callbacks to the accept and reject buttons.
            The method also includes a task explanation label and sets up the label_job_details for displaying the task details.
            """

        def accept_task(task_index):
            # Action for accepting the task
            print("Task accepted:", self.__tasks[task_index])

        def reject_task(task_index):
            # Action for rejecting the task
            print("Task rejected:", self.__tasks[task_index])

        # Reset the task show label
        dic = {}
        task_explain = Label(self.__mainWindow, text=4*"-----------------------", fg="blue")
        task_explain.grid(row=5, column=0, columnspan=5)
        self.__noticeLabel = self.__deadline

        # Iterate over the tasks
        for i in range(len(self.__tasks)):
            # Convert the deadline string to a datetime object and calculate the number of days left
            day = datetime.strptime(self.__noticeLabel[i], '%d/%m/%y')
            days = day.date() - date.today()

            # Create labels for the task, deadline, and days left
            dic[i] = [Label(self.__mainWindow, text=str(self.__tasks[i])),
                      Label(self.__mainWindow, text=str(self.__deadline[i])),
                      Label(self.__mainWindow, text=str(days.days))]

            # Position the labels in the grid layout
            dic[i][0].grid(row=i+10, column=0)
            dic[i][1].grid(row=i+10, column=1)
            dic[i][2].grid(row=i+10, column=4)

            # Create accept and reject buttons for each task
            accept_button = Button(self.__mainWindow, text="Accept",width=2, command=lambda index=i: accept_task(index))
            accept_button.grid(row=i+10, column=3)

            reject_button = Button(self.__mainWindow, text="Reject",width=2, command=lambda index=i: reject_task(index))
            reject_button.grid(row=i+10, column=2)

        # Create labels for the task details (Task, Deadline, Action, Days Left)
        label_job_details = [None, None, None, None]
        label_job_details[0] = Label(self.__mainWindow, text="Task", relief=SUNKEN, width=30, fg="magenta")
        label_job_details[1] = Label(self.__mainWindow, text="Deadline", relief=SUNKEN, width=8, fg="magenta")
        label_job_details[2] = Label(self.__mainWindow, text="Action", relief=SUNKEN, width=14, fg="magenta")
        label_job_details[3] = Label(self.__mainWindow, text="Days Left", relief=SUNKEN, width=8, fg="magenta")

        # Position the labels for task details in the grid layout
        label_job_details[0].grid(row=9, column=0)
        label_job_details[1].grid(row=9, column=1)
        label_job_details[2].grid(row=9, column=2, columnspan=2)
        label_job_details[3].grid(row=9, column=4)

    def reset_fields(self):
        """
        This method resets the input fields and error messages in the application.
        It clears the error messages related to subject, owner, customer, and deadline.
        It clears the deadline entry field and inserts the default value "dd/mm/yy".
        It resets the subject, customer, and owner variables to their default value "Select".
        """
        self.__subjectErrorText.configure(text="")
        self.__ownerErrorText.configure(text="")
        self.__customerErrorText.configure(text="")
        self.__deadlineErrorText.configure(text="")
        self.__deadlineEntry.delete(0, END)
        self.__deadlineEntry.insert(0, "dd/mm/yy")
        self.__subjectVar.set("Select")
        self.__customerVar.set("Select")
        self.__ownerVar.set("Select")

    def show_tasks(self):
        """
        This method shows all tasks and resets the input fields for adding a new task.
        It calls the add_task method to add the task to the application.
        If the task was successfully added, it resets the input fields using the reset_fields method.
        """

        added = self.add_task()

        # Reset error messages and input fields if the task was added
        if added == "added":
            self.reset_fields()

    def stop(self):
        """
        This method stops the execution of the application by destroying the main window.
        """
        self.__mainWindow.destroy()


def main():
    ui = TaskManager()
    ui.start()


if __name__ == "__main__":
    main()
