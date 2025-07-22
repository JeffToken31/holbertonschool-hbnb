document.addEventListener('DOMContentLoaded', () => {
    /* Footer module */
    const footerDyn = document.getElementById('footer-dyn');

    fetch('footer.html')
        .then(res => res.text())
        .then(html => footerDyn.innerHTML = html)
        .catch(err => console.error("Footer Error:", err));
})