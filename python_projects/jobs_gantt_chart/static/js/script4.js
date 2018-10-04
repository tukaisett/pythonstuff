const rawData = {};

const container = d3.select("#chart");

const bbox = container.node().getBoundingClientRect();

const width = bbox.width,
  height = bbox.height;
const dataValues = rawData.contributions;

const parseDate = d3.time.format("%Y-%m-%dT%H:%M:%SZ").parse;

function makeChart(data) {
  const margin = { top: 30, right: 20, bottom: 30, left: 50 },
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

  const tooltip = container
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

  const x = d3.time.scale().range([0, width]);
  const y = d3.scale.linear().range([height, 0]);

  const xAxis = d3.svg
    .axis()
    .scale(x)
    .orient("bottom")
    .tickFormat(d3.time.format("%b"));

  const yAxis = d3.svg
    .axis()
    .scale(y)
    .orient("left")
    .ticks(12);

  const valueline = d3.svg
    .line()
    .x(function(d) {
      return x((d.timestamp));
    })
    .y(function(d) {
      return y(d.size);
    })
    .interpolate("cardinal");

  const svg = container
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  x.domain(
    d3.extent(data, function(d) {
      return (d.timestamp);
    })
  );
  y.domain([
    0,
    d3.max(data, function(d) {
      return d.size;
    })
  ]);

  svg
    .append("path")
    .attr("class", "line")
    .attr("d", valueline(data));

  // DOTS

  const dots = svg
    .selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr({
      cx: function(d) {
        return x((d.timestamp));
      },
      cy: function(d) {
        return y(d.size);
      },
      r: 4,
      fill: "blue",
      class: "circle"
    })
    //mouse events
    .on("mouseover", function(d) {
      tooltip
        .transition()
        .duration(1000)
        .delay(20)
        .style("opacity", 0.9);
      tooltip
        .html("<strong>" + d.size + "</strong>")
        .style("left", d3.event.pageX + "px")
        .style("top", d3.event.pageY - 28 + "px");
    })
    .on("mouseout", function(d) {
      tooltip
        .transition()
        .duration(1000)
        .delay(20)
        .style("opacity", 0);
    });

  svg
    .append("g")
    .attr("class", "x-axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

  svg
    .append("g")
    .attr("class", "y-axis")
    .call(yAxis);
}

function UpdateChart(data) {
  const margin = { top: 30, right: 20, bottom: 30, left: 50 },
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

  const x = d3.time.scale().range([0, width]);
  const y = d3.scale.linear().range([height, 0]);

  const xAxis = d3.svg
    .axis()
    .scale(x)
    .orient("bottom")
    .tickFormat(d3.time.format("%b"));

  const yAxis = d3.svg
    .axis()
    .scale(y)
    .orient("left")
    .ticks(12);

  const valueline = d3.svg
    .line()
    .x(function(d) {
      return x(d.timestamp);
    })
    .y(function(d) {
      return y(d.size);
    })
    .interpolate("cardinal");

  const svg = container.select("svg");

  x.domain(
    d3.extent(data, function(d) {
      return d.timestamp;
    })
  );
  y.domain([
    0,
    d3.max(data, function(d) {
      return d.size;
    })
  ]);

  svg
    .selectAll("path")
    .transition()
    .duration(1000)
    .delay(20)
    .ease("linear")
    .attr("d", valueline(data));

  var dots = svg
    .selectAll(".circle")
    .transition()
    .duration(1000)
    .delay(20)
    .ease("linear")
    .attr({
      cx: function(d) {
        return x(d.timestamp);
      },
      cy: function(d) {
        return y(d.size);
      }
    });

  svg
    .selectAll(".x-axis, .y-axis")
    .selectAll("*")
    .remove();
  svg.select(".x-axis").call(xAxis);
  svg.select(".y-axis").call(yAxis);
}

d3.select("select").on("change", function(d, i) {
  const sel = d3.select("#date-option").node().value;
  let updatedData = dataValues;
  console.log(updatedData);
  let startPosition = dataValues.length - sel;
  let endPosition = dataValues.length;
  let slicedData = updatedData.slice(startPosition, endPosition);
  console.log(slicedData);
  UpdateChart(slicedData);
});

d3.json(
  "https://gist.githubusercontent.com/cyrilcherian/6e345d87a8bacb9ae7f3cdd2f22901f0/raw/1111927bf6433b1cc7304d24b6cced69c3621abc/test.json",
  function(error, data) {
    if (error) {
      console.log(error);
    } else {
      data = data.query.usercontribs;
      data.forEach(function(d) {
        d.timestamp = new Date(parseDate(d.timestamp));
        d.size = +d.size;
      });
      data.sort(function(a, b) {
        return a.timestamp - b.timestamp;
      });
      
      makeChart(data);
    }
  }
);

