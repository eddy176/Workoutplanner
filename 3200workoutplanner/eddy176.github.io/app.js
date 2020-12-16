
var BASE_URL = "https://my-workout-planner.herokuapp.com";
//add button and text box to send workouts to server
var addButton = document.querySelector("#add"); //create add button so users can add workouts
addButton.onclick = function () {
    var newWorkoutName = document.querySelector("#new-workout-name").value;
    var newWorkoutSets = document.querySelector("#new-workout-sets").value;
    var newWorkoutReps = document.querySelector("#new-workout-reps").value;
    var newWorkoutTut = document.querySelector("#new-workout-tut").value;
    var newWorkoutRest = document.querySelector("#new-workout-rest").value;

    var bodystr = "name=" + encodeURIComponent(newWorkoutName);
    bodystr += "&sets=" + encodeURIComponent(newWorkoutSets);
    bodystr += "&reps=" + encodeURIComponent(newWorkoutReps);
    bodystr += "&tut=" + encodeURIComponent(newWorkoutTut);
    bodystr += "&rest=" + encodeURIComponent(newWorkoutRest);

    fetch( BASE_URL + "/workouts", {
        method: "POST",
        body: bodystr,
        headers: {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        
      }).then(getWorkouts)

};

var updateWorkoutbutton = document.querySelector("#update");
updateWorkoutbutton.onclick = function () {
    var workoutid = document.querySelector("#update-workout-id").value;
    console.log("workoutid", workoutid);
    var newWorkoutName = document.querySelector("#update-workout-name").value;
    var newWorkoutSets = document.querySelector("#update-workout-sets").value;
    var newWorkoutReps = document.querySelector("#update-workout-reps").value;
    var newWorkoutTut = document.querySelector("#update-workout-tut").value;
    var newWorkoutRest = document.querySelector("#update-workout-rest").value;

    var bodystr = "workoutid=" + encodeURIComponent(workoutid);
    bodystr += "&name=" + encodeURIComponent(newWorkoutName);
    bodystr += "&sets=" + encodeURIComponent(newWorkoutSets);
    bodystr += "&reps=" + encodeURIComponent(newWorkoutReps);
    bodystr += "&tut=" + encodeURIComponent(newWorkoutTut);
    bodystr += "&rest=" + encodeURIComponent(newWorkoutRest);
    console.log("bodystring", bodystr);
    
    fetch( BASE_URL + "/workouts/" + workoutid, {
        method: "PUT",
        body: bodystr,
              headers: {
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    }).then( getWorkouts);

};


var deleteWorkout = function (workoutId) {
  fetch( BASE_URL + "/workouts/" + workoutId, {
      method: "DELETE",
      headers: {
        "Content-Type" : "application/x-www-form-urlencoded"
    }
  }).then( getWorkouts);
 
};

function getWorkouts () {
    fetch(BASE_URL + "/workouts").then(function (response) {
        response.json().then(function (data) {
          console.log("data received from server:", data);
          
          
          // loop over the data and display it immediately:
          var workoutList = document.querySelector("#workouts");
          workoutList.innerHTML = "";

          data.forEach(function (workout) {
            // append each workout to a new element in the DOM
    
            // li tag: contains everything about one workout
            var newListItem = document.createElement("li");


            // h3 tag: contains the title 
            var titleHeading = document.createElement("h3");
            titleHeading.setAttribute("id", "nameid");
            titleHeading.innerHTML = workout.name;
            newListItem.appendChild(titleHeading);
          
    
            // div tag: contains the sets
            var setsDiv = document.createElement("div");
            setsDiv.setAttribute("id", "setsid");
            setsDiv.innerHTML = "Sets " + workout.sets;
            newListItem.appendChild(setsDiv);
            
            // div tag: contains reps
            var repsDiv = document.createElement("div");
            repsDiv.setAttribute("id", "repsid");
            repsDiv.innerHTML = "Reps " + workout.reps;
            newListItem.appendChild(repsDiv);

            // div tag: contains time under tension
            var tutDiv = document.createElement("div");
            tutDiv.setAttribute("id", "tutid");
            tutDiv.innerHTML =  "Tut " + workout.tut;
            newListItem.appendChild(tutDiv);

            // div tag: contains time rest
            var restDiv = document.createElement("div");
            restDiv.setAttribute("id", "restid");
            restDiv.innerHTML = "Rest " + workout.rest;
            newListItem.appendChild(restDiv);
    
            // button tag: the delete button
            var deleteButton = document.createElement("button");
            deleteButton.innerHTML = "Delete";
            deleteButton.setAttribute("id", "del");
            deleteButton.onclick = function () {
              console.log("delete clicked:", workout.id);
              if (confirm("Are you sure you want to delete " + workout.name + "?")) {
                deleteWorkout(workout.id);
                getWorkouts();
              }
            }
            var updateButton = document.createElement("button");
            updateButton.innerHTML = "Update";
            updateButton.setAttribute("id", "up");
            updateButton.onclick = function () {
              console.log("update clicked:", workout.id);
              getWorkout(workout.id);
              
            };
            newListItem.appendChild(updateButton);
            newListItem.appendChild(deleteButton);
            
            workoutList.appendChild(newListItem);
            
          });
        });
        
      });
      
    };
    getWorkouts();


var getWorkout = function (workoutId) {

  fetch(BASE_URL + "/workouts/" + workoutId).then(function (response) {
  response.json().then(function (data) { 
    var updateWorkoutId = document.querySelector("#update-workout-id");
    var updateWorkoutName = document.querySelector("#update-workout-name");
    var updateWorkoutSets = document.querySelector("#update-workout-sets");
    var updateWorkoutReps = document.querySelector("#update-workout-reps");
    var updateWorkoutTut = document.querySelector("#update-workout-tut");
    var updateWorkoutRest = document.querySelector("#update-workout-rest");
    console.log("workoutid150", workoutId);
    console.log("data150", data.id);
    updateWorkoutId.value = data.id;
    updateWorkoutName.value =  data.name;
    updateWorkoutSets.value = data.sets;
    updateWorkoutReps.value = data.reps;
    updateWorkoutTut.value = data.tut;
    updateWorkoutRest.value = data.rest;

  });
});




//query input
//input.field.value
//cors google first link reading
//rest api


};
