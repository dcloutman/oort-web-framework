#####################################
### Flask Standard Configurations ###
#####################################

########################
### MySQL Connection ###
########################
db_name = 'my_app'
"""
Change this to something appropriate for your application.
"""

db_user = 'oort_app'
"""
Choose a username to your database for your application that is difficult for adversaries guess. Do not use `root`.

Ideally, you should create a separate user for making schema changes and deny the user listed above the ability to make schema changes to the database.
"""

db_pw = 'notag00dPW-changeme'
"""
Definitely change this password to something highly randomized.
"""


#####################
### Oort Specific ###
#####################

OVERRIDE_FROM_ENVIRONMENT_VARIABLES = True
"""
If set to True, environment variables will be inspected and any variable that has a name matching one of the configuration variables will take the value of the environment variable.
"""
