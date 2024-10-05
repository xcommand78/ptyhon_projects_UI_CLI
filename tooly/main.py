import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import wikipedia# for wikiedia 
import pandas as pd # for tables 
from rich.console import Console #styling
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
import math # calulation
import pyttsx3 # for audio output
from fpdf import FPDF# pdf genration
import os
class tooly_class:
    def __init__(self):
        self.console = Console()
        self.logo='''

                   ///           __/////////__ __/////////__  ///      ///      ///
                  ///           ///       /// ///        /// ///      ///      ///
           _____ ///_________  ///       /// ///        /// ///      ///      ///
          /////////////////// ///       /// ///        /// ///      ///      ///
               ///           ///       /// ///        /// ///      ///      ///
              ///           ///       /// ///        /// ///      ////////////
             ///           ///______ /// ///________/// ///_______        ///
            ///_________    /////////     //////////   ///////////       ///
           /////////////                                                ///
                                                               /////////// v1.0
                                                    /////////////// [magenta]By: karan singh(xcommand)[/magenta]'''
        self.console.print(Panel(self.logo), style="green")
        
        self.console.print(Panel(Text("Welcome to Tooly! 🎉", style="bold magenta"), title="Tooly"))
        self.console.print(f"Hello sir, how are you?")
        self.console.print(f"Current time is {datetime.datetime.now()} and Date is {datetime.date.today()}")

    def wikipedia(self, query):
        wiki = wikipedia.page(query)
        self.console.print(f"[bold cyan]{wiki.title}[/bold cyan]")
        self.console.print(wiki.summary)

    def notes_creation(self, notes):
        date = datetime.date.today()
        filename = date.strftime("%d-%m-%y") + ".txt"
        with open(filename, "w") as file:
            file.write(notes)
        self.console.print(f"[green]Notes saved to {filename}[/green]")

    def notes_cheack(self, date_of_creation):
        date_log_data = date_of_creation + ".txt"
        try:
            with open(date_log_data, "r") as file:
                file_reading = file.read()
                self.console.print(f"[blue]Notes for {date_of_creation}:[/blue]")
                self.console.print(file_reading)
        except FileNotFoundError:
            self.console.print(f"[red]No notes found for {date_of_creation}[/red]")

    def calculation(self, operation, values):
        try:
            values = list(map(float, values.split(',')))
            if operation.lower() in ["addition", "add"]:
                result = sum(values)
                self.console.print(f"[green]The result of the addition is: {result}[/green]")
            elif operation.lower() in ["sub", "subtraction"]:
                result = values[0]
                for i in range(1, len(values)):
                    result -= values[i]
                self.console.print(f"[green]The result of the subtraction is: {result}[/green]")
            elif operation.lower() in ["mul", "multiplication"]:
                result = math.prod(values)
                self.console.print(f"[green]The result of the multiplication is: {result}[/green]")
            elif operation.lower() in ["div", "division"]:
                result = values[0]
                for i in range(1, len(values)):
                    result /= values[i]
                self.console.print(f"[green]The result of the division is: {result}[/green]")
            elif operation.lower() == "round":
                rounded_values = [round(value) for value in values]
                self.console.print(f"[green]Rounded values: {rounded_values}[/green]")
            elif operation.lower() == "ceil":
                ceiling_values = [math.ceil(value) for value in values]
                self.console.print(f"[green]Ceiling values: {ceiling_values}[/green]")
            else:
                self.console.print(f"[red]Operation '{operation}' is not recognized.[/red]")
        except Exception as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def tasks_manger(self, time, date, task, filename="Task_Schedule_file.csv"):
        data = {"Time": [time],
                "Date": [date],
                "Task": [task]}
        task_df = pd.DataFrame(data)
        try:
            task_df.to_csv(filename, mode='a', header=False, index=False)
            self.console.print(f"[green]Task added successfully![/green]")
        except FileNotFoundError:
            task_df.to_csv(filename, index=False)
            self.console.print(f"[green]Task file created and task added![/green]")

    def show_tasks(self, filename="Task_Schedule_file.csv"):
        try:
            tasks_df = pd.read_csv(filename)
            if tasks_df.empty:
                self.console.print("[red]No tasks available.[/red]")
                return

            table = Table(title="Task Schedule", show_header=True, header_style="bold magenta")
            table.add_column("Time", style="cyan")
            table.add_column("Date", style="red")
            table.add_column("Task", style="green")

            for index, row in tasks_df.iterrows():
                table.add_row(row['Time'], row['Date'], row['Task'])

            self.console.print(table)

        except FileNotFoundError:
            self.console.print("[red]Task file not found.[/red]")

    def read_document(self, file, speed):
        engine = pyttsx3.init()
        with open(file, "r") as file_to_read:
            audio_file = file_to_read.read()
            engine.say(audio_file)
            self.console.print(Panel(Text(audio_file, style="bold green"), title=file))
            print("/n")
            engine.setProperty('rate', speed)
            engine.runAndWait()

    def report_to_pdf(self, report_file, pdffile):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=15)
        if os.path.exists(pdffile):
            self.console.print(f"[red]File already exists[/red]")
            return
        try:
            with open(report_file, "r", encoding='utf-8') as report:
                pdf_file = report.read()

            pdf.multi_cell(10, 12, text=pdf_file)
            self.console.print(f"[blue]Generating PDF: {pdffile}[/blue]")
            pdf.output(pdffile)
        except FileNotFoundError:
            self.console.print(f"[red]The file {report_file} not found[/red]")

    def web(self, operation):
        driver = webdriver.Edge()
        try:
            if operation.lower() == "git_hub":
                driver.get("http://www.github.com")
            elif operation.lower() == "gmail":
                driver.get("https://gmail.com")
                time.sleep(2)  # Wait for the page to load
                
                # Add your email and password handling here
                email_address = "example@gamil.com" # add the email address
                password ="password"
                
                # Enter email
                email_input = driver.find_element(By.ID, "identifierId")
                email_input.send_keys(email_address)
                email_input.send_keys(Keys.RETURN)
                time.sleep(2)  # Wait for transition

                # Enter password
                password_input = driver.find_element(By.NAME, "password")
                password_input.send_keys(password)
                password_input.send_keys(Keys.RETURN)
                time.sleep(5)  # Wait for inbox to load

                # Display unread emails
                unread_emails = driver.find_elements(By.CSS_SELECTOR, "tr.zE")  # Unread emails have class 'zE'
                if unread_emails:
                    print(f"You have {len(unread_emails)} unread emails.")
                    for email in unread_emails:
                        subject = email.find_element(By.CSS_SELECTOR, "h3").text
                        print(f"Unread email subject: {subject}")
                else:
                    print("No unread emails.")
                
                print("Gmail opened. Press Enter to close the browser.")
                input()  # Wait for user input to close the browser
            else:
                self.console.print(f"[red]Unknown operation: {operation}[/red]")
        finally:
            driver.quit()


