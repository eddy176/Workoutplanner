
# _Workout Planner_

  

## _Resource_

  

### Attributes

  

* Name (string)
*  Sets (integer)
* Reps (integer)
* Tut (string)
* Rest (string)

 ### Schema

       CREATE TABLE workouts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        sets INTEGER,
        reps INTEGER,
        tut TEXT,
        rest TEXT);
        
### REST Endpoints

Name | Method | Path
---- | ------ | ----
Retrieve Workout Collection | GET | /workouts
Retrieve Workout Member | GET | /workouts/*id*
Create Workout Member | POST | /workouts
Update Workout Member | PUT | /workout/*id*
Delete Workout Member | DELETE | /workout/*id*
