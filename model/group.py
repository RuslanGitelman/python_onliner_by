class Group:

    def __init__(self, baseUrl=None, username=None, password=None):
        self.baseUrl = baseUrl
        self.username = username
        self.password = password

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.baseUrl, self.username, self.password)
