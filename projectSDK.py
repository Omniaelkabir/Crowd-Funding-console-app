from project import Project
import sqlite3
import os.path

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(l, 'projects.db'))

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS projects
             (title TEXT, details TEXT, total_target INTEGER , start_time DATE, end_time DATE )''')

def cursor():
    
    l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return sqlite3.connect(os.path.join(l, 'projects.db')).cursor()

def add_project(project):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO projects VALUES (?, ?, ?, ?, ?)", (project.title, project.details, project.total_target, project.start_time, project.end_time))
    c.connection.close() 
    return c.lastrowid

def get_project_by_title(title):
    c = cursor()
    c.execute('SELECT * FROM projects WHERE title=?', (title,))
    data = c.fetchone()
    c.connection.close()

    if not data:
        return None

    return Project(data[0], data[1], data[2], data[3], data[4])


def get_project_by_date(start_time, end_time):
    c = cursor()
    c.execute('SELECT * FROM projects WHERE start_time=?', (start_time))
    data = c.fetchone()
    c.connection.close()

    if not data:
        return None

    return Project(data[0], data[1], data[2], data[3], data[4])    
        
def get_projects():
    c = cursor()
    projects = []
    for row in c.execute('SELECT * FROM projects'):
        projects.append(Project(row[0], row[1], row[2], row[3], row[4]))
    c.connection.close()
    return projects

def update_prokject(project, new_title, new_details, new_total_target, new_start_time, new_end_time):
    c = cursor()
    with c.connection: #don't forget this part.
        c.execute('UPDATE project SET title=?, detils=?, total_target=?, start_time=?, end_time=? WHERE title=? AND details=? AND total_target=? AND start_time=? AND end_time=?', 
        (new_title, new_details,new_total_target,new_start_time,new_end_time, project.title, project.details, project.total_target, project.start_time, project.end_time))
    project = get_project_by_title(project.title) #after commit
    c.connection.close()
    return project

def delete_project(project):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM projects WHERE title=?', (project.title))
    rows = c.rowcount
    c.connection.close()
    return rows
