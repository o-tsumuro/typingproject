document.addEventListener("DOMContentLoaded", () => {
    const targetSentenceDiv = document.getElementById("target-sentence");
    const typingInput = document.getElementById("typing-input");

    // 目的の文章を取得
    const targetText = targetSentenceDiv.textContent.trim();

    // 文章を1文字ずつ <span> で囲んで表示
    targetSentenceDiv.innerHTML = [...targetText].map(char => `<span>${char}</span>`).join("");
    const spans = targetSentenceDiv.querySelectorAll("span");

    let beforeLen = 0;

    typingInput.addEventListener("input", () => {
        const inputText = typingInput.value;
        const length = inputText.length;

        // 文字削除時の背景削除
        if (length < beforeLen) {
            spans[length].className = "";
        }
        beforeLen = length;

        let hasError = false;

        for (let i = 0; i < targetText.length; i++) {
            if (i < length) {
                if (!hasError && inputText[i] === targetText[i]) {
                    spans[i].className = "correct";
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
    });
});