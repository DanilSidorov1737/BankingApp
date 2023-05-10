import customtkinter as customtkinter
import json
import tkinter.messagebox as messagebox
import tkinter as tk

# To-Do List:
# 1. Create a stock market page where users can search for stocks and view their graphs.
# 2. Develop an investment page where users can buy stocks.
# 3. Include retirement, stocks, and other assets in the net worth calculator.
# 4. Implement the ability to hide money on every page, not just the net worth main text box.
# 5. Create stock market settings to allow users to customize their experience.
# 6. Implement message boxes for checking, savings, credit withdrawal, and deposit.
# 7. Add a refresh button to the app so users can update their account balances after a transaction.
# 8. Need to get rid of the tiny errors that happen when you click on a button or exit






attempts = 0
def login():
    global attempts

   

    username = username_entry.get()
    password = password_entry.get()

    with open('Data/users.json') as f:
        data = json.load(f)

        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                checking = user['checking']
                savings = user['savings']
                credit = user['credit']
                username = user['username']
                password = user['password']
                debt = user['debt']
                networth = user['networth']
                print("User authenticated!")
                login_screen.destroy() 
                app = App(username, password, checking, savings, credit, debt, networth)
                app.mainloop()
                
                
                return True

        attempts += 1
        if attempts == 3:
            messagebox.showerror("Error", "Too many failed attempts. Exiting...")
            login_screen.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password. " + str(3 - attempts) + " remaining.")
        return False

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self, username, password, checking, savings, credit, debt, networth):
        
        super().__init__()

        self.username = username
        self.password = password 
        self.checking = checking 
        self.savings = savings 
        self.credit = credit
        self.debt = debt 
        self.networth = networth



        # configure window
        self.title("Banking App")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"Hi, {username}", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)


        self.sidebar_button_logout = customtkinter.CTkButton(self.sidebar_frame, command=self.logout_button)
        self.sidebar_button_logout.grid(row=5, column=0, padx=20, pady=10)


        # self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        # self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text="Search", text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(36, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Checking")
        self.tabview.add("Saving")
        self.tabview.add("Credit")

        self.tabview.tab("Checking").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Saving").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Credit").grid_columnconfigure(0, weight=1)



        self.string_input_deposit = customtkinter.CTkButton(self.tabview.tab("Checking"), text="Deposit",
                                                        command=self.open_input_deposit_checking_event)
        self.string_input_deposit.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.string_input_withdraw = customtkinter.CTkButton(self.tabview.tab("Checking"), text="Withdraw",
                                                        command=self.open_input_withdraw_checking_event)
        self.string_input_withdraw.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_deposit_savings = customtkinter.CTkButton(self.tabview.tab("Saving"), text="Deposit",
                                                        command=self.open_input_deposit_savings_event)
        self.string_input_deposit_savings.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_withdraw_savings = customtkinter.CTkButton(self.tabview.tab("Saving"), text="Withdraw",
                                                        command=self.open_input_withdraw_savings_event)
        self.string_input_withdraw_savings.grid(row=3, column=0, padx=20, pady=(10, 10))


        self.string_input_deposit_credit = customtkinter.CTkButton(self.tabview.tab("Credit"), text="Pay Off",
                                                        command=self.open_input_credit_deposit_event)
        self.string_input_deposit_credit.grid(row=3, column=0, padx=20, pady=(10, 10))



        self.label_tab_1 = customtkinter.CTkLabel(self.tabview.tab("Checking"), text=f"Total Checking: {checking}")
        self.label_tab_1.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Saving"), text=f"Total Savings: {savings}")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        

        self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Credit"), text=f"Total Credit: {credit}")
        self.label_tab_3.grid(row=0, column=0, padx=50, pady=20)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(36, 0), sticky="nsew")
        self.radio_var = tk.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Hide Money:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0, text="Hidden", command=self.on_radio_button_hidden_click)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text="Viewable", command=self.on_radio_button_shown_click)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2.select()
        

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="white")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        self.slider_frame_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Calculator")
        self.slider_frame_label.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.progress_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Total Debt to Assets: \n ", font=("Roboto", 15))
        self.progress_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=3, column=0, padx=(20, 20), pady=(5, 0), sticky="ew")




        #Total Borrowing Ammount
        self.total_borrowing_entry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Total Borrowing:")
        self.total_borrowing_entry.grid(row=2, column=1, padx=5, pady=(10, 5), sticky="ew")

        # Debt Lease
        self.debt_lease_entry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Debt Lease (Years)")
        self.debt_lease_entry.grid(row=3, column=1, padx=5, pady=(10, 5), sticky="ew")

        self.interest_entry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Interest Rate")
        self.interest_entry.grid(row=4, column=1, padx=5, pady=(10, 5), sticky="ew")


        self.calc_button = customtkinter.CTkButton(self.slider_progressbar_frame, text="Calculate Payment", command=self.calculate_payment)
        self.calc_button.grid(row=5, column=1, padx=5, pady=(10, 5), sticky="ew")

        self.calc_button_ans = customtkinter.CTkLabel(self.slider_progressbar_frame, text=F"Total Payment is: \n  ", font=("Roboto", 15))
        

        self.calc_button_ans.grid(row=4, column=0, padx=(20, 5), pady=5, sticky="w")




        #Interest Rate
        # self.interest_rate_entry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Interest")
        # self.interest_rate_entry.grid(row=4, column=1, padx=5, pady=(0, 0), sticky="ew")





 




        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Stock Market Settings")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.stock_bot_switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Stock Bot")
        self.stock_bot_switch.grid(row=0, column=0, padx=10, pady=(0, 20))

        self.auto_buy_switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Auto Buy")
        self.auto_buy_switch.grid(row=1, column=0, padx=10, pady=(0, 20))

        self.auto_sell_switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Auto Sell")
        self.auto_sell_switch.grid(row=2, column=0, padx=10, pady=(0, 20))

            

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.checkbox_label = customtkinter.CTkLabel(self.checkbox_slider_frame, text="Include in \n\nNetworth Calculation", font=("Roboto", 15))
        self.checkbox_label.grid(row=0, column=0, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="Investments" , state="disabled")
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="Retirement  ", state="disabled")
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="Other Assets", state="disabled")
        self.checkbox_3.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="n")

        # set default values
        self.sidebar_button_1.configure(state="disabled", text="Stock Market")
        self.sidebar_button_2.configure(state="disabled", text="Invesments")
        self.sidebar_button_3.configure(state="disabled", text="Coming Soon")
        self.sidebar_button_logout.configure(state="enabled", text="Logout")
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
    
        # self.appearance_mode_optionemenu.set("Dark")
        # self.scaling_optionemenu.set("100%")
  
        #self.slider_1.configure(command=self.progressbar_2.set)
        #self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="determinate", progress_color="red" )
        #self.progressbar_1.set(0.5)
        #self.progressbar_1.start()
        self.textbox.insert("0.0", f"Your Total Networth is : ${(float(self.checking[1:]) + float(self.savings[1:])) - float(self.credit[1:])} \n\n")
        self.textbox.insert("0.0", "-------- " * 7)
        self.textbox.insert("0.0", f"The Ammount of Credit Debt you owe is: {self.credit} \n\n")
        self.textbox.insert("0.0", f"The Value of your Savings account it: {self.savings} \n\n")
        self.textbox.insert("0.0", f"The Value of your Checking account it: {self.checking} \n\n")
        
        self.textbox.insert("1.0", "Networth \n\n")


    def on_radio_button_hidden_click(self):
        print("Hidden Button Clicked")
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", f"Your Total Networth is : ******* \n\n")
        self.textbox.insert("0.0", "-------- " * 7)
        self.textbox.insert("0.0", f"The Ammount of Credit Debt you owe is: ******* \n\n")
        self.textbox.insert("0.0", f"The Value of your Savings account it: ******* \n\n")
        self.textbox.insert("0.0", f"The Value of your Checking account it: ******* \n\n")
        self.textbox.insert("1.0", "Networth \n\n")
    
    def on_radio_button_shown_click(self):
        print("Shown Button Clicked")
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", f"Your Total Networth is : ${(float(self.checking[1:]) + float(self.savings[1:])) - float(self.credit[1:])} \n\n")
        self.textbox.insert("0.0", "-------- " * 7)
        self.textbox.insert("0.0", f"The Ammount of Credit Debt you owe is: {self.credit} \n\n")
        self.textbox.insert("0.0", f"The Value of your Savings account it: {self.savings} \n\n")
        self.textbox.insert("0.0", f"The Value of your Checking account it: {self.checking} \n\n")
        
        self.textbox.insert("1.0", "Networth \n\n")

    def calculate_payment(self):
        # Get the values entered by the user
        total_borrowing = self.total_borrowing_entry.get()
        debt_lease = self.debt_lease_entry.get() 
        interest_entry = self.interest_entry.get()

        TB = float(total_borrowing)
        DL = int(debt_lease)
        IE = float(interest_entry) / 100 / 12

        # Print the values to the console
        print("Total Borrowing:", total_borrowing)
        print("Debt Lease:", debt_lease)
        print("Interest Rate:", interest_entry)

        num_payments = 12 * DL
        denominator = 1- (1 + IE) ** (-num_payments)
        monthly_payment = (IE * (TB + DL)) / denominator

        print()
        print("Total Payment is: \n $ {:.2f}".format(monthly_payment))
        self.calc_button_ans.configure(text=f"Total Payment is: ${monthly_payment:.2f}")

        DEBT_To_NET = (TB / float(self.networth)) * 100
        print(DEBT_To_NET)
        self.progressbar_1.set(DEBT_To_NET)

        self.progress_label.configure(text=f"Total Debt to Assets: \n{DEBT_To_NET:.2f}%")

        

        

  



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)

    # def change_scaling_event(self, new_scaling: str):
    #     new_scaling_float = int(new_scaling.replace("%", "")) / 100
    #     customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def logout_button(self):
        quit()

    def open_input_credit_deposit_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in how much you want to pay off:", title="Credit Deposit")
        credit_ammount = float(self.credit[1:])
        withdraw = float(dialog.get_input())
        if withdraw > credit_ammount:
            messagebox.showinfo(title="Error", message="Something went wrong!!!", icon="error")
        else:
            print(f"New Ammount: {credit_ammount - withdraw}")
            new_amount = credit_ammount - withdraw
            # Open the JSON file and read its contents
            with open('Data/users.json', 'r') as f:
                data = json.load(f)

            # Find the user with the desired username
            username = self.username
            user = next((u for u in data['users'] if u['username'] == username), None)

            if user:
                # Modify the value of the "checking" entry
                print(self.checking)
                user['credit'] = f"${new_amount}"
                print(user['checking'])

                # Write the updated JSON data structure back to the file
                with open('Data/users.json', 'w') as f:
                    json.dump(data, f, indent=4)
      
            else:
                print(f"No user with username {username} found")

    def open_input_deposit_savings_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in how much you want to Deposit (savings):", title="Deposit")
        checking_ammount = float(self.savings[1:])
        deposit = float(dialog.get_input())
        print(f"New Ammount: {checking_ammount + deposit}")
        new_amount = checking_ammount + deposit
        # Open the JSON file and read its contents
        with open('Data/users.json', 'r') as f:
            data = json.load(f)

        # Find the user with the desired username
        username = self.username
        user = next((u for u in data['users'] if u['username'] == username), None)

        if user:
            # Modify the value of the "checking" entry
            print(self.checking)
            user['savings'] = f"${new_amount}"
            print(user['checking'])

            # Write the updated JSON data structure back to the file
            with open('Data/users.json', 'w') as f:
                json.dump(data, f, indent=4)    
        else:
            print(f"No user with username {username} found")


    def open_input_deposit_checking_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in how much you want to Deposit (checking):", title="Deposit")
        checking_ammount = float(self.checking[1:])
        deposit = float(dialog.get_input())
        print(f"New Ammount: {checking_ammount + deposit}")
        new_amount = checking_ammount + deposit
        # Open the JSON file and read its contents
        with open('Data/users.json', 'r') as f:
            data = json.load(f)

        # Find the user with the desired username
        username = self.username
        user = next((u for u in data['users'] if u['username'] == username), None)

        if user:
            # Modify the value of the "checking" entry
            print(self.checking)
            user['checking'] = f"${new_amount}"
            print(user['checking'])

            # Write the updated JSON data structure back to the file
            with open('Data/users.json', 'w') as f:
                json.dump(data, f, indent=4)    
        else:
            print(f"No user with username {username} found")
        

    def open_input_withdraw_savings_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in how much you want to withdraw: (savings)", title="Withdrawal")
        checking_ammount = float(self.savings[1:])
        withdraw = float(dialog.get_input())
        if withdraw > checking_ammount:
            messagebox.showinfo(title="Error", message="Something went wrong!!!", icon="error")
        else:
            print(f"New Ammount: {checking_ammount - withdraw}")
            new_amount = checking_ammount - withdraw
            # Open the JSON file and read its contents
            with open('Data/users.json', 'r') as f:
                data = json.load(f)

            # Find the user with the desired username
            username = self.username
            user = next((u for u in data['users'] if u['username'] == username), None)

            if user:
                # Modify the value of the "checking" entry
                print(self.checking)
                user['savings'] = f"${new_amount}"
                print(user['checking'])

                # Write the updated JSON data structure back to the file
                with open('Data/users.json', 'w') as f:
                    json.dump(data, f, indent=4)
      
            else:
                print(f"No user with username {username} found")

    def open_input_withdraw_checking_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in how much you want to withdraw: (checking)", title="Withdrawal")
        checking_ammount = float(self.checking[1:])
        withdraw = float(dialog.get_input())
        if withdraw > checking_ammount:
            messagebox.showinfo(title="Error", message="Something went wrong!!!", icon="error")
        else:
            print(f"New Ammount: {checking_ammount - withdraw}")
            new_amount = checking_ammount - withdraw
            # Open the JSON file and read its contents
            with open('Data/users.json', 'r') as f:
                data = json.load(f)

            # Find the user with the desired username
            username = self.username
            user = next((u for u in data['users'] if u['username'] == username), None)

            if user:
                # Modify the value of the "checking" entry
                print(self.checking)
                user['checking'] = f"${new_amount}"
                print(user['checking'])

                # Write the updated JSON data structure back to the file
                with open('Data/users.json', 'w') as f:
                    json.dump(data, f, indent=4)
                
                
                

                
                
            else:
                print(f"No user with username {username} found")
   

login_screen = customtkinter.CTk()
login_screen.geometry("400x400")
login_screen.title("Login Screen")

username_label = customtkinter.CTkLabel(login_screen, text="Username:")
username_label.pack(pady=10)

username_entry = customtkinter.CTkEntry(login_screen)
username_entry.pack(pady=5)

password_label = customtkinter.CTkLabel(login_screen, text="Password:")
password_label.pack(pady=10)

password_entry = customtkinter.CTkEntry(login_screen, show="*")
password_entry.pack(pady=5)

login_button = customtkinter.CTkButton(login_screen, text="Login", command=login)
login_button.pack(pady=10)

login_screen.mainloop()

if __name__ == "__main__":
    login()
