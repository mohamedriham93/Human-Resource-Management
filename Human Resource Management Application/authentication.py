# This entire application was created by Mohamed Riham from CSD21 Batch.
# ID = 1028401
def authenticate(username, password):

    with open('Credential/Stored Credentials.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:

            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
        return False
