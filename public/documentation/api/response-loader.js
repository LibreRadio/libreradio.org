var data_file;
location.search.substr(1).split("&").forEach(function(key_val) {
var temporary_array = key_val.split("=");
  if (temporary_array[0] === "data") {
    data_file = decodeURIComponent(temporary_array[1]);
  }
});

var xmlHttp = new XMLHttpRequest();
xmlHttp.onreadystatechange = function() {
  if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
    output_data(xmlHttp.responseText);
  }
}
xmlHttp.open("GET", "/documentation/api/"+data_file, true);
xmlHttp.send(null);

function output_data(responseText) {
  var json_data = JSON.parse(responseText);
  document.getElementById("response-title").innerHTML = json_data["title"];
  document.getElementById("response-before").innerHTML = json_data["response-before"];
  document.getElementById("response-after").innerHTML = json_data["response-after"];
  document.getElementById("response-data").innerHTML = JSON.stringify(json_data["response-data"], null, 2);
}
