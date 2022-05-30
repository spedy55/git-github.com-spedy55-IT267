
def turnon():
    global switch_status
    switch_status = True


def turnoff():
    global switch_status
    switch_status = False

switch_status = False
print(f'Status = {switch_status}')
turnon()
print(f'Status = {switch_status}')
turnoff()
print(f'Status = {switch_status}')
turnoff()
print(f'Status = {switch_status}')