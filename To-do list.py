import uuid

filename = 'todo-list-data.txt'

def add_task():
    print('\n[ADD TASK]')
    task = input('What is the task? ')
    deadline = input('What is the deadline? ')
    
    try:
        stream = open(filename, 'a')
        stream.write(str(uuid.uuid4()) + ';' + task.replace(';', '') + ';' + deadline.replace(';', '') + '\n')
        stream.close()
    except Exception as e:
        print('Error while adding task:', e)
    finally:
        print()

def complete_task():
    print('\n[COMPLETE TASK]')
    if show_tasks() > 0:
        id_to_delete = input('Enter id to complete: ')
        try:
            stream = open(filename, 'r')
            lines = stream.readlines()
            stream.close()
            stream = open(filename, 'w')
            for line in lines:
                if not line.startswith(id_to_delete):
                    stream.write(line)
            stream.close()
        except Exception as e:
            print('Error while adding task:', e)
        finally:
            print()
    else:
        print('No tasks to complete\n')

def show_tasks():
    print('\n[YOUR TASKS]')
    try:
        stream = open(filename, 'r')
        tasks = stream.readlines()
        if len(tasks) == 0:
            print('Empty list\n')
            return 0
        for task in tasks:
            task_elements = task.split(';')
            print(' | '.join(task_elements), end='')
        print()
        return len(tasks)
    except Exception as e:
        if e.errno == 2:
            print('Empty list\n')
            return 0
        else:
            print('Error while adding task:', e)
            return 0

def show_menu():
    while True:
        print('== TODO LIST ==')
        choice = input('[1] show tasks\n[2] add task\n[3] complete task\n[4] exit\nYour choice: ')

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print('Enter a correct number')

if __name__ == '__main__':
    show_menu()
