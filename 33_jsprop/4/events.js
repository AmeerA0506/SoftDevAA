// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //A: only one alert will occur
  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?
//A: The order does not matter


//Predict, then test...
//Q: What effect does the boolean arg have in each?
//A: it changes the priority of the alerts, so 
//   (Leave exactly 1 version uncommented to test...)


for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, false);
  //trs[x].addEventListener('click', clicky, false);
}

for (var x=0; x < tds.length; x++) {
  //tds[x].addEventListener('click', clicky, true);
  tds[x].addEventListener('click', clicky, false);
}



table.addEventListener('click', clicky, true);
//table.addEventListener('click', clicky, false);

//the trues are like a stack, first in last out