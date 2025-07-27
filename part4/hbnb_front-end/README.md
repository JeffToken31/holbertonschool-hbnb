# HBnB Evolution - FrontEnd

This repository contains the **FrontEnd** of the HBnB Evolution project, a learning project developed as part of the **Holberton School high-level curriculum**.  
The FrontEnd provides a **simple yet functional web interface** for users to explore listings, interact with the platform, and visualize data served by the backend.

The FrontEnd is entirely built with:

- **HTML5** for the page structure
- **CSS3** for styling and responsive layouts
- **Vanilla JavaScript (ES6)** for dynamic behavior and communication with the backend API

This part of the project focuses on:

- Rendering user-friendly views for places, users, and reviews
- Dynamically fetching and displaying data from the backend
- Practicing clean code structure with modular files

For more details about the overall project, check the [Main README](https://github.com/JeffToken31/holbertonschool-hbnb/blob/main/part4/README.md).  
To explore the backend side, see the [Backend README](https://github.com/JeffToken31/holbertonschool-hbnb/blob/main/part4/hbnb_back-end/README.md).

## ⭐ Features

- **Homepage (`index.html`)**

  - Displays a **list of available places (listings)**.
  - Allows navigation to each place’s **detail page**.
  - Provides an option to **log in**.

- **Place Details Page (`place.html`)**

  - Shows detailed information about a place (price, host, description, etc.).
  - Displays **existing reviews**.
  - Provides an option to **log in**.
  - If the user is **logged in**, they can **add a review**.
  - If the user is **not logged in**, they are prompted to log in.

- **Login Page (`login.html`)**
  - Allows users to log in.
  - Includes a **logout system** to sign out.

## 👁️ Overview

You can view the project structure by running: `tree -I "FaviconionosJB|places"`:

```bash
.
├── README.md
├── add_review.html
├── footer.html
├── images
│   ├── icon.png
│   ├── icon_bath.png
│   ├── icon_bed.png
│   ├── icon_wifi.png
│   └── logo.png
├── index.html
├── js
│   ├── api.js
│   ├── footer.js
│   ├── index.js
│   ├── login.js
│   ├── place.js
│   └── utils.js
├── login.html
├── place.html
└── styles.css
```

## 📂 Project Structure & Files Description

The FrontEnd is organized into clear sections for easy navigation and maintenance.  
Below is a description of each key file and folder.

---

### `index.html`

This is the **homepage** of the HBnB Evolution FrontEnd.  
It displays the list of **available places (listings)**, fetched dynamically from the backend API.

> **Code snippet example here:** _(How the places are fetched from the API and rendered dynamically)_

```javascript
export async function fetchPlaces(token) {
  try {
    const response = await fetch(API_BASE_URL + '/places/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Problem with loading API');
    }
    const placeObjet = await response.json();
    console.log('Places data:', placeObjet);
    return placeObjet;
  } catch (error) {
    console.error('loading problem:', error);
    throw error;
  }
}
```

---

### `place.html`

This page shows **detailed information about a specific place** (price, description, amenities, reviews).  
If the user is logged in, they can **add a review** directly from this page.

> **Code snippet example here:** _(How place details and reviews are loaded dynamically)_

```javascript
        if (!token) {
            logoutlink.style.display = 'none';
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
        }
    }
```

---

### `login.html`

This page handles the **user authentication**.  
It allows users to log in, and once logged in, the session is stored locally for accessing restricted features like adding reviews.

> **Code snippet example here:** _(The login form and fetch to the backend)_

```javascript
    if (!token) {
      try {
        const places = await fetchPlaces(token);
        displayPlaces(places);
      } catch (error) {
        console.error("error: ", error);
        throw error;
      }
      loginLink.style.display = 'block';
      logoutlink.style.display = 'none';

        return;
    } else {
      logoutlink.style.display = 'block';
      loginLink.style.display = 'none';
```

---

### `add_review.html`

A dedicated page for **adding reviews** to a place.  
Accessible only when the user is authenticated.

> **Code snippet example here:** _(Submitting a review via POST request)_

```javascript
export async function submitReview(token, place, reviewText, ratingDatas) {
  // Make a POST request to submit review data
  try {
    const response = await fetch(`${API_BASE_URL}/reviews/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        text: reviewText,
        rating: parseInt(ratingDatas),
        place: place,
      }),
    });
    // Include the token in the Authorization header
    // Send placeId and reviewText in the request body
    return response;
  } catch (error) {
    console.error('loading problem:', error);
    throw error;
  }
  // Handle the response
}
```

---

### `footer.html`

A **reusable footer component**, dynamically injected into each page using `footer.js`.  
Ensures a consistent design across the site.

> **Code snippet example here:** _(How the footer is loaded and inserted dynamically)_

```javascript
document.addEventListener('DOMContentLoaded', () => {
  /* Footer module */
  const footerDyn = document.getElementById('footer-dyn');

  fetch('footer.html')
    .then((res) => res.text())
    .then((html) => (footerDyn.innerHTML = html))
    .catch((err) => console.error('Footer Error:', err));
});
```

---

### `styles.css`

This file contains all the **styling rules** for the application, including layout, responsiveness, and theming.

> **Code snippet example here:**

```css
:root {
  --color-primary: #eb2c4f;
  --color-primary-hover: #b32640;
  --color-secondary: #007a87;
  --color-secondary-light: #48a9a6;
  --color-text: #333;
  --color-bg: #ededed;
  --color-bg2: #f0f0f0f0;
  --color-white: #fff;
  --color-shadow: #909090;
  --font-sans: 'Helvetica Neue', Arial, sans-serif;
  --font-serif: 'Georgia', serif;
  --font-mono: 'Courier New', monospace;

  --border-radius: 10px;
  --box-shadow: 0 2px 8px var(--color-shadow);
}
```

---

### `/js` Folder

Contains all the **JavaScript files** organized by purpose:

- `api.js`: Handles all API calls (GET, POST).
- `footer.js`: Dynamically injects the `footer.html` into pages.
- `index.js`: Manages homepage dynamic behavior (fetching and displaying listings).
- `login.js`: Manages login and session logic.
- `place.js`: Fetches and renders specific place details and its reviews.
- `utils.js`: Contains helper functions used across multiple scripts (parseCookie, logout...).

## 🧑‍🏫 Authors

👨‍💻 Jeffrey Basset: <https://github.com/JeffToken31>
