import random
import subprocess
import os
import datetime as dt


def git_commit_and_push():
    try:
        # Stage the changes
        subprocess.run(['git', 'add', 'number.txt'], check=True)

        # Create commit with current date
        date = dt.datetime.now().strftime('%Y-%m-%d')
        commit_message = f"Update number: {date}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        # Push the changes
        subprocess.run(['git', 'push'], check=True)
        print("Changes committed and pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")


def read_number():
    try:
        with open('number.txt', 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def write_number(number):
    with open('number.txt', 'w') as file:
        file.write(str(number))

def main():
    try:
        # Increment the number in 'number.txt'
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)

        # Commit and push the changes to GitHub
        git_commit_and_push()

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()