class UserProfile:

    def __init__(self, profile_image=None, name="No name yet"):
        self.biography = None
        self.skills = None
        self.experience = None
        self.profile_image = profile_image
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def name(self, value):
        self.__name = value


def get_profile():
    user_profile = UserProfile("images/david.jpg", "David Johnson")
    user_profile.biography = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
                              "Suspendisse nunc eros, faucibus non porta nec, interdum non mauris."

    user_profile.skills = "Python | C# | Java | C | C++"
    user_profile.experience = [("Software Engineer", "Sed ultricies, dolor eu mattis molestie, felis libero"),
                               ("Systems Analyst", "Sed odio lorem, commodo ut dictum in, ullamcorper sit amet")]
    return user_profile