tooly = tooly_class()
conso = Console()
while True:
    # User input action starts 
    conso.print(f"[green]What you want to do[/green] [red][wikipedia[/red]|[yellow]create_notes[/yellow]|[blue]show_notes[/blue]|[green]gmail[/green]|[sky blue]read_document[/sky blue]|[magenta]add_task[/magenta]|[green]show_task|calculation|git_hub]: ")
    action = input()
    if action.lower() == "wikipedia" or action.lower() == "wiki":
        query = input("Enter the query[]: ")
        tooly.wikipedia(query)
    elif action.lower() == "create_notes":
        tooly.console.print("Enter your notes for the day......[]:", style="green")
        notes = input()
        tooly.notes_creation(notes)
    elif action.lower() == "show_notes":
        tooly.console.print("Check notes [Enter the date in the standard format eg: D-M-Y]: ")
        date = input()
        tooly.notes_cheack(date)
    elif action.lower() == "read_document":
        file_path = input("Enter file path: ")
        speed = int(input("Enter the speed [100:slow|150:medium|200:fast]: "))
        tooly.read_document(file_path, speed)
    elif action.lower() == "add_task":
        time = input("Enter the time [Eg: 00:00]: ")
        date = input("Enter the Date [Eg: D-M-Y]: ")
        task = input("Enter your Task you will do at the day..[] ")
        tooly.tasks_manger(time, date, task)
    elif action.lower() == "show_task":
        tooly.show_tasks()
    elif action.lower() == "calculation":
        operation_in = input("Enter the Operation [add/sub/mul/div/round/ceil]: ")
        values_in = input("Enter the values [Eg: 1,2,3,4]: ")
        tooly.calculation(operation_in, values_in)
    elif action.lower() == "generate_pdf":
        file_name_ = input("Enter the file name[]: ")
        pdf_file_name = input("Enter the name you want to give to your file[]: ")
        tooly.report_to_pdf(file_name_, pdf_file_name)
    elif action.lower() == "git_hub":
        tooly.web(action)
    elif action.lower() == "gmail":
        tooly.web(action)
    else:
        tooly.console.print(f"[red]Unknown action: {action}[/red]")
