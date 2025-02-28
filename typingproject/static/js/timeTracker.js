import { typingInput, startButton, timer } from "./domElements.js";

let timerInterval;
let startTime;

export function startTimer() {
    startTime = new Date();
    timerInterval = setInterval(() => {
        const elapsedTime = Math.floor((new Date() - startTime) / 1000);
        let minutes = Math.floor(elapsedTime / 60).toString().padStart(2, '0');
        let seconds = (elapsedTime % 60).toString().padStart(2, '0');
        timer.textContent = `タイム： ${minutes}:${seconds}`;
    }, 1000);

    typingInput.disabled = false;
    typingInput.focus();
    startButton.style.display = "none";
}

export function stopTimer() {
    clearInterval(timerInterval);
    typingInput.blur();
    const elapsedTime = Math.floor((new Date() - startTime) / 1000);
    document.getElementById("typing_time").value = elapsedTime;
    document.getElementById("typing_form").submit();
}

document.addEventListener("DOMContentLoaded", () => {
    startButton.addEventListener("click", startTimer);
});
