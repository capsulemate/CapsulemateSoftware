import tkinter as tk

def init_gui():
    win = tk.Tk()
    win.title("CapsuleMate")
    win.geometry('500x400')
    tk.Label(win, text="Hello!", font=('Arial', 16)).pack()
    draw_buttons(win)
    win.update()
    return win


def maintain_gui(win):
    win.update()

def change_instruction_text(win, text):
    win.slaves()[0]["text"] = "\n\n\n{}".format(text)
    win.update()

def change_button_text(win, text_list):
    win.slaves()[1].itemconfig("btn_text_r", text=text_list[0])
    win.slaves()[1].itemconfig("btn_text_y", text=text_list[1])
    win.slaves()[1].itemconfig("btn_text_g", text=text_list[2])
    win.update()
    

def draw_buttons(win,):
    C = tk.Canvas(win, height=250, width=500)

    left_o = 30;
    
    # Draw circle for each 
    coord = 10+left_o, 160, 50+left_o, 200
    C.create_oval(coord, fill="red")
    coord = 80+left_o, 160, 120+left_o, 200
    C.create_oval(coord, fill="yellow")
    coord = 150+left_o, 160, 190+left_o, 200
    C.create_oval(coord, fill="green")

    # text for each button colour
    C.create_text(30+left_o,225, text="", font=('Arial', 14), tags="btn_text_r")
    C.create_text(100+left_o,225, text="", font=('Arial', 14), tags="btn_text_y")
    C.create_text(170+left_o,225, text="", font=('Arial', 14), tags="btn_text_g")
    
    C.pack()
    win.update()
