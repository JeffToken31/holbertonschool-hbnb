import { getCookie } from "./utils.js";
import { fetchPlaceDetails } from "./api.js";

document.addEventListener('DOMContentLoaded', () => {

  checkAuthentication();
    /* Insert and display place */
    function displayPlaceDetails(place) {
        // Clear the current content of the place details section
        const placeDetails = document.getElementById("place-details");
        placeDetails.textContent = '';
        /* I try to loop all amenities to create a list of amenities */
        let amenityList = "No amenity !"
        if (place.amenities) {
            amenityList = `<ul>`;
            place.amenities.forEach(amenity => {
            amenityList += `<li>${amenity.name}</li>`;
            });
            amenityList += `</ul>`;
        }
        // Create elements to display the place details (name, description, price, amenities and reviews)
        placeDetails.innerHTML = `
            <h3 class="place-title">${place.title}</h3>
        `
        const cardPlace = document.createElement('div');
        cardPlace.classList.add("place-info");
        cardPlace.innerHTML = `
            <p class="host"><strong>Host:</strong> ${place.owner.first_name} ${place.owner.last_name}</p>
            <p class="place-price"><strong>Price per night:</strong> ${place.price}$</p>
            <p class="place-description"><strong>Description:</strong> ${place.description}</p>
            <div class="place-amenities"><strong>Amenities:</strong> ${amenityList}</div>    
        `
        // Append the created elements to the place details section
        placeDetails.appendChild(cardPlace)
    }
    
    /* Keep url with id selected */
    function getPlaceIdFromURL() {
        // Extract the place ID from window.location.search
      const params = new URLSearchParams(window.location.search);
      const id = params.get('id');
      console.log(id)
      return id
    // Your code here
  }
    async function checkAuthentication() {
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
            try {
                const placeId = getPlaceIdFromURL();
                console.log(placeId);
                const place = await fetchPlaceDetails(token, placeId);
                displayPlaceDetails(place);
            } catch (error) {
                console.error("error: ", error);
                throw error;
            }
        }
    }
})
