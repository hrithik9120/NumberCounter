## Windows Task Scheduler Setup

1. Clone this repository:

```bash
fork and clone https://github.com/Shogun89/fancy_job
cd fancy_job
```

2. Run the script manually for the first time to verify it works:

```bash
python update_number.py
```

3. Set up a Task Scheduler job to run the script daily:

- Open Task Scheduler and create a new task.
- Name the task and set the trigger to run daily at a time of your choice.
- In the "Actions" tab, create a new action to start a program.
- Set the program/script to `python` and add the path to `update_number.py` in the "Add arguments" field.
- Set the "Start in" field to the directory containing `update_number.py`.

4. Optional: If you prefer to ensure the script runs at a fixed time initially, you can manually set up the task to run at a specific time.

This will run the script at the specified time daily.

## Usage

The script will increment the number in `number.txt` and commit the change to git. You can modify the script to increment by any value or use a different file to store the number.