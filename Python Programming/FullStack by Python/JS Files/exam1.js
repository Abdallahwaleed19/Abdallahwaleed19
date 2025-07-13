function printName() {
  var name = document.getElementById("nameInput").value;
  document.getElementById("output").innerHTML = name;
}

function changeTitleStyle() {
  var title = document.getElementById("main");
  title.style.backgroundColor = "yellow" ; 
  title.style.color = "blue";
  title.style.fontSize = "32px";
  title.style.textTransform = "uppercase" ;
}

function printAllItems() {
  var items = document.querySelectorAll(".item");
  var output = "";
  for (var i = 0 ; i<items.length ; i++) {
    output += items[i].textContent+"<br>";
  };
  document.getElementById("output").innerHTML = output;
}

function highlightItems() {
  var items = document.querySelectorAll(".item");
  for (var i = 0; i < items.length; i++) {
    items[i].classList.add("highlight");
  }
}
