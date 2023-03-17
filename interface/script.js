
const inputFolder = document.getElementById("getInputFolder");
const outputFolder = document.getElementById("getOutputFolder");


document.getElementById("processBtn").addEventListener("click", taskTrigger);
//document.getElementById("restartBtn").addEventListener("click", );
//document.getElementById("closeBtn").addEventListener("click", );

let taskConf = {
    inputFolder: './input',
    outputFolder: './output',
    check: false,
    task: 'selection',
    specification: {"pages": "1, 3-5, 15"}
}

function taskTrigger() {
  document.getElementById("gray").style.display='flex';
  checkBox();
  eel.processing(taskConf.inputFolder, taskConf.outputFolder, taskConf.check, taskConf.task, taskConf.specification);
}

function checkBox(){

}

inputFolder.addEventListener('click', async (e) => {
  e.preventDefault();
  let path = await eel.selectFolder()();
  inputFolder.nextElementSibling.innerHTML = path;
  taskConf.inputFolder=path 
} ) 

