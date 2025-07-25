import { fetchPlaces } from './api.js';
import { getCookie } from './utils.js';

document.addEventListener('DOMContentLoaded', () => {

  const divPlaces = document.getElementById('places-list');
  const priceFilter = document.getElementById('price-filter');
  const priceLabel = document.querySelector('label[for="price-filter"]');

  checkAuthentication();


    function displayPlaces(places) {
      // Clear the current content of the places list
      divPlaces.textContent = "";
      // Iterate over the places data
      // For each place, create a div element and set its content
      // Append the created element to the places list
      places.forEach((place) => {
        const card = document.createElement('div');
        card.classList.add("place-card");
        card.setAttribute('data-price', place.price);
        card.innerHTML = `
                <h3 class="place-title">${place.title}</h3>
                <p class="place-price"><strong>Price per night: </strong>${place.price}$</p>
                <a href="place.html?id=${place.id}" class="details-button">View Details</a>
                `;
        divPlaces.appendChild(card);
      })
    }

  /* Check authentication the display place list */
  async function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
      try {
        const places = await fetchPlaces(token);
        displayPlaces(places);
      } catch (error) {
        console.error("error: ", error);
        throw error;
      }
      loginLink.style.display = 'block';
        return;
    } else {
      loginLink.style.display = 'none';
      priceFilter.style.display = 'block';
      priceLabel.style.display = 'block';
      
      // Fetch places data if the user is authenticated
      try {
        const places = await fetchPlaces(token);
        displayPlaces(places);
      } catch (error) {
        console.error("error: ", error);
        throw error;
      }
    }
  }

 /* Add option price max dynamically */

  document.getElementById('price-filter').addEventListener('change', async (event) => {
      event.preventDefault();
      const cardPlaces = document.getElementsByClassName("place-card");
      const price_max = priceFilter.value;

      for (const card of cardPlaces) {
        const pricestr = card.dataset.price;
        const price = parseFloat(pricestr);
        if (price_max === 'all') {
          card.style.display = 'flex';
        } else {
          if (price <= parseFloat(price_max)) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        }
      }
      // Iterate over the places and show/hide them based on the selected price
    });
    /* if condition to handle dom error beaucause filter is not on all page */
    const options = [
      { value: '10', text: "10$" },
      { value: '50', text: "50$" },
      { value: '100', text: "100$" },
      { value: 'all', text: "All", selected: true}
    ];

    for (const opt of options) {
      const option = document.createElement('option');
      option.value = opt.value;
      option.textContent = opt.text;
      if (opt.selected) {
        option.selected = true
      }
      priceFilter.appendChild(option);
    }
})