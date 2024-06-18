import os
import sys
import tkinter as tk
import ctypes

# Function to run the script with administrative privileges
def run_as_admin():
    if sys.platform.startswith('win'):
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        else:
            cmd_args = ' '.join(['"{}"'.format(arg) for arg in sys.argv])
            try:
                ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, cmd_args, None, 1)
                return True
            except:
                return False
    else:
        return True

# Function to block websites
def block_website():
    website = website_entry.get()
    if website:
        # Add website to hosts file with localhost IP address
        with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as file:
            file.write("127.0.0.1 " + website + "\n")
        blocked_websites.insert(tk.END, website)
        website_entry.delete(0, tk.END)

# Check if script is running with administrative privileges
if not run_as_admin():
    tk.messagebox.showerror("Error", "This script requires administrator privileges to run.")
    sys.exit()

# Create GUI window
window = tk.Tk()
window.title("Website Blocker")

# Create input box and button to block websites
website_label = tk.Label(window, text="Website:")
website_label.pack()

website_entry = tk.Entry(window)
website_entry.pack()

block_button = tk.Button(window, text="Block", command=block_website)
block_button.pack()

# Create listbox to display blocked websites
blocked_websites_label = tk.Label(window, text="Blocked Websites:")
blocked_websites_label.pack()

blocked_websites = tk.Listbox(window)
blocked_websites.pack()

# Load blocked websites from hosts file
with open(r"C:\Windows\System32\drivers\etc\hosts", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("127.0.0.1"):
            website = line.split()[1]
            blocked_websites.insert(tk.END, website)

window.mainloop()

