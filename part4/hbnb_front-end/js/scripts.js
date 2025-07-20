/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
import { loginUser } from './api.js';


document.addEventListener('DOMContentLoaded', () => {
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