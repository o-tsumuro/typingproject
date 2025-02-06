import { typingInput, startButton, timer } from "./domElements.js";

let timerInterval;
let startTime;

//時間測定
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

//時間測定終了
export function stopTimer() {
    clearInterval(timerInterval);
    const elapsedTime = Math.floor((new Date() - startTime) / 1000);
    document.getElementById("typing_time").value = elapsedTime;
    document.getElementById("typing_form").submit();
}

//スタートボタンクリック時に計測開始
document.addEventListener("DOMContentLoaded", () => {
    startButton.addEventListener("click", startTimer);
});
