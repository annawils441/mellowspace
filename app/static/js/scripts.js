window.onload = function () {
    selectMood();
}

document.addEventListener("DOMContentLoaded", function () {
    initialiseEmotionSelector();
    const links = document.querySelectorAll(".navbar a");
    links.forEach(link => {
        link.addEventListener("click", () => {
            document.getElementById("navbar").classList.remove("show");
        });
    });
    document.addEventListener("click", function (event) {
        const navbar = document.getElementById("navbar");
        const hamburgerMenu = document.querySelector(".hamburger");
        if (!navbar) return;
        const clickedOutsideNavbar = !navbar.contains(event.target);
        const clickedOutsideHamburger = !hamburgerMenu || !hamburgerMenu.contains(event.target);
        if (clickedOutsideNavbar && clickedOutsideHamburger) {
            navbar.classList.remove("show");
        }
    });
    document.querySelectorAll(".favourite-btn").forEach(button => {
        button.addEventListener("click", async function (event) {
            event.preventDefault();
            const strategy_id = this.dataset.strategy;
            const response = await fetch(`/toggle-favourite/${strategy_id}`, {
                method: "POST"
            });
            const data = await response.json();
            this.textContent = data.favourited ? "❤️" : "🤍";
        });
    });
   const continueBtn = document.getElementById("continue-btn");
    const passwordInput = document.getElementById("currentpassword");
    function updateButtonState() {
        if (!continueBtn || !passwordInput) return;
        continueBtn.disabled = passwordInput.value.trim().length === 0;
    }
    if (continueBtn && passwordInput) {
        updateButtonState();
        passwordInput.addEventListener("input", updateButtonState);
    }
});

async function checkPassword() {
    const passwordInput = document.getElementById("currentpassword");
    const continueBtn = document.getElementById("continue-btn");
    const response = await fetch("/verify_password", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            password: passwordInput.value
        })
    });
    const data = await response.json();
    if (data.valid) {
        showConfirmDelete();
    } else {
        alert("Incorrect password. Please try again.");
        passwordInput.value = "";
        continueBtn.disabled = true;
    }
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
    const submitBtn = document.getElementById("mood-submit-btn");
    if (selected) {
        selected.closest(".mood-card").classList.add("selected");
        if (submitBtn) submitBtn.disabled = false;
    } else {
        if (submitBtn) submitBtn.disabled = true;
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

function initialiseEmotionSelector() {
    const emotionCards = document.querySelectorAll(".emotion-child-container");
    const copingSections = document.querySelectorAll(".coping-section");
    emotionCards.forEach(card => {
        card.addEventListener("click", () => {
            emotionCards.forEach(c => c.classList.remove("selected"));
            card.classList.add("selected");
            copingSections.forEach(section => {
                section.classList.remove("active");
            });
            const emotion = card.dataset.emotion;
            copingSections.forEach(section => {
                const emotions = section.dataset.emotions;
                if (emotions && emotions.split(" ").includes(emotion)) {
                    section.classList.add("active");
                }
            });
        });
    });
}

function toggleMenu() {
    document.getElementById("navbar").classList.toggle("show");
}

function dismissMessage(button) {
    const flash = button.parentElement;
    flash.style.opacity = "0";
    flash.style.transform = "translateY(-10px)";
    setTimeout(() => {
        flash.remove();
    }, 300);
}

function openEditPopup() {
    document.getElementById("edit-popup").style.display = "flex";
}

function closeEditPopup() {
    document.getElementById("edit-popup").style.display = "none";
}

function showUsernameForm() {
    document.getElementById("username-form").style.display = "block";
    document.getElementById("email-form").style.display = "none";
}

function showEmailForm() {
    document.getElementById("email-form").style.display = "block";
    document.getElementById("username-form").style.display = "none";
}

function openPasswordPopup() {
    document.getElementById("change-pwd-popup").style.display = "flex";
}

function closePasswordPopup() {
    document.getElementById("change-pwd-popup").style.display = "none";
}

function closeDeletePopup() {
    document.getElementById("delete-account-popup").style.display = "none";
}

function openDeletePopup() {
    document.getElementById("delete-account-popup").style.display = "flex";
}

function showConfirmDelete() {
    document.getElementById("delete-confirmation").style.display = "flex";
}

function confirmDeleteStepCompleted() {
    const el = document.getElementById("delete-confirmation");
    return el && el.style.display === "flex";
}


function submitDeleteForm() {
    const confirmationBox = document.getElementById("delete-confirmation");
    if (confirmationBox.style.display !== "flex") {
        alert("Please confirm deletion first.");
        return;
    }
    document.getElementById("delete-form").submit();
}