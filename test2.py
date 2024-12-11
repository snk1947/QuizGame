import tkinter as tk


def approach_3():
    def close_window():
        root.destroy()

    # Create the main window
    root = tk.Tk()

    # Set the window size
    root.geometry("400x300+200+200")

    # Remove the default title bar
    root.overrideredirect(True)

    # Create a custom title bar
    title_bar = tk.Frame(root, bg='gray', relief='raised', bd=2)
    title_bar.pack(fill=tk.X)

    # Add a title label to the custom title bar
    title_label = tk.Label(title_bar, text="Custom Title Bar - Approach 3", bg='gray', fg='white')
    title_label.pack(side=tk.LEFT, padx=10)

    # Add a close button to the custom title bar
    close_button = tk.Button(title_bar, text='X', command=close_window, bg='gray', fg='white', relief='flat')
    close_button.pack(side=tk.RIGHT, padx=5)

    # Add content to the main window
    content = tk.Frame(root, bg='lightblue')
    content.pack(fill=tk.BOTH, expand=True)

    # Function to move the window
    def move_window(event):
        pos_of_mouse_x = event.x_root
        pos_of_mouse_y = event.y_root
        pos_of_root_x = pos_of_mouse_x - event.x
        pos_of_root_y = pos_of_mouse_y - event.y
        pos_of_root_after_mouse_motion_x=pos_of_root_x
        root.geometry(f"+{pos_of_root_x}+{pos_of_root_y}")
        print(pos_of_mouse_x,pos_of_mouse_y)

    # Bind the title bar to the move window function
    title_bar.bind('<B1-Motion>', move_window)
    # title_bar.bind('<Button-1>', move_window)

    # Run the application
    root.mainloop()


approach_3()
