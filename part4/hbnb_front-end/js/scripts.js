/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
import { loginUser, fetchPlaces } from './api.js';


document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();

  /* display place on index page */
  function displayPlaces(places) {
    // Clear the current content of the places list
    const divPlaces = document.getElementById('places-list');
    divPlaces.textContent = "";
    // Iterate over the places data
    // For each place, create a div element and set its content
    // Append the created element to the places list
    places.forEach((place) => {
      const card = document.createElement('div');
      card.classList.add("place-card");
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
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
      // Fetch places data if the user is authenticated
      try {
        const places = await fetchPlaces(token);
        displayPlaces(places);
      } catch (error) {
        console.error("error: ", error)
      }
    }
  }
  function getCookie(name) {
    // Function to get a cookie value by its name
    const token = parseCookies()
    if (!token) {
      return null
    }
    return token[name]
  }
  /* Utils to parse cookie into object */
  function parseCookies() {
    const cookies = {};
    document.cookie.split('; ').forEach(cookie => {
        const [key, value] = cookie.split('=');
        cookies[key] = value;
    });
    return cookies;
  }
  
  /* fetch data send via loginform */
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      loginUser(email, password);
    });
}
  /* Add option price max dynamically */
  const priceFilter = document.getElementById('price-filter');

  /* if condition to handle dom error beaucause filter is not on all page */
  if (priceFilter) {
    const options = [
      { value: '', text: "All" },
      { value: '100', text: "100$" },
      { value: '150', text: "150$" },
      { value: '200', text: "200$" },
      { value: '250', text: "250$" },
      { value: '300', text: "300$" }
    ];

    for (const opt of options) {
      const option = document.createElement('option');
      option.value = opt.value;
      option.textContent = opt.text;
      priceFilter.appendChild(option);
    }
  }
});

  /*---------------------------------*/