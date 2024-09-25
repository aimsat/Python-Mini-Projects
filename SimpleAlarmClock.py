import time
import datetime

# Function to get the alarm time from the user
def set_alarm():
    while True:
        alarm_time = input("Set the alarm time (HH:MM:SS in 24-hour format): ")
        try:
            alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
            return alarm_time
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM:SS format.")

# Function to handle snooze functionality
def snooze():
    snooze_minutes = int(input("Enter snooze time in minutes: "))
    snooze_duration = datetime.timedelta(minutes=snooze_minutes)
    new_alarm_time = datetime.datetime.now() + snooze_duration
    print(f"Snooze set for {snooze_minutes} minutes. New alarm at {new_alarm_time.time().strftime('%H:%M:%S')}")
    return new_alarm_time.time()

# Main alarm clock loop
def alarm_clock():
    alarm_time = set_alarm()
    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        current_time = datetime.datetime.now().time()
        # Check if the current time matches the alarm time
        if current_time >= alarm_time:
            print("Wake up! It's time!")
            choice = input("Do you want to snooze? (yes/no): ").lower()
            if choice == 'yes':
                alarm_time = snooze()
            else:
                print("Alarm turned off. Have a great day!")
                break

        # Wait for 1 second before checking the time again
        time.sleep(1)

# Start the alarm clock
if __name__ == "__main__":
    alarm_clock()
