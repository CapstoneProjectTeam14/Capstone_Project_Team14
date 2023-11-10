import tkinter as tk
from tkinter import Label, Text, Button, messagebox, simpledialog
import requests

# REST API url and headers
host = "192.168.0.239"
port = "8181"
url = f"http://{host}:{port}/onos/v1/acl/rules"
headers = {'Content-type': 'application/json'}

def get_credentials():
    username = simpledialog.askstring("Authentication", "Enter your username:")
    password = simpledialog.askstring("Authentication", "Enter your password:", show='*')
    return username, password

def upload_policy():
    username, password = get_credentials()
    if not username or not password:
        messagebox.showwarning("Warning", "Please enter both username and password.")
        return

    policy_data = policy_text.get("1.0", "end-1c")
    if not policy_data.strip():
        messagebox.showwarning("Warning", "Please enter firewall policies.")
        return

    firewall_rules = []
    lines = policy_data.split('\n')
    for line in lines:
        row = line.split(',')
        if len(row) >= 3:
            firewall_rules.append((row[1], row[2]))

    if not firewall_rules:
        messagebox.showwarning("Warning", "Invalid firewall policies format.")
        return

    # put each firewall rule into the ACL using the REST API
    for rule in firewall_rules:
        resp = requests.post(
            url,
            json={
                "srcIp": "10.0.0.0/24",
                "srcMac": rule[0],
                "dstMac": rule[1]
            },
            auth=(username, password)
        )
        print(resp.text)

    if resp.status_code == 200:
        messagebox.showinfo("Success", "Policy uploaded successfully")
        policy_text.delete("1.0", tk.END)
    else:
        messagebox.showerror("Error", f"Failed to upload policies. Status code: {resp.status_code}")

# GUI setup
root = tk.Tk()
root.title("Firewall Policy Uploader")

header_label = Label(root, text="Firewall Policy Uploader", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

instruction_label = Label(root, text="Paste Firewall Policies (CSV):")
instruction_label.pack()

policy_text = Text(root, height=5, width=50)
policy_text.pack()

upload_button = Button(root, text="Upload Policies", command=upload_policy, bg="green", fg="white")
upload_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
