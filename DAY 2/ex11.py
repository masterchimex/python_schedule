print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")



# Collect user data
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

# Display the collected data
print("Name:", name)
print("Age:", age)
print("Email:", email)
print("Address:", address)

# import tkinter as tk

# def submit_form():
#     # Retrieve values from the form inputs
#     name = name_entry.get()
#     email = email_entry.get()
#     age = age_entry.get()
#     address = address_text.get("1.0", tk.END)
#     gender = gender_var.get()
#     interests = []
#     if interest_var1.get():
#         interests.append("Programming")
#     if interest_var2.get():
#         interests.append("Gaming")
#     if interest_var3.get():
#         interests.append("Reading")

#     # Display the submitted form data
#     print("Name:", name)
#     print("Email:", email)
#     print("Age:", age)
#     print("Address:", address)
#     print("Gender:", gender)
#     print("Interests:", ", ".join(interests))

# # Create the main window
# window = tk.Tk()
# window.title("Form")

# # Create form labels and inputs
# name_label = tk.Label(window, text="Name:")
# name_label.pack()
# name_entry = tk.Entry(window)
# name_entry.pack()

# email_label = tk.Label(window, text="Email:")
# email_label.pack()
# email_entry = tk.Entry(window)
# email_entry.pack()

# age_label = tk.Label(window, text="Age:")
# age_label.pack()
# age_entry = tk.Entry(window)
# age_entry.pack()

# address_label = tk.Label(window, text="Address:")
# address_label.pack()
# address_text = tk.Text(window, height=5, width=30)
# address_text.pack()

# gender_label = tk.Label(window, text="Gender:")
# gender_label.pack()
# gender_var = tk.StringVar()
# gender_var.set("Male")
# gender_option = tk.OptionMenu(window, gender_var, "Male", "Female", "Other")
# gender_option.pack()

# interests_label = tk.Label(window, text="Interests:")
# interests_label.pack()
# interest_var1 = tk.BooleanVar()
# interest_var1.set(False)
# interest_check1 = tk.Checkbutton(window, text="Programming", variable=interest_var1)
# interest_check1.pack()
# interest_var2 = tk.BooleanVar()
# interest_var2.set(False)
# interest_check2 = tk.Checkbutton(window, text="Gaming", variable=interest_var2)
# interest_check2.pack()
# interest_var3 = tk.BooleanVar()
# interest_var3.set(False)
# interest_check3 = tk.Checkbutton(window, text="Reading", variable=interest_var3)
# interest_check3.pack()

# submit_button = tk.Button(window, text="Submit", command=submit_form)
# submit_button.pack()

# # Start the main event loop
# window.mainloop()
