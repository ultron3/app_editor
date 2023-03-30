import tkinter as tk
from tkinter import filedialog
#pyinstaller nome_script.py --onefile
#pyinstaller nome_script.py --noconsole --onefile
#i due comandi per far diventare un programma python in un nome_script.exe
#docker image build -t prima-immagine:0.1 .

class Menubar:

    def __init__(self, parent):
        font_specs = ("ubuntu20.04", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="Nuovo File",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Apri File",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Salva",
                                  command=parent.save)
        file_dropdown.add_command(label="Salva con Nome",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esci",
                                  command=parent.master.destroy)

        menubar.add_cascade(label="File", menu=file_dropdown)


class PyText:

    def __init__(self, master):
        master.title("Notepad - PyText")
        master.geometry("1200x700")

        font_specs = ("ubuntu", 18)

        self.master = master

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)

    def set_window_title(self):
        pass

    def new_file(self):
        self.textarea.delete('1.0', tk.END)

        

    def open_file(self):

        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                file_content = f.read()
            self.textarea.delete('1.0', tk.END)
            self.textarea.insert(tk.END, file_content)
       

    def save(self):
        try:
            
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("Tutti i file", "*.*"),
                           ("File di Testo", "*.txt"),
                           ("Script Python", "*.py"),
                           ("Markdown Text", "*.md"),
                           ("File JavaScript", "*.js"),
                           ("File TipeScript", "*.ts"),
                           ("file pdf","*.pdf"),
                           ("Documenti HMTL", "*.html"),
                           ("documento jsonanta","*.json"),
                           ("Documenti CSS", "*.css")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)
       

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:

            with open(file_path, 'w') as f:
                f.write(self.textarea.get('1.0', tk.END))
       



if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()