import tkinter as tk


class firstScreen:
    def __init__(self,window):
        window.title("Entry Terminal")
        window.geometry("800x700")
        window.configure(bg="black")

        title = tk.Label(window, text="Edit Game",bg = "blue", fg="white", font=("Arial", 27, "bold"))
        title.pack()

        main_frame = tk.Frame(window, bg="gray")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=200, pady=40)

        red_frame = tk.Frame(main_frame,bg="red", width=500,height=900)
        red_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH,expand=True)
        self.make_rows(red_frame, "red", 20)

        green_frame = tk.Frame(main_frame,bg = "green", width=500,height=900)
        green_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.BOTH,expand=True)
        self.make_rows(green_frame, "green", 20)

        button_frame = tk.Frame(main_frame, bg="gray",width=200,height=300, highlightbackground="black", highlightthickness=4)
        button_frame.pack(pady=5, padx=5)
        button_frame.pack_propagate(False)

        button = tk.Button(button_frame, text="F1 Edit Game", bg = "black", fg="white",width= 100)
        button.pack(padx=5,pady=5)
        button = tk.Button(button_frame, text="F3 Start Game", bg = "black", fg="white",width= 100)
        button.pack(padx=5,pady=5)
        button = tk.Button(button_frame, text="F8 View Game", bg = "black", fg="white",width= 100)
        button.pack(padx=5,pady=5)
        button = tk.Button(button_frame, text="F11 Change Network", bg = "black", fg="white",width= 100) #new as of 2/4/2025
        button.pack(padx=5,pady=5)
        button = tk.Button(button_frame, text="F12 Clear Game", bg = "black", fg="white",width= 100)
        button.pack(padx=5,pady=5)


    def make_rows(self, frame, bg_color, num_rows):
        
        #Making labels for ID, equipment ID
        row_frame = tk.Frame(frame, bg=bg_color)
        row_frame.pack(fill=tk.X, padx=5, pady=1)
        label = tk.Label(row_frame, text=f"       Player ID", bg=bg_color, font=("Helvetica", 14, "bold"))
        label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        label = tk.Label(row_frame, text=f"Equipment ID", bg=bg_color, font=("Helvetica", 14, "bold"))
        label.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)

        
        for row in range(num_rows):
            row_frame = tk.Frame(frame, bg=bg_color)
            row_frame.pack(fill=tk.X, padx=5, pady=1)

            #Making alignment good for entry boxes
            if row <= 9:
                label = tk.Label(row_frame, text=f" {row} ", bg=bg_color, font=("Helvetica", 20))
                label.pack(side=tk.LEFT, padx=5)
            else:
                label = tk.Label(row_frame, text=f"{row}", bg=bg_color, font=("Helvetica", 20))
                label.pack(side=tk.LEFT, padx=5)

            entry = tk.Entry(row_frame, bg="white", fg="black")
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            entry = tk.Entry(row_frame, bg="white", fg="black")
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)



window = tk.Tk()
gui = firstScreen(window)
window.mainloop()
