"""The dictionary of subjects and respective teachers"""
subjects_teachers = {
    "Science": {"teachers": ["Miss Kenya", "Mr Asad", "Miss Sevinch"]},
    "Technology": {"teachers": ["Miss Madina", "Mr Omad", "Miss Zarina"]},
    "Engineering": {"teachers": ["Miss Oygul", "Mr Rasul", "Mr Amir"]},
    "Art": {"teachers": ["Miss Shaxzoda", "Mr Kevin", "Mr Smith", "Miss Elina"]},
    "Math": {"teachers": ["Miss Sevara", "Mr Shokir", "Miss Komil"]},
}

#The dictionary of buildings and respective rooms
buildings_rooms = {
    'IOP': ["IOP4", "IOP5", "IOP6", "IOP10", "IOP9"],
    'BIN': ["BIN4", "BIN5", "BIN6", "BIN10", "BIN9"],
    "SOB": ["SOB1", "SOB6", "SOB4", "SOB2", "SOB4"]
}

#The list of periods that are divided into 10 slots
time_before_break = ["8:00 - 8:55", "9:00 - 9:55", "10:00 - 10:55", "11:00 - 11:55"]
time_after_break = ["13:00 - 13:55", "14:00 - 14:55", "15:00 - 15:55", "16:00 - 16:55", "17:00 - 17:55"]


#The list of classses
classes = ["5", "6", "7", "8", "9", "10", "11"]

#The list of groups
groups = ["EU", "US", "UK", "RF"]

#The list where the result of the inputs will be stored
timetable_results = []


"""The input of subject. User should enter the number in order to select the subject"""
def choose_subject():
    subject_list = list(subjects_teachers.keys())
    #Enumerate function is responsible for numerating the keys of the list
    for idx, subject in enumerate(subject_list):
        print(f"{idx + 1}. {subject}")


    while True:   #Input with the validation
        get_subject = int(input("\nChoose the subject by its number: "))
        if 1 <= get_subject <= len(subject_list):
            chosen_subject = subject_list[get_subject - 1]
            print(f"\nYou chose: {chosen_subject}")
            return chosen_subject
        else:
            print("Error: Invalid choice. Please enter a number from the list!.")


"""The input of teacher. User should enter the number in order to select the teacher"""
def choose_teacher(subject):
    teachers = subjects_teachers[subject]["teachers"]
    print("\nTeachers for this subject are:")
    for idx, teacher in enumerate(teachers):
        print(f"{idx + 1}. {teacher}")

    while True:   #Input with the validation
        get_teacher = int(input("\nChoose the teacher by its number: "))
        if 1 <= get_teacher <= len(teachers):
            chosen_teacher = teachers[get_teacher - 1]
            print(f"\nYou chose: {chosen_teacher}")
            return chosen_teacher
        else:
            print("Error: Invalid choice. Please enter a number from the list!")

"""The input of class. User should enter the number in order to select the class"""
def choose_class():
    for idx, _class in enumerate(classes):
        print(f"{idx + 1}. {_class}")

    while True:   #Input with the validation
        get_class = int(input("\nChoose the class: "))
        if 1 <= get_class <= len(classes):
            chosen_class = classes[get_class - 1]
            print(f"\nChosen class: {chosen_class}")
            return chosen_class
        else:
            print("Error: Invalid choice. Please enter a valid number from the list!")

"""The input of group. User should enter the number in order to select the group"""
def choose_group():
    for idx, group in enumerate(groups):
        print(f"{idx + 1}. {group}")

    while True:    #Input with the validation
        get_group = int(input("\nChoose the group: "))
        if 1 <= get_group <= len(groups):
            chosen_group = groups[get_group - 1]
            print(f"\nChosen group: {chosen_group}")
            return chosen_group
        else:
            print("Error: Invalid choice. Please enter a valid number!")


"""The input of time. User should enter the number in order to select the time"""
def choose_time():
    # Ask the user if they want to choose a time before or after the break
    while True:  
        period = input("\nIs the lesson before or after the break? (Enter 'a' for before or 'b' for after): ").strip().lower()
        
        # Determine the correct time slots based on user input
        if period == 'b':
            time_slots = time_before_break
            break
        elif period == 'a':
            time_slots = time_after_break
            break
        else:
            print("Error: Please enter 'a' for 'after break' or 'b' for 'before break'!")

    # Showing the appropriate time slots according to the answer of period input 
    for idx, time in enumerate(time_slots):
        print(f"{idx + 1}. {time}")

    # Ask the time 
    while True:
        get_time = int(input("\nChoose the time by its number: "))
        if 1 <= get_time <= len(time_slots):
            chosen_time = time_slots[get_time - 1]
            print(f"\nChosen time: {chosen_time}")
            return chosen_time
        else:
            print("Error: Invalid choice. Please enter a number from the list!")

"""The input of building and respective room. User should enter the number in order to select the both of them"""
def choose_building_room(): #Shows the list
    building_list = list(buildings_rooms.keys())
    for idx, building in enumerate(building_list):
        print(f"{idx + 1}. {building}")

    while True:  #Input with validation
        get_building = int(input("\nChoose the building: "))
        if 1 <= get_building <= len(building_list):
            chosen_building = building_list[get_building - 1]
            print(f"\nChosen building: {chosen_building}")
            break
        else:
            print("Error: Invalid choice. Please enter a number from the list!")
    
    rooms = buildings_rooms[chosen_building]   #According to the answer of input chosen_building shows the respective rooms
    for idx, room in enumerate(rooms):
        print(f"{idx + 1}. {room}")

    while True:    #Input with validation
        get_room = int(input("\nChoose the room: "))
        if 1 <= get_room <= len(rooms):
            chosen_room = rooms[get_room - 1]
            print(f"\nChosen room: {chosen_room}")
            return chosen_building, chosen_room
        else:
            print("Error: Invalid choice. Please enter a valid number from the list!")


"""The whole result of the created timetable. Calls all the functions"""
def result():
    chosen_subject = choose_subject()
    chosen_teacher = choose_teacher(chosen_subject)
    chosen_class = choose_class()
    chosen_group = choose_group()
    chosen_time = choose_time()
    chosen_building, chosen_room = choose_building_room()

    # Store the timetable entry as a dictionary
    timetable_result = {
        "Time": chosen_time,
        "Group": chosen_group,
        "Building": chosen_building,
        "Room": chosen_room,
        "Lesson": chosen_subject,
        "Class": chosen_class,
        "Teacher": chosen_teacher
    }

    # Add the timetable entry to the list
    timetable_results.append(timetable_result)


    print("\nTimetable Result:")
    for key, value in timetable_result.items():
        print(f"{key}: {value}")

    # Ask if the user wants to create another timetable entry
    create_another = input("\nDo you want to create another timetable? (yes/no): ").lower()
    if create_another == "yes":
        result()
    else:
        # Display all timetable entries 
        print("\nTimetable result summary:")
        for entry_idx, entry in enumerate(timetable_results):
            print(f"\nEntry {entry_idx}:")
            for key, value in entry.items():
                print(f"{key}: {value}")
        print("\nThank you! Run the program again for another entries.")

if __name__ == "__main__":
    result()



