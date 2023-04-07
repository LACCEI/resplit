const inputFolder = document.getElementById("getInputFolder");
const outputFolder = document.getElementById("getOutputFolder");
const closeButton = document.getElementById('closeBtn');
const restartButton = document.getElementById('restartBtn');
const numberInput = document.getElementById("number-input");
const getsFile = document.getElementById("getFile")
const progress = document.getElementById("progress")

const pattern = /^(\d+|\d+-\d+)(,\s*\d+|\s*,\s*\d+-\d+)*$/;
document.getElementById("processBtn").addEventListener("click", taskTrigger);

let taskConf = {
  inputFolder: './input',
  outputFolder: './output',
  check: false,
  task: 'selection',
  specification: {"pages": "1, 3-5, 15"} 
}

// overlay while processing occurs
function taskTrigger() {
  document.getElementById("gray").style.display='flex';
  eel.processing(taskConf.inputFolder, taskConf.outputFolder, taskConf.check, taskConf.task, taskConf.specification, checkBox());
}

// gets the path for the input folder
inputFolder.addEventListener('click', async (e) => {
  e.preventDefault();
  let path = await eel.selectFolder()();
  taskConf.inputFolder=path; 
  path = path.split('/').pop(); // puts the path into an array using / as delimiter and pops the last element
  inputFolder.nextElementSibling.innerHTML = path;
} ) 

// gets the path for the output folder
outputFolder.addEventListener('click', async (e) => {
  e.preventDefault();
  let path = await eel.selectFolder()();
  path = path.split('/').pop(); // puts the path into an array using / as delimiter and pops the last element
  outputFolder.nextElementSibling.innerHTML = path;
  taskConf.outputFolder=path 
} ) 

// CLOSING THE PROGRESSED WINDOW
closeButton.addEventListener('click', async (e) =>{
  document.getElementById("gray").style.display='none'; 
});

restartButton.addEventListener('click', async (e) =>{
  document.getElementById("gray").style.display='none'; 
});

// for the page selection box
numberInput.addEventListener("input", function() {
  const value = numberInput.value.trim(); // gets what the user typed for page # and removes spaces
  const isValid = pattern.test(value);
  input.setCustomValidity(isValid ? "" : "Invalid input format. Please enter numbers and ranges separated by commas.");
  taskConf.specification = value;
});

// if check box is clicked, it will create a csv file
function checkBox (){
  return getsFile.checked ?  "" :  "processed_log.csv" // ternary condition
} 

// check if folders have been uploaded & call processbtnstatus funct
outputFolder.addEventListener('input', processBtnStatus);
inputFolder.addEventListener('input', processBtnStatus);

// enabling and disabling process btn
function processBtnStatus() { 
  (inputFolder.files.length > 0 && outputFolder.files.length > 0 ?  (processBtn.disabled = false) :  (processBtn.disabled = true)) 
}

eel.expose(updateProcessBar)
function updateProcessBar(number) {
  number=(number>100) ? 100 : number;
  number=(number<0) ? 0 : number;
  progress.value = number; // changes the value/progression
}