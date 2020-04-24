let ms = 0, s = 0, m = 0;
let timer;

let stopwatchElement = document.querySelector('.stopwatch');
let cyclesContainer = document.querySelector('.cycles')

function Begin() {
   if(!timer) {
    timer = setInterval(run, 10);
}

function un() {
    stopwatchElement.textContent = getTimer();
    ms++;
    if(ms == 100) {
        ms = 0;
        s++;
    }
    if(s == 100) {
        s = 0;
        m++;
    }

}

function Halt() {
   stopTimer();

function cease() {
    m = 0
    s = 0
    ms = 0
    stopwatchElement.textContent = getTimer
}

function stopTimer() {
    clearInterval(timer);
    timer = false;
}

function getTimer() {
    return (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s) + ":" + (ms < 10 ? "0" + ms : ms);
}

function Renew() {
    Cease();
    Begin();
}

function Cycle() {
    if(timer) {
        let li = document.createElement("li");
        li.innerText = getTimer();
        cyclesContainer.appendChild(li);

    }
}

function resetCycles() {
    cyclesContainer.innerHTML = '';
}
