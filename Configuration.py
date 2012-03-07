import Authentication
import os

class ConfigurationManager():
    """Provides an interface to access and configure the extension settings
    """
    
    def __init__(self):
        """
        """
        self._am=Authentication.AccountManager()
        

    def get_account(self):
        """Returns the current selected account
        """
        #TODO: Properly implement the functionality to get the 
        #account from a persistence location

        account=self._am.get_accounts().pop()
        return account

    def get_system_path(self, ):
        """Returns the path of the place where the python scripts are
        """
        return os.path.expanduser('~')+'/4sep/'

    def set_proxy(self, url,port):
        """
        Sets proxy for the environment of the script
        
        Arguments:
        - `url`:URL of the proxy server
        - `port`:port of the proxy server
        """
        
        os.environ['http_proxy']=url+":"+port
        os.environ['https_proxy']=url+":"+port
