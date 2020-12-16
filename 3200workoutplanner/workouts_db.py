import os
import psycopg2
import psycopg2.extras
import urllib.parse

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class WorkoutsDB:
    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

        self.connection = psycopg2.connect(
            cursor_factory=psycopg2.extras.RealDictCursor,
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def createWorkoutsTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS workouts (id SERIAL PRIMARY KEY, name TEXT, sets INTEGER, reps INTEGER, tut TEXT, rest TEXT)")
        self.connection.commit()

    def insertWorkout(self, name, sets, reps, tut, rest):
        data = [name, sets, reps, tut, rest]
        self.cursor.execute("INSERT INTO workouts (name, sets, reps, tut, rest) VALUES (%s,%s,%s,%s,%s)", data)
        self.connection.commit()
        return None

    def getWorkouts(self):
        self.cursor.execute("SELECT * FROM workouts ORDER BY id")
        result = self.cursor.fetchall() #return as list of dictionaries it is a list of tuples now (row_factory python sqlite3)
        return result
    
    def getOneWorkout(self, workout_id):
        data = [workout_id]
        self.cursor.execute("SELECT * FROM workouts WHERE id = %s", data)
        result = self.cursor.fetchone()
        return result

    def deleteOneWorkout(self, workout_id):
        data = [workout_id]
        print("data", data)

        self.cursor.execute("DELETE FROM workouts WHERE id = %s", data)
        self.connection.commit()
        return None

    def updateOneWorkout(self, workout_id, name, sets, reps, tut, rest):
        
        data = [name, sets, reps, tut, rest, workout_id]
        self.cursor.execute("UPDATE workouts SET name = %s, sets = %s, reps = %s, tut = %s, rest = %s WHERE id = %s", data)
        self.connection.commit()
        return None
    
    

#print(result[0][0]) #print first item out of first tuple
#print(cursor.fetchall()) #prints out list of tuples











