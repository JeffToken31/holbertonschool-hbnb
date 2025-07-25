import { getCookie } from "./utils.js";
import { fetchPlaceDetails, submitReview, fetchReviewDetails } from "./api.js";

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
    
    function displayReviews(reviews) {
        // Clear the current content of the reviews section
        const reviewsSection = document.getElementById("reviews");
        reviewsSection.textContent = '';

        // Iterate over reviewobjet to innerHtlk cardreviews by card
        reviews.forEach(review => {
            const cardReview = document.createElement('div');
            cardReview.classList.add("review-card");
            cardReview.innerHTML = `
                <p class="reviewer"><strong>By:</strong> ${review.user.first_name} ${review.user.last_name}</p>
                <p class="comment">${review.text}</p>
                <p class="rating"><strong>Rating:</strong> ${review.rating}</p>
            `;
            reviewsSection.appendChild(cardReview);
        });
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
        const logoutlink = document.getElementById('logout-link');
        const main = document.getElementsByTagName('main');


        if (!token) {
            loginLink.style.display = 'block';
            try {
                const placeId = getPlaceIdFromURL();

                if (!placeId) {
                    main[0].textContent = '';
                    main[0].innerHTML = `<h1 class="error">It's forbidden bro !</h1>`;
                    return;
                }
                const place = await fetchPlaceDetails(token, placeId);
                const reviews = await fetchReviewDetails(token, placeId);
                displayPlaceDetails(place);
                displayReviews(reviews);
            } catch (error) {
                console.error("error: ", error);
                throw error;
            }
            addReviewSection.innerHTML = `
            <p>You must to be logged to leaves a review.</p>
            <a href="login.html" class="details-button">Login</a>
        `;
        } else {
            // Store the token for later use
            loginLink.style.display = 'none';
            logoutlink.style.display = 'block';
            try {
                const placeId = getPlaceIdFromURL();
                console.log(placeId);
                const place = await fetchPlaceDetails(token, placeId);
                const reviews = await fetchReviewDetails(token, placeId);
                displayPlaceDetails(place);
                displayReviews(reviews);
            } catch (error) {
                console.error("error: ", error);
                throw error;
            }
        }
    }
    const reviewForm = document.getElementById("review-form");
    reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const reviewText = document.getElementById('review').value;
        const ratingDatas = document.getElementById('rating').value;
        // Get review text from form
        const token = getCookie('token');
    
        const placeId = getPlaceIdFromURL();
        try {
            const response = await submitReview(token, placeId, reviewText, ratingDatas);

            if (response.ok) {
                alert('Review submitted successfully!');
                window.location.href = `place.html?id=${placeId}`;
            } else {
                const errorData = await response.json();
                alert(`Failed to submit review: ${errorData.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error('Error submitting review:', error);
            alert('An error occurred while submitting your review.');
        }
        // Handle the response
    });

})
