from datetime import datetime
import sys 

now = datetime.now()

original_stdout = sys.stdout # Save a reference to the original standard output

with open('hora.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.

    current_time = now.strftime("%H:%M")
    print("The current time is", current_time)

    sys.stdout = original_stdout # Reset the standard output to its original va>
