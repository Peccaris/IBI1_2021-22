class Staff:  # create a class called 'Staff'
    def __init__(self, first_name, last_name, location, role):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.role = role

    def information(
        self
    ):  # a function which prints the staff members' full name, their location and their role
        print(self.first_name, self.last_name, ',', self.location, ',',
              self.role)

# an example of using this class:
current_staff = Staff('Robort', 'Young', 'Edinburgh', 'faculty')
current_staff.information()