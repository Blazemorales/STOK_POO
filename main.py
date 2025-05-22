from packages.controllers.Controle_STOK import Interface_Estoque
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("STOK - Sistema de Estoque - Made in FGA")
    root.geometry("500x400")
    
    app_STOK = Interface_Estoque(root)
    root.mainloop()

if __name__ == "__main__":
    main()