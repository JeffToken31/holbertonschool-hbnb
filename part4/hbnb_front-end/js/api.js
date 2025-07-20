const API_BASE_URL = 'http://localhost:5000/api/v1';


/* post email and password to api and receive JWT */
export async function loginUser(email, password) {
    const response = await fetch(API_BASE_URL +'/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();
      document.cookie = `token=${data.access_token}; path=/`;
      window.location.href = 'index.html';
    } else {
      alert('Login failed: ' + response.statusText);
    }
}

/* Fetch all places (get) */
export async function getAllPlaces() {
    try {
        const response = await fetch(API_BASE_URL + '/places')
        if (!response.ok) {
            throw new Error("Problem with loading API");
        }
        const placeObjet = await response.json();
        return placeObjet
    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
}

/* Fetch place by ID (get) */
export async function getPlaceId(placeId) {
    try {
        const response = await fetch(API_BASE_URL + '/places/' + placeId)
        if (!response.ok) {
            throw new Error("Problem with loading API");
        }
        const placeIdObjet = await response.json();
        return placeIdObjet
    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
}

/* Fetch review by place ID (get) */

export async function getReviewByPlace(placeId) {
    try {
        const response = await fetch(API_BASE_URL + '/reviews/places/' + placeId  + '/reviews')
        if (!response.ok) {
            throw new Error("Problem with loading API");
        }
        const reviewsObjet = await response.json();
        return reviewsObjet
    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
}