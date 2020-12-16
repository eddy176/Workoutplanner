import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from workouts_db import WorkoutsDB



class RequestHandler(BaseHTTPRequestHandler): #include base class BashHTTP to my class

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, PUT, UPDATE, OPTIONS")
        self.send_header("Access-Allow-Control-Headers",  "Content-Type")
        self.end_headers()

    def do_GET(self):
        print("Path is", self.path)
        if self.path == "/workouts":
            self.handleWorkoutsRetrieveCollection()
        elif self.path.startswith("/workouts/"):
            self.handleWorkoutsRetrieveMember()
        else:
            self.handleNotFound()

    def do_DELETE(self):
        if self.path.startswith("/workouts/"):
            self.handleWorkoutsDeletemember()
        else:
            self.handleNotFound()

    def do_PUT(self):
        if self.path.startswith("/workouts/"):
            self.handleWorkoutsUpdateMember()
        else:
            self.handleNotFound

    def do_POST(self):
        print("Path is", self.path)
        if self.path == "/workouts":
            self.handleWorkoutsCreate()
        else:
            self.handleNotFound()

    def handleNotFound(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes("Not found.", "utf-8"))
    
    def handleWorkoutsRetrieveCollection(self):
        #respon accordingly
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        #send body
        db = WorkoutsDB()
        workouts = db.getWorkouts()
        self.wfile.write(bytes(json.dumps(workouts), "utf-8"))
    
    def handleWorkoutsRetrieveMember(self):
        parts = self.path.split("/")
        workout_id = parts[2]
        db = WorkoutsDB()
        workout = db.getOneWorkout(workout_id)
        print("workout", workout)
        if workout != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(workout), "utf-8"))
        else: 
            self.handleNotFound()
    
    def handleWorkoutsDeletemember(self):
        parts = self.path.split("/")
        workout_id = parts[2]
        print("id", workout_id)
        
        db = WorkoutsDB()
        exists = db.getOneWorkout(workout_id)
        if exists != None:
            db.deleteOneWorkout(workout_id)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
        else:
            self.handleNotFound()


    def handleWorkoutsCreate(self):
        #read the body 
        length = self.headers["Content-Length"]
        body = self.rfile.read(int(length)).decode("utf-8")
        print("BODY: ", body)

        #parse body into dictionary using parse_qs()
        parsed_body = parse_qs(body)
        name = parsed_body["name"][0]
        sets = parsed_body["sets"][0]
        reps = parsed_body["reps"][0]
        tut = parsed_body["tut"][0]
        rest = parsed_body["rest"][0]

        db = WorkoutsDB()
        db.insertWorkout(name, sets, reps, tut, rest)
       
        #respond to the client
        self.send_response(201)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
    
    def handleWorkoutsUpdateMember(self):
        parts = self.path.split("/")
        workout_id = parts[2] 
        print ("parts", parts)
       
        print("workout id", workout_id)
        length = self.headers["Content-Length"]
        print("length: ", length)
        body = self.rfile.read(int(length)).decode("utf-8")
        print("BODY: ", body)

        #parse body into dictionary using parse_qs()
        parsed_body = parse_qs(body)
        print("parsed body", parsed_body)
        name = parsed_body["name"][0]
        sets = parsed_body["sets"][0]
        reps = parsed_body["reps"][0]
        tut = parsed_body["tut"][0]
        rest = parsed_body["rest"][0]

        print("id", workout_id)
        db = WorkoutsDB()
 
        exists = db.getOneWorkout(workout_id)
        if exists != None:
            db.updateOneWorkout(workout_id, name, sets, reps, tut, rest)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
        else:
            self.handleNotFound()
        
def run():
    db = WorkoutsDB()
    db.createWorkoutsTable()
    db = None

    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    listen = ("0.0.0.0", port)


    server= HTTPServer(listen, RequestHandler)
    
    print("listening on ", "{}:{}".format(*listen) )
    server.serve_forever()
run()




