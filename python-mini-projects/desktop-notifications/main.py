from win10toast import ToastNotifier

n = ToastNotifier()

n.show_toast(
    "Python Project",
    "Here is your notification boyd",
    duration=10,
    icon_path='desktop-notifications\\logo.ico'
)