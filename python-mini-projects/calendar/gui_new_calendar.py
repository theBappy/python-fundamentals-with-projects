from tkinter import *
from tkinter import ttk
import calendar

# Function to display the calendar of a given year
def showCal():
    new_window = Toplevel()
    new_window.title("Calendar")
    new_window.geometry("600x600")
    new_window.config(bg="#fdfdfd")

    fetch_year = year_field.get().strip()

    # Validation
    if not fetch_year.isdigit():
        error_label = Label(
            new_window,
            text="❌ Please enter a valid year (e.g., 2025)",
            font=("Helvetica", 12, "bold"),
            fg="red",
            bg="#fdfdfd",
        )
        error_label.pack(pady=20)
        return

    fetch_year = int(fetch_year)
    cal_content = calendar.calendar(fetch_year)

    title_label = Label(
        new_window,
        text=f"📅 Calendar - {fetch_year}",
        font=("Helvetica", 18, "bold"),
        bg="#fdfdfd",
        fg="#2c3e50",
    )
    title_label.pack(pady=10)

    text_area = Text(
        new_window,
        wrap=NONE,
        font=("Consolas", 10),
        bg="#ffffff",
        fg="#2c3e50",
        relief=SOLID,
        borderwidth=1,
    )
    text_area.insert(END, cal_content)
    text_area.config(state=DISABLED)
    text_area.pack(padx=20, pady=10, fill=BOTH, expand=True)

    # Add scrollbar
    scroll_y = Scrollbar(new_window, orient=VERTICAL, command=text_area.yview)
    text_area.config(yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x = Scrollbar(new_window, orient=HORIZONTAL, command=text_area.xview)
    text_area.config(xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM, fill=X)


# Main window
if __name__ == "__main__":
    root = Tk()
    root.title("📆 Calendar Application")
    root.geometry("500x400")
    root.config(bg="#f5f6fa")

    # Style configuration
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TButton",
        font=("Helvetica", 11, "bold"),
        padding=8,
        background="#2ecc71",
        foreground="black",
    )
    style.map(
        "TButton",
        background=[("active", "#27ae60")],
    )

    style.configure("TLabel", background="#f5f6fa", font=("Helvetica", 12))

    # Title Label
    title = Label(
        root,
        text="Welcome to the Calendar App",
        font=("Helvetica", 20, "bold"),
        bg="#f5f6fa",
        fg="#2c3e50",
    )
    title.pack(pady=30)

    # Year entry section
    frame = Frame(root, bg="#f5f6fa")
    frame.pack(pady=10)

    year_label = Label(frame, text="Enter Year:", font=("Helvetica", 14), bg="#f5f6fa")
    year_label.grid(row=0, column=0, padx=10, pady=5)

    year_field = Entry(frame, font=("Helvetica", 14), width=10, justify="center")
    year_field.grid(row=0, column=1, padx=10, pady=5)

    # Buttons
    button_frame = Frame(root, bg="#f5f6fa")
    button_frame.pack(pady=20)

    show_btn = ttk.Button(button_frame, text="Show Calendar", command=showCal)
    show_btn.grid(row=0, column=0, padx=10)

    exit_btn = ttk.Button(button_frame, text="Exit", command=root.destroy)
    exit_btn.grid(row=0, column=1, padx=10)

    # Footer
    footer = Label(
        root,
        text="Created with ❤️ using Tkinter",
        bg="#f5f6fa",
        fg="#7f8c8d",
        font=("Helvetica", 10),
    )
    footer.pack(side=BOTTOM, pady=10)

    root.mainloop()
