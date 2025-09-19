# Student Personal Information
full_name = "Joshua Evans"
student_email = "jmevans8@aggies.ncat.edu"
Hometown = "Durham, NC"
grad_semester = "Spring 2029"
Major = "Computer Science"

# lists lines 7 to 10
current_courses = ["COMP 163", "COMP 121", "ENG 100", "HIS 106", "GEEN 111"]
completed_courses = ["none"]
current_credit_hours = [3, 3, 3, 3]
gpa_history = [4.0, 3.3, 3.6, 3.8]

# Tuples lines 12 to 16
emergency_contacts = ("Mom", "Beverly Williams", "704-555-0199")
home_adress = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@ayo.jex", 843)
twitter_info = ("Twitter", "@UnoJex", 25)
birthday = ("Birthday", 8, 8, 2007)

# sets go from line 18 to line 22
current_skills = {"Python basics", "Problem solving", "Time management", "Music Production"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Graphic Desgign"}
career_intrests = {"Software development", "Web development", "Data science", "Cyber Security"}
hobbies = {"Gaming", "Music Production", "Fashion", "Working Out", "Music"}
entertainment_backlog = {"One Piece", "Dexter"}

# dictionaries start at line 24 and end at line 29
course_credit_dict = {"COMP 163": 3, "COMP 121": 1, "ENG 100": 3, "HIS 106": 3, "GEEN 111": 1}
course_proffesor_dict = {"COMP 163": "Prof. Rhodes", "COMP 121": "Prof. Rhodes", "ENG 100": "Prof. Rhodes", "GEEN 111": "Prof. Parish", "HIS 106": "Prof. Devoe"}
course_room_dict = {"COMP 163": "M-Eric 300", "COMP 121": "Graham 210", "ENG 100": "Merrick 327", "HIS 106": "Online", "GEEN 111": "McNair 239"}
monthly_budget_dict = {"Food": 100, "Entertainment": 50, "Books": 0, "Transportation": 50}
per_subject_study_hours_dict = {"Programming": 10, "English": 4, "History": 3}
contact_directory_dict = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

# calculations
total_credits = sum(current_credit_hours)
cumultive_gpa = sum(gpa_history) / len(gpa_history)
completed_courses_count = len(completed_courses)
total_study_hours = sum(per_subject_study_hours_dict.values())
Academic_load = total_credits + total_study_hours
total_monthly_budget = sum(monthly_budget_dict.values())
daily_food_budget = monthly_budget_dict["Food"] / 30
annual_budget = total_monthly_budget * 12
Hourly_study_cost = monthly_budget_dict["Books"] / total_study_hours

# analytical calculations
total_social_followers = instagram_info[2] + twitter_info[2]
skills_comparison = len(current_skills) / len(skills_to_learn)
entertainment_backlog_number = len(entertainment_backlog)
current_hobbies_count = len(hobbies)

# prints out users information to create profile
print("================================================================")
print("             PERSONAL ACADEMIC & LIFE PORTFOLIO ")
print("================================================================")
print("Student:", full_name, "| Email:", student_email)
print("From:", Hometown, "| Graduating:", grad_semester)
print("Major:", Major)
print("=== ACADEMIC PROFILE ===")
print("Current Semester:", total_credits, "credits across", len(current_courses), "courses")
print(f"Cumulative GPA: {cumultive_gpa:.2f}")
print("Weekly Study Time:", total_study_hours, "hours")
print(f"Academic Investment: ${Hourly_study_cost:.1f} per study hour")
print("=== Current Courses ===")
print("COMP 163 -", course_credit_dict["COMP 163"], "credits -", course_proffesor_dict["COMP 163"], "-", course_room_dict["COMP 163"])
print("COMP 121 -", course_credit_dict["COMP 121"], "credits -", course_proffesor_dict["COMP 121"], "-", course_room_dict["COMP 121"])
print("ENG 100 -", course_credit_dict["ENG 100"], "credits -", course_proffesor_dict["ENG 100"], "-", course_room_dict["ENG 100"])
print("GEEN 111-", course_credit_dict["GEEN 111"], "credits -", course_proffesor_dict["GEEN 111"], "-", course_room_dict["GEEN 111"])
print("HIS 106 -", course_credit_dict["HIS 106"], "credits -", course_proffesor_dict["HIS 106"], "-", course_room_dict["HIS 106"])
print("=== PERSONAL DEVELOPMENT ===")
print("Current Skills:", current_skills)
print("Learning Goals:", skills_to_learn)
print("Career Interests:", career_intrests)
print("Skills Currently Have:", len(current_skills))
print("Skills Want to Learn:", len(skills_to_learn))
print("=== FINANCIAL OVERVIEW ===")
print("Monthly Budget: $", total_monthly_budget, sep="")
print("Food: $", monthly_budget_dict["Food"], " ($", f"{daily_food_budget:.1f}", "/day)", sep="")
print("Entertainment: $", monthly_budget_dict["Entertainment"], sep="")
print("Books: $", monthly_budget_dict["Books"], sep="")
print("Transportation: $", monthly_budget_dict["Transportation"], sep="")
print("Annual Projection: $", annual_budget, sep="")
print("=== CONNECTIONS & CONTACTS ===")
print("Emergency Contact:", emergency_contacts[1], "("+emergency_contacts[0]+") -", emergency_contacts[2])
print("Home Address:", home_adress[0], ",", home_adress[1], home_adress[2])
print("Social Media Presence:", total_social_followers, "followers across", len([instagram_info, twitter_info]), "platforms")
print("Key Contacts:", len(contact_directory_dict), "people in directory")
print("=== LIFE STATISTICS ===")
print("Total Courses Completed:", completed_courses_count)
print("Current Academic Load:", Academic_load, "weekly commitments")
print("Entertainment Backlog:", entertainment_backlog_number, "items")
print("Current Hobbies:", current_hobbies_count, "activities")
print("================================================================")