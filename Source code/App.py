import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

BG_COLOR = "#2c3e50"
FG_COLOR = "#ffffff"
BUTTON_BG_COLOR = "#34495e"
BUTTON_FG_COLOR = "#ffffff"
BUTTON_ACTIVE_COLOR = "#95a5a6"


def generate_key():
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)
    messagebox.showinfo("Key Generated", "Key has been generated and saved as 'mykey.key'.")


def encrypt_file():
    key_file = filedialog.askopenfilename(title="Select Key File", filetypes=(("Key files", "*.key"),))
    file_to_encrypt = filedialog.askopenfilename(title="Select File to Encrypt")
    
    if key_file and file_to_encrypt:
        with open(key_file, 'rb') as key_file:
            key = key_file.read()
        
        fernet = Fernet(key)
        
        with open(file_to_encrypt, 'rb') as original_file:
            original = original_file.read()
        
        encrypted = fernet.encrypt(original)
        
        with open(file_to_encrypt, 'wb') as file_to_encrypt:
            file_to_encrypt.write(encrypted)
        
        messagebox.showinfo("Encryption Successful", "File has been encrypted successfully.")
    else:
        messagebox.showerror("Error", "Please provide all the necessary information.")


def decrypt_file():
    key_file = filedialog.askopenfilename(title="Select Key File", filetypes=(("Key files", "*.key"),))
    file_to_decrypt = filedialog.askopenfilename(title="Select File to Decrypt")
    
    if key_file and file_to_decrypt:
        with open(key_file, 'rb') as key_file:
            key = key_file.read()
        
        fernet = Fernet(key)
        
        with open(file_to_decrypt, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        
        decrypted = fernet.decrypt(encrypted)
        
        with open(file_to_decrypt, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        
        messagebox.showinfo("Decryption Successful", "File has been decrypted successfully.")
    else:
        messagebox.showerror("Error", "Please provide all the necessary information.")

# Create the main window
window = tk.Tk()
window.configure(bg=BG_COLOR)
window.title("File Encryption")
window.geometry("400x200")

# Generate Key Button
generate_key_button = tk.Button(window, text="Generate Key", font=("Arial", 12), bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,
                               activebackground=BUTTON_ACTIVE_COLOR, command=generate_key)
generate_key_button.pack(pady=20)

# Encrypt File Button
encrypt_button = tk.Button(window, text="Encrypt File", font=("Arial", 12), bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,
                           activebackground=BUTTON_ACTIVE_COLOR, command=encrypt_file)
encrypt_button.pack()

# Decrypt File Button
decrypt_button = tk.Button(window, text="Decrypt File", font=("Arial", 12), bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,
                           activebackground=BUTTON_ACTIVE_COLOR, command=decrypt_file)
decrypt_button.pack(pady=10)

# Start the main loop
window.mainloop()
