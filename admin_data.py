# Importing necessary modules:
import sys # type: ignore
import os # type: ignore

# Function to get the absolute path of a resource file:
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# List of available branches for students:
# NOTE: Update this list as needed to include or exclude branches offered in the institution.
branches = ['BAI', 'BAS', 'BBA', 'BCE', 'BCG',
            'BCY', 'BEC', 'BET', 'BEY', 'BHI',
            'BME', 'BMR', 'BOE', 'BSA', 'MBA',
            'MCA', 'MEI', 'MIM', 'MIP', 'MSI']

# System email credentials used for sending emails:
# NOTE: Replace with your email and app password (e.g., for Gmail, create an app password for SMTP use).
my_email = 'your-email@example.com' # Replace with your email.
my_password = 'your-app-password' # Replace with your app password.

# Admin account details:
# NOTE: Replace the placeholders below with your preferred admin username, password, and name.
admin_username = 'your-username' # Replace with your preferred admin username.
admin_password = 'your-password' # Replace with your preferred admin password.
admin_name = 'Your Name' # Replace with your preferred admin name.

# File paths for external resources (icons and database):
root_icon_path = resource_path('icons/silly_cat.ico')
student_login_icon_path = resource_path('icons/login_student_img.png')
admin_login_icon_path = resource_path('icons/admin_img.png')
add_student_icon_path = resource_path('icons/add_student_img.png')
locked_icon_path = resource_path('icons/locked_img.png')
unlocked_icon_path = resource_path('icons/unlocked_img.png')
add_student_pic_icon_path = resource_path('icons/add_img.png')
student_card_frame_path = resource_path('icons/student_card_frame_img.png')
temp_pic = resource_path('temp_data/temp_pic.png')
db_path = resource_path('temp_data/srms_database.db')