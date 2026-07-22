import csv, secrets, string, logging

# - filename='onboarding.log': Saves all log entries into a file named "onboarding.log".
# - level=logging.INFO: Sets the logging threshold to INFO, meaning INFO, WARNING, ERROR, and CRITICAL messages will be logged.
# - format: Defines the structure of each log line:
#     - %(asctime)s: Inserts a human-readable timestamp of when the event happened.
#     - %(message)s: Inserts the custom text message passed to the logger.
logging.basicConfig(filename='onboarding.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def gen_pass(length=12):
    """
    Generates a secure, random temporary password.
    
    Parameters:
        length (int): The number of characters in the password (defaults to 12).
        
    Returns:
        str: A randomly generated password string.
    """
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(secrets.choice(chars) for _ in range(length))

def onboard():
    """
    Reads an employee CSV file, formats user credentials, maps active directory / RBAC groups,
    prints a summary to the console, and logs the operation.
    """
    dept_groups = {"Finance": ["Sec-Grp-Finance", "M365-E5-Std"], "Engineering": ["Sec-Grp-Devs", "M365-E5-Dev"]}
    with open('employees.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = f"{row['Firstname'].lower()}.{row['Lastname'].lower()}@company.local"
            temp_pwd = gen_pass()
            groups = dept_groups.get(row['Department'], ["Sec-Grp-General"])
            welcome_msg = f"User: {username} | Pass: {temp_pwd} | Dept: {row['Department']} | Groups: {','.join(groups)}"
            print(welcome_msg)
            logging.info(f"Account provisioned for {username} in {row['Department']}")

if __name__ == '__main__':
    onboard()