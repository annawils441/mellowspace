window.onload = function () {
    selectMood()
}

function validateCheckboxes() {
    const termsChecked = document.getElementById('terms').checked;
    const privacyChecked = document.getElementById('privacy').checked;

    document.getElementById('register-btn').disabled =
        !(termsChecked && privacyChecked);
}

function togglePassword(fieldId, button) {
    const field = document.getElementById(fieldId);

    if (field.type === "password") {
        field.type = "text";
        button.textContent = "🙈";
    } else {
        field.type = "password";
        button.textContent = "👁️";
    }
}

function selectMood() {
    const cards = document.querySelectorAll(".mood-card");
    cards.forEach(card => {
        card.classList.remove("selected");
    });
    const selected = document.querySelector('input[name="mood"]:checked');
    if (selected) {
        selected.closest(".mood-card").classList.add("selected");
        document.getElementById("mood-submit-btn").disabled = false;
    } else {
        document.getElementById("mood-submit-btn").disabled = true;
    }
}

function showMood(dayElement) {
    const date = dayElement.dataset.date;
    const score = Number(dayElement.dataset.score);
    const notes = dayElement.dataset.notes;
    document.getElementById("mood-popup").style.display = "block";
    document.getElementById("popup-date").textContent = date;
    const moods = {
        1: "😞 Very Low",
        2: "😟 Struggling",
        3: "😐 Okay",
        4: "🙂 Good",
        5: "🥰 Feeling Great"
    };
    document.getElementById("popup-mood").textContent = moods[score];
    document.getElementById("popup-notes").textContent =
        notes || "No notes were written.";
}

function closePopup() {
    document.getElementById("mood-popup").style.display = "none";
}