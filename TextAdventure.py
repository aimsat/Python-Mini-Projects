# Simple Text-Based Adventure Game

def intro():
    print("Welcome, brave adventurer!")
    print("You find yourself at the entrance of a dark forest, known to be full of danger and mystery.")
    print("Will you venture into the forest or return to the safety of your village?")
    
    while True:
        choice = input("Enter 'forest' to go into the forest or 'village' to return to the village: ").lower()
        if choice == 'forest':
            forest_path()
            break
        elif choice == 'village':
            print("You return to the village, living a peaceful but uneventful life. The adventure ends.")
            break
        else:
            print("Invalid choice. Please type 'forest' or 'village'.")

def forest_path():
    print("\nYou venture into the forest and soon come to a fork in the road.")
    print("To the left, the path leads to a deep cave.")
    print("To the right, the path leads toward a shimmering river.")
    
    while True:
        choice = input("Enter 'cave' to explore the cave or 'river' to go to the river: ").lower()
        if choice == 'cave':
            cave_path()
            break
        elif choice == 'river':
            river_path()
            break
        else:
            print("Invalid choice. Please type 'cave' or 'river'.")

def cave_path():
    print("\nYou enter the dark cave, and the air grows cold.")
    print("Suddenly, you hear the sound of something moving in the darkness.")
    print("Do you investigate the sound or run back to the forest?")
    
    while True:
        choice = input("Enter 'investigate' to check out the sound or 'run' to run back to the forest: ").lower()
        if choice == 'investigate':
            print("\nYou move toward the sound and discover a hidden treasure chest! You open it and find gold.")
            print("Congratulations, you have found treasure and your adventure is a success!")
            break
        elif choice == 'run':
            print("\nYou run out of the cave and back to the safety of the forest.")
            forest_path()
            break
        else:
            print("Invalid choice. Please type 'investigate' or 'run'.")

def river_path():
    print("\nYou approach the river and see a boat tied to the shore.")
    print("You also notice a bridge that crosses the river.")
    print("Do you take the boat or cross the bridge?")
    
    while True:
        choice = input("Enter 'boat' to take the boat or 'bridge' to cross the bridge: ").lower()
        if choice == 'boat':
            print("\nYou take the boat and sail down the river. Suddenly, the boat capsizes, and you struggle in the water.")
            print("After a difficult swim, you manage to reach the shore, but you are exhausted. The adventure ends.")
            break
        elif choice == 'bridge':
            print("\nYou cross the bridge and find a peaceful meadow on the other side.")
            print("In the meadow, you find a magical sword stuck in the ground. You pull the sword free and feel its power.")
            print("Congratulations, you have found the Sword of Destiny and your adventure is a success!")
            break
        else:
            print("Invalid choice. Please type 'boat' or 'bridge'.")

# Start the game
if __name__ == "__main__":
    intro()
