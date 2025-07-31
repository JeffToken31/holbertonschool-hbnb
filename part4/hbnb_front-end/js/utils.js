export function getCookie (name) {
  // Function to get a cookie value by its name
  const token = parseCookies();
  return token[name];
}
/* Utils to parse cookie into object */
export function parseCookies () {
  const cookies = {};
  document.cookie.split('; ').forEach(cookie => {
    const [key, value] = cookie.split('=');
    cookies[key] = value;
  });
  return cookies;
}

export function logoutUser () {
  document.cookie = 'token=; Max-Age=0; path=/;';
  window.location.href = 'index.html';
}
