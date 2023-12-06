let output = document.getElementById("output");

function appendToOutput(value) {
  if (output.innerHTML === "0") {
    output.innerHTML = value;
  } else {
    output.innerHTML += value;
  }
}

function clearOutput() {
  output.innerHTML = "0";
}

function calculate() {
  output.innerHTML = eval(output.innerHTML);
}