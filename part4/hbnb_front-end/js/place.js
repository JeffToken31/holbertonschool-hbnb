import { getCookie } from "./utils.js";

document.addEventListener('DOMContentLoaded', () => {

  checkAuthentication();

    /* Keep url with id selected */
    function getPlaceIdFromURL() {
        // Extract the place ID from window.location.search
      const params = new URLSearchParams(window.location.search);
      const id = params.get('id');
      console.log(id)
      return id
    // Your code here
  }
    function checkAuthentication() {
        const token = getCookie('token');
        const addReviewSection = document.getElementById('add-review');
        const loginLink = document.getElementById('login-link');


        if (!token) {
          loginLink.style.display = 'block';
        
          addReviewSection.innerHTML = `
            <p>You must to be logged to leaves a review.</p>
            <a href="login.html" class="details-button">Login</a>
        `;
    } else {
        // Store the token for later use
      loginLink.style.display = 'none';
            const placeId = getPlaceIdFromURL();
      fetchPlaceDetails(token, placeId);
    }
}
})

      /*Hidden form review if user is not logged 
  const isLoggedIn = false; // Simulation (tu changeras ça plus tard)
    const reviewSection = document.getElementById("add-review");

    if (!isLoggedIn) {
        reviewSection.innerHTML = `
            <p>You must to be logged to leaves a review.</p>
            <a href="login.html" class="details-button">Login</a>
        `;
    }*/