import { typingInput, targetSentenceDiv } from "./domElements.js";
import { stopTimer } from "./timeTracker.js";

document.addEventListener("DOMContentLoaded", () => {
    const targetText = targetSentenceDiv.textContent.trim();

    // 文章を1文字ずつ <span> で囲む
    targetSentenceDiv.innerHTML = [...targetText].map(char => `<span>${char}</span>`).join("");
    const spans = targetSentenceDiv.querySelectorAll("span");

    let beforeLen = 0;

    //改行時のエラーマーカー定義
    let errorMarker = document.createElement("span");
    errorMarker.className = "error-marker";
    errorMarker.style.backgroundColor = "red";
    errorMarker.style.display = "none";
    errorMarker.style.width = "1ch";
    errorMarker.style.height = "1.4em";
    errorMarker.style.verticalAlign = "middle";
    targetSentenceDiv.appendChild(errorMarker);

    //入力するたびに正誤判定実行
    typingInput.addEventListener("input", () => {
        const inputText = typingInput.value;
        const length = inputText.length;

        //入力と目的が一致した場合時間計測終了
        if (inputText === targetText) {
            stopTimer();
            typingInput.disabled = true;
        }

        // 文字削除時の背景削除
        if (length < beforeLen) {
            spans[length].className = "";
            errorMarker.style.display = "none";
        }
        beforeLen = length;

        //1度の正誤判定処理の内に間違いがあるかを記録するフラグ
        let hasError = false;
        //改行エラーマーカーを追加するかの判断用するためのインデックス保持変数
        let lastCorrectIndex = -1;

        for (let i = 0; i < targetText.length; i++) {
            if (i < length) {
                if (!hasError && inputText[i] === targetText[i]) {
                    spans[i].className = "correct";
                    lastCorrectIndex = i;
                } else if (i === 0 || spans[i - 1].classList.contains("correct")) {
                    hasError = true;
                    spans[i].className = "incorrect";
                } else {
                    hasError = true;
                    spans[i].className = "";
                }
            } else {
                spans[i].className = "";
            }
        }

        if (lastCorrectIndex + 1 < targetText.length && targetText[lastCorrectIndex + 1] === "\n" && length > lastCorrectIndex + 1) {
            errorMarker.style.display = "inline-block";
            spans[lastCorrectIndex].after(errorMarker);
        } else {
            errorMarker.style.display = "none";
        }
    });
});
