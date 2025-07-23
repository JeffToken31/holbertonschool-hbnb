const API_BASE_URL = 'http://localhost:5000/api/v1';


/* post email and password to api and receive JWT */
export async function loginUser(email, password) {
    const response = await fetch(API_BASE_URL +'/auth/login', {
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
        console.log(data)
        document.cookie = `token=${data.access_token}; path=/`;
        window.location.href = 'index.html';
        console.log(document.cookie)
    } else {

        const data = await response.json();
        console.log(data.error);
        if (data.error == ("Invalid email")) {
            errorEmail.innerHTML = `&#9888; ${data.error}`;
        } else if (data.error == ("Invalid password")) {
            errorPwd.innerHTML = `&#9888; ${data.error}`;
        } else {
            errorEmail.textContent = "Ca craint !!!";
        }
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
        const response = await fetch(API_BASE_URL + '/places/' + placeId, {
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
export async function submitReview(token, placeId, reviewText) {
    // Make a POST request to submit review data
    const response = await fetch(API_BASE_URL +'/reviews/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ reviewText, ratingDatas, placeId })
    });
    // Include the token in the Authorization header
    // Send placeId and reviewText in the request body
    handleResponse(response);
    // Handle the response
}