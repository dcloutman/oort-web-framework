class AuthUser():
    """
    Flask Login requires a class with this signature to generate the session.
    """
    
    def __init__ (self, user_id):
        self.is_authorized = True
        """
        This property should return True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)
        """

        self.is_active = True
        """
        This property should return True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).
        """

        self.is_anonymous = True
        """
        This property should return True if this is an anonymous user. (Actual users should return False instead.)
        """

        self.user_id = user_id

    def get_id(self):
        return self.user_id
    
    
    