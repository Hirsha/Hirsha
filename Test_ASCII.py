import pyfiglet

while True:
    text = input("Enter a text (or 'exit' to quit): ")
    
    if text.lower() == 'exit':
        break
    
    try:
        ascii_art = pyfiglet.figlet_format(text)
        print(ascii_art)
    except pyfiglet.FontNotFound:
        print("Invalid input. Please try again.")
