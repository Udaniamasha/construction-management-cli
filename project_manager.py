# Initialize empty lists and variables to store project details and worker count
ongoing_projects = []
completed_projects = []
on_hold_projects =[]
available_workers = 500

# Main program loop
while True:
    # Display the main menu options
    print("\nXYZ Company Main Menu")
    print("1. Add a new project to existing projects")
    print("2. Remove a completed project from existing projects")
    print("3. Add new workers to available workers group")
    print("4. Update details on ongoing projects")
    print("5. Project Statistics")
    print("6. Exit")

    # Ask for user input to choose an option
    choice = input("Your Choice: ")

    # Option 1: Add a new project
    if choice == '1':
        print("\nAdd a new project.")
        project_code = input("\nProject Code ('0' to exit): ")
        if project_code == '0':
            continue

        # Gather project details from user input
        client_name = input("Client's Name: ")
        start_date = input("Start date: ")
        end_date = input("Expected end date: ")
        num_workers = int(input("Number of workers: "))
        project_status = input("Project status (ongoing, on hold, completed): ").lower()
        

        # Check if enough workers are available for the new project
        if num_workers <= available_workers and project_status=='ongoing' :
            ongoing_projects.append({
                'Project Code': project_code,
                'Client Name': client_name,
                'Start Date': start_date,
                'End Date': end_date,
                'Number of Workers': num_workers,
                'Project Status': project_status
            })
            available_workers -= num_workers
            save_choice = input("Do you want to save the project (Yes/No)? ").lower()
            if save_choice == 'yes':
                print("Project added to ongoing projects.")
            else:
                ongoing_projects.pop()
                available_workers += num_workers
                print("Project not saved.")
        else:
            print("Insufficient workers available or invalid project status. Cannot undertake the project.")

    # Option 2: Remove a completed project
    elif choice == '2':
        print("\nRemove Completed Project")
        project_code = input("Project Code: ")
        for project in ongoing_projects:
            if project['Project Code'] == project_code:
                remove_choice = input("Do you want to remove the project (Yes/No)? ").lower()
                if remove_choice == 'yes':
                    completed_projects.append(project)
                    ongoing_projects.remove(project)
                    available_workers += project['Number of Workers'] 
                    print("Project removed and moved to completed projects.")
                else:
                        print("Project Not Removed")
                break
               
        else:
            print("Project not found or not completed.")

    # Option 3: Add new workers
    elif choice == '3':
        print("\nAdd new workers")
        num_workers = int(input("Number of workers to add: "))
        add_choice = input("Do you want to add Workers(Yes/No)? ").lower()
        if add_choice == 'yes':
            available_workers += num_workers
            print(f"{num_workers} workers added.")
        else:
            print("No workers added.")

    # Option 4: Update details of ongoing projects
    elif choice == '4':
        print("\nUpdate Project Details")
        project_code = input("Project Code ('0' to exit): ")
        if project_code == '0':
            continue

        for project in ongoing_projects:
            if project['Project Code'] == project_code:
                client_name = input("Client's Name: ")
                start_date = input("Start date: ")
                end_date = input("Expected end date: ")
                num_workers = int(input("Number of workers: "))
                project_status = input("Project status (ongoing, on hold, completed): ")

                update_choice = input("Do you want to update the project details (Yes/No)? ").lower()
                if update_choice == 'yes':
                    project['Client Name'] = client_name
                    project['Start Date'] = start_date
                    project['End Date'] = end_date
                    project['Number of Workers'] = num_workers
                    project['Project Status'] = project_status
                    if project_status =="completed":
                          completed_projects.append(project)
                          ongoing_projects.remove(project)
                          available_workers += project['Number of Workers']
                    elif project_status=="on hold":
                          on_hold_projects.append(project)
                          ongoing_projects.remove(project)
                          
                    print("Project details updated.")
                else:
                    print("Project details not updated.")

                #check the updated project status    

                    
                break
        else:
            print("Project not found.")

    # Option 5: Display project statistics
    elif choice == '5':
        print("\nProject Statistics")
        print(f"Number of ongoing projects: {len(ongoing_projects)}")
        print(f"Number of completed projects: {len(completed_projects)}")
        print(f"Number of on hold projects: {len(on_hold_projects)}")
        print(f"Number of available workers to assign: {available_workers}")

    # Option 6: Exit the program
    elif choice == '6':
        print("Exiting the program.")
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Please enter a valid option.")
