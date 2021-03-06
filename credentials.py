class Credentials:
    """
    Class that generates new instances of users.
    """
    credentials_list = []

    def __init__(self,credentials_name,name,password,email):
        self.credentials_name = credentials_name
        self.name = name
        self.password = password
        self.email = email

    
    def save_credentials(self):
        """
        Method to save credential objects into credentials list
        """  
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        A method that deletes credentials from the list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
         for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
             return credentials

    @classmethod
    def credentials_exist(cls,name):
        """
        """
        for credentials in cls.credentials_list:
            if credentials.password == name:
                    return credentials

        return False

    @classmethod
    def display_credentials(cls): 
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list       