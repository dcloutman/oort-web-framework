#####################################
### Flask Standard Configurations ###
#####################################

SECRET_KEY="X0LFpiJ87U!hB%0o2ku7dyRW?hUB9N7tfO^Ry~Qiqsz/J##R~4)|>7fCMs9nXlwKUf#u31n&TfR{ew^vS)i:s5mOQQi7b4s1MUOmfU-iIH@Nvi>rh5f(I@&yK#H@HA^E"
"""
A secret key that will be used for securely signing the session cookie and can be used for any other security related needs 
by extensions or your application. It should be a long random bytes or str.
"""

#####################
### Oort Specific ###
#####################

APP_ROUTE_PREFIX='/'
"""
Change this if you want to run this application to appear as if it runs out of a subdirectory of your server.
"""

OVERRIDE_FROM_ENVIRONMENT_VARIABLES = True
"""
If set to True, environment variables will be inspected and any variable that has a name matching one of the configuration variables will take the value of the environment variable.
"""
