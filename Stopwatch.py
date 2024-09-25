import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print(f"Stopwatch stopped. Elapsed time: {self.format_time(self.elapsed_time)}")
        else:
            print("Stopwatch is not running.")

    def reset(self):
        if self.running:
            self.running = False
        self.elapsed_time = 0
        print("Stopwatch has been reset.")

    def elapsed(self):
        if self.running:
            return time.time() - self.start_time
        return self.elapsed_time

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"

# User interface for the stopwatch
def stopwatch_ui():
    stopwatch = Stopwatch()
    while True:
        print("\nOptions:")
        print("1. Start Stopwatch")
        print("2. Stop Stopwatch")
        print("3. Reset Stopwatch")
        print("4. Show Elapsed Time")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            stopwatch.start()
        elif choice == "2":
            stopwatch.stop()
        elif choice == "3":
            stopwatch.reset()
        elif choice == "4":
            print(f"Elapsed time: {stopwatch.format_time(stopwatch.elapsed())}")
        elif choice == "5":
            print("Exiting stopwatch. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the stopwatch interface
if __name__ == "__main__":
    stopwatch_ui()
