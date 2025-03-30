
def user_input(message):
    cmd, *args = message.split()
    cmd = cmd.strip().lower()
    return cmd, *args

