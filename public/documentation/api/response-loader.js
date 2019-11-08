var dataFile;
location.search.substr(1).split('&').forEach(function (keyVal) {
  var temporaryArray = keyVal.split('=');
  if (temporaryArray[0] === 'data') {
    dataFile = decodeURIComponent(temporaryArray[1]);
  }
});

var xmlHttp = new XMLHttpRequest();
xmlHttp.onreadystatechange = function () {
  if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
    outputData(xmlHttp.responseText);
  }
};

xmlHttp.open('GET', '/documentation/api/' + dataFile, true);
xmlHttp.send(null);

function outputData(responseText) {
  var jsonData = JSON.parse(responseText);
  document.getElementById('response-title').innerHTML = jsonData.title;
  document.getElementById('response-before').innerHTML = jsonData.textBefore;
  document.getElementById('response-after').innerHTML = jsonData.textAfter;
  document.getElementById('response-data').innerHTML = JSON.stringify(
    jsonData.responseData, null, 2);
}
