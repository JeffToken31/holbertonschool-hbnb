const API_BASE_URL = 'http://localhost:5000/api/v1';


/* post email and password to api and receive JWT */
export async function loginUser(email, password) {
    try {
        const response = await fetch(API_BASE_URL + '/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const errorEmail = document.getElementById("erroremail");
        const errorPwd = document.getElementById("errorpassword");
        errorEmail.textContent = '';
        errorPwd.textContent = '';

        if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; Max-Age = 600; path=/`;
            window.location.href = 'index.html';
        } else {
            const data = await response.json();
            console.error(data.error);
            if (data.error === "Invalid email") {
                errorEmail.innerHTML = `&#9888; ${data.error}`;
            } else if (data.error === "Invalid password") {
                errorPwd.innerHTML = `&#9888; ${data.error}`;
            } else {
                errorEmail.textContent = "An unexpected error occurred.";
            }
        }
    } catch (error) {
        console.error('Login request failed:', error);
        const errorEmail = document.getElementById("erroremail");
        errorEmail.textContent = 'Network error: Could not connect to the server.';
    }
}

/* Fetch all places (get) */
export async function fetchPlaces(token) {
    try {
        const response = await fetch(API_BASE_URL + '/places/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error("Problem with loading API");
        }
        const placeObjet = await response.json();
        console.log("Places data:", placeObjet);
        return placeObjet
    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
}

/* Fetch place by ID (get) */
export async function fetchPlaceDetails(token, placeId) {
    // Make a GET request to fetch place details
    // Include the token in the Authorization header
    try {
        const response = await fetch(`${API_BASE_URL}/places/${placeId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error("Problem with loading API");
        }
        // Handle the response and pass the data to displayPlaceDetails function
        const placeObjet = await response.json();
        return placeObjet
    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
}
/* Send a review post */
export async function submitReview(token, place, reviewText, ratingDatas) {
    // Make a POST request to submit review data
    try {
        const response = await fetch(`${API_BASE_URL}/reviews/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ text: reviewText, rating: parseInt(ratingDatas), place: place })
        });
        // Include the token in the Authorization header
        // Send placeId and reviewText in the request body
        return response;

    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
    // Handle the response 
    
}

/* Fetch review by placeID (get) */
export async function fetchReviewDetails(token, placeId) {
    // Make a GET request to fetch review details
    // Include the token in the Authorization header
    try {
        const response = await fetch(`${API_BASE_URL}/reviews/places/${placeId}/reviews`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error("Problem with loading API");
        }
        // Handle the response and pass the data to display reviewDetails function
        const reviewObjet = await response.json();
        return reviewObjet
    } catch (error) {
        console.error("loading problem:", error)
        throw error;
    }
}
