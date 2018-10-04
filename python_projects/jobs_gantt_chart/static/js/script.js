// static/js/script.js
var API_URL = 'http://localhost:5010/api/v1/etl_job_start_end';

var formatTime = function (input) {
	var dateParse = d3.timeParse("%Y-%m-%d %H:%M:%S");
	//var dateFormat = d3.time.format(formatOutput);
	return dateParse(input);
};


example();

function example() {
    var tasks = [];

    var taskStatus = {
	"SUCCESS" : "bar-blue",
	"ERROR" : "bar-red",
	"LOADING": "bar-green"
    };

    d3.json(API_URL, function(error, json) {
	if (error)
	    return console.warn(error);
	var taskNames = [];
	for ( var i = 0; i < json.length; i++) {
	    var processName = json[i]["etl_process_name"];
		var processStatus = json[i]["etl_process_status"];
		taskNames.push(processName);
		tasks.push({
		    "startDate" : new Date(json[i]["etl_process_start_time"]),
		    "endDate" : new Date(json[i]["etl_process_end_time"]),
		    "taskName" : processName,
		    "status" : processStatus
		});
	 
	}
	//var format = "%b-%e-%y";
	var format = "%m/%d %H:%M";
	var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
	//var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus)
	gantt(tasks);
    });

};

/*
var inter = setInterval(function () {
	updateData();
}, 5000);

*/
