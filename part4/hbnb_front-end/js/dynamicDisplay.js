document.addEventListener('DOMContentLoaded', () => {
    /* Footer module */
    const footerDyn = document.getElementById('footer-dyn');

    fetch('footer.html')
        .then(res => res.text())
        .then(html => footerDyn.innerHTML = html)
        .catch(err => console.error("Footer Error:", err));
    
      /*Hidden form review if user is not logged */
  const isLoggedIn = false; // Simulation (tu changeras ça plus tard)
    const reviewSection = document.getElementById("add-review");

    if (!isLoggedIn) {
        reviewSection.innerHTML = `
            <p>You must to be logged to leaves a review.</p>
            <a href="login.html" class="details-button">Login</a>
        `;
    }
})