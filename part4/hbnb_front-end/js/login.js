import { loginUser } from "./api.js";
import { getCookie } from "./utils.js";

document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
  /* fetch data send via loginform */
  const loginForm = document.getElementById('login-form');

  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    loginUser(email, password);
  });
  
  function checkAuthentication() {
    const token = getCookie('token');
  
    if (token) {
      alert('You are already logged in.');
      window.location.href = 'index.html';
      return;
    }
  }
});