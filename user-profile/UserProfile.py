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






