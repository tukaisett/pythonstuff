<!DOCTYPE html>
<meta charset="utf-8">
 
<link href="../src/nv.d3.css" rel="stylesheet" type="text/css">
 
<style>
 
body {
  overflow-y:scroll;
  margin: 0;
  padding: 0;
}
 
svg {
  overflow: hidden;
}
 
div {
  border: 0;
  margin: 0;
}
 
 
#test1 {
  margin: 0;
}
 
#chart svg {
  height: 800px;
  width: 600px;
}
 
</style>
 
<body>
 
<div id="offsetDiv">
  <div id="chart" class='with-3d-shadow with-transitions'>
    <svg></svg>
  </div>
</div>
 
<script src="../lib/d3.v3.js"></script>
<script src="../nv.d3.js"></script>
<script src="../src/tooltip.js"></script>
<script src="../src/utils.js"></script>
<script src="../src/models/legend.js"></script>
<script src="../src/models/axis.js"></script>
<script src="../src/models/distribution.js"></script>
<script src="../src/models/scatter.js"></script>
<script src="../src/models/scatterChart.js"></script>
<script>
generateChart();
function generateChart() {
    var chart;
    var rate = [{key:"Exchange Rate against USD", values:[]}];
    var test;
    d3.json('http://openexchangerates.org/api/latest.json?app_id=YOUR_OWN_API', function(error,data){
 
        for(var key in data.rates){
            if(data.rates.hasOwnProperty(key)){
                switch(key) {
                    case "CAD":
                        rate[0]["values"].push({"label":"Canadian Dollar","value":data.rates[key]});
                        break;
                    case "CNY":
                        rate[0]["values"].push({"label":"Chinese Yuan","value":data.rates[key]});
                        break;
                    case "CHF":
                        rate[0]["values"].push({"label":"Swiss Franc","value":data.rates[key]});
                        break;
                    case "EUR":
                        rate[0]["values"].push({"label":"Euro","value":data.rates[key]});
                        break;
                    case "JPY":
                        rate[0]["values"].push({"label":"Japanese Yen","value":data.rates[key]});
                        break;
 
                }
 
            }
        }
        nv.addGraph(function() {
            chart = nv.models.discreteBarChart()
                    .x(function(d) { return d.label })    //Specify the data accessors.
                    .y(function(d) { return d.value })
                    .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
                    .tooltips(false)        //Don't show tooltips
                    .showValues(true)       //...instead, show the bar value right on top of each bar.
                    .transitionDuration(350);
 
            generateChart(chart);
            d3.select('#chart svg')
                    .datum(rate)
                    .call(chart);
 
            nv.utils.windowResize(chart.update);
 
            return chart;
        });
    })
 
}
</script>