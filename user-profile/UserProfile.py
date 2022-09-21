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
                              "Suspendisse nunc eros, faucibus non porta nec, interdum non mauris. " \
                              "Phasellus posuere, mi quis faucibus elementum, tellus sem placerat neque, " \
                              "non consequat massa ligula vel tortor."
    user_profile.skills = "Python | C# | Java | C | C++"
    user_profile.experience = [("Software Engineer", "Sed ultricies, dolor eu mattis molestie, felis libero "
                                                     "vulputate diam, quis ultricies nulla massa in diam."),
                               ("Systems Analyst", "Sed odio lorem, commodo ut dictum in, ullamcorper sit amet "
                                                   "metus. Donec metus ipsum, fermentum ac ultricies ac, ultricies "
                                                   "a diam.")]
    return user_profile





