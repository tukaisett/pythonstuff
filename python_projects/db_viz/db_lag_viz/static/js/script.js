// static/js/script.js
var API_URL = 'http://localhost:5010/api/v1/lag_times';

var formatTime = function (input) {
	var dateParse = d3.timeParse("%Y-%m-%d %H:%M:%S");
	//var dateFormat = d3.time.format(formatOutput);
	return dateParse(input);
};


var svg = d3.select("svg"),
	margin = {
		top: 20,
		right: 20,
		bottom: 30,
		left: 50
	},
	width = +svg.attr("width") - margin.left - margin.right,
	height = +svg.attr("height") - margin.top - margin.bottom,
	g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleTime()
	.rangeRound([0, width]);

var y = d3.scaleLinear()
	.rangeRound([height, 0]);

var line = d3.line()
	.x(function (d) {
		return x(d.reading_date_time);
	})
	.y(function (d) {
		return y(d.reading_lag_time);
	});

// define the area
var area = d3.area()
	.x(function (d) {
		return x(d.reading_date_time);
	})
	.y0(height)
	.y1(function (d) {
		return y(d.reading_lag_time);
	});

//console.log(formatTime("2018-08-18 00:00:39", "%Y-%m-%d %H:%M:%S"));

// This needs to be changed to my API request
d3.json(API_URL, function (error, data) {

	//console.log(data);
	//var data = d.Data;
	data.forEach(function (d) {
		d.reading_date_time = formatTime(d.reading_date_time);
		d.reading_lag_time = +d.reading_lag_time;
	});

	//console.log(data);
	if (error) throw error;

	x.domain(d3.extent(data, function (d) {
		return d.reading_date_time;
	}));
	y.domain([0, d3.max(data, function (d) {
		return d.reading_lag_time;
	})]);

	g.append("g")
		.attr("transform", "translate(0," + height + ")")
		.call(d3.axisBottom(x))
		.select(".domain")
		.text("Date of Reading")
		.remove();

	g.append("g")
		.call(d3.axisLeft(y))
		.append("text")
		.attr("fill", "#000")
		.attr("transform", "rotate(-90)")
		.attr("y", 6)
		.attr("dy", "0.71em")
		.attr("text-anchor", "end")
		.text("Lag in Seconds");

	g.append("path")
		.data([data])
		.attr("fill", "none")
		.attr("class", "line")
//		.attr("stroke", "steelblue")
		.attr("stroke-linejoin", "round")
		.attr("stroke-linecap", "round")
//		.attr("stroke-width", 1.5)
		.attr("d", line);

	// add the area
	g.append("path")
		.data([data])
		.attr("class", "area")
		.attr("d", area);
});


var inter = setInterval(function () {
	updateData();
}, 5000);

function updateData() {

	// Get the data again
	d3.json(API_URL, function (error, data) {

		//console.log(data);
		//var data = d.Data;
		data.forEach(function (d) {
			d.reading_date_time = formatTime(d.reading_date_time);
			d.reading_lag_time = +d.reading_lag_time;
		});

		//console.log(data);
		if (error) throw error;

		d3.select("svg").remove();
		var svg = d3.select("body").append("svg").attr("width", "960").attr("height", "500"),
			margin = {
				top: 20,
				right: 20,
				bottom: 30,
				left: 50
			},
			width = +svg.attr("width") - margin.left - margin.right,
			height = +svg.attr("height") - margin.top - margin.bottom,
			g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

		x.domain(d3.extent(data, function (d) {
			return d.reading_date_time;
		}));
		y.domain([0, d3.max(data, function (d) {
			return d.reading_lag_time;
		})]);

		g.append("g")
			.attr("transform", "translate(0," + height + ")")
			.call(d3.axisBottom(x))
			.select(".domain")
			.text("Date of Reading")
			.remove();

		g.append("g")
			.call(d3.axisLeft(y))
			.append("text")
			.attr("fill", "#000")
			.attr("transform", "rotate(-90)")
			.attr("y", 6)
			.attr("dy", "0.71em")
			.attr("text-anchor", "end")
			.text("Lag in Seconds");

		g.append("path")
			.data([data])
			.attr("fill", "none")
			.attr("class", "line")
		//	.attr("stroke", "steelblue")
			.attr("stroke-linejoin", "round")
			.attr("stroke-linecap", "round")
		//	.attr("stroke-width", 1.5)
			.attr("d", line);
		// add the area
		g.append("path")
			.data([data])
			.attr("class", "area")
			.attr("d", area);
	});
}