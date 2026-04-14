// Fade in elements on load
document.addEventListener("DOMContentLoaded", () => {
    const fadeElements = document.querySelectorAll(".glass-card, h1, h2");
    fadeElements.forEach((el, index) => {
        el.classList.add("fade-in");
        el.style.animationDelay = `${index * 0.1}s`;
    });
});

// Mood Selector API Call
function addMood(value) {
    fetch('/api/mood', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ value: value })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            window.location.reload();
        }
    });
}
