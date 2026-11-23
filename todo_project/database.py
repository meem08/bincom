import psycopg2

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="todo_db",
            user="todo_user",
            password="1234"
        )

        print("Database connection successful!")
        return connection

    except psycopg2.Error as error:
        print("Database connection failed:", error)
        return None


connect_db()

def add_task(title, description):
    connection = connect_db()

    if connection:
        try:
            cursor = connection.cursor()

            query = """
               INSERT INTO tasks (title, description)
               VALUES (%s, %s)
            """
            cursor.execute(query, (title, description))
            connection.commit()

            print("Task added successfully!")
            
        except psycopg2.Error as error:
            print("Error adding task:", error)
        finally:
            cursor.close()
            connection.close()


def view_tasks():
    connection = connect_db()

    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(f"ID: {task[0]}")
                    print(f"Title: {task[1]}")
                    print(f"Description: {task[2]}")
                    print(f"Completed: {task[3]}")
                    print("----------------------")
        except psycopg2.Error as error:
            print("Error retrieving tasks:", error)
        finally:
            cursor.close()
            connection.close()

def update_task(task_id, new_title):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            query ="""
               UPDATE tasks
               SET title = %s
               WHERE id = %s
            """

            cursor.execute(query, (new_title, task_id))
            connection.commit()

            if cursor.rowcount > 0:
                print("Task updated successfully")
            else:
                print("Task not found.")
        except psycopg2.Error as error:
            print("Erroor updating task:", error)
        finally:
            cursor.close()
            connection.close()

def complete_task(task_id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            query = """
               UPDATE tasks
               SET completed = TRUE
               WHERE id = %s
            """
            cursor.execute(query, (task_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
               print("Task updated successfully!")
            else:
               print("Task not found.")
        except psycopg2.Error as error:
            print("Error updating task:", error)
        finally:
            cursor.close()
            connection.close()

def delete_task(task_id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            query = """
                DELETE FROM tasks
                WHERE id = %s;
            """
            cursor.execute(query, (task_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("Task successfully deleted!")
            else:
                print("Task not found.")

        except psycopg2.Error as error:
            print("Error in deleting task", error)
            
        finally:
            cursor.close()
            connection.close()

def ask_for_id():
    value = input("Task ID: ").strip()
    if not value.isdigit():
        print("Please enter a number.")
        return None
    return int(value)


def main():
    menu = """
==== TO-DO LIST ====
1. View tasks
2. Add task
3. Edit task title
4. Mark task complete
5. Delete task
6. Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            title = input("Title: ").strip()
            if not title:
                print("Title can't be empty.")
                continue
            description = input("Description (optional): ").strip()
            add_task(title, description)
        elif choice == "3":
            task_id = ask_for_id()
            if task_id is not None:
                new_title = input("New title: ").strip()
                if new_title:
                    update_task(task_id, new_title)
                else:
                    print("Title can't be empty.")
        elif choice == "4":
            task_id = ask_for_id()
            if task_id is not None:
                complete_task(task_id)
        elif choice == "5":
            task_id = ask_for_id()
            if task_id is not None:
                confirm = input(f"Delete task {task_id}? (y/n): ").strip().lower()
                if confirm == "y":
                    delete_task(task_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try 1-6.")


if __name__ == "__main__":
    main()