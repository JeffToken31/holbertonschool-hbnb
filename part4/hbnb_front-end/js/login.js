import { loginUser } from "./api.js";

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
})