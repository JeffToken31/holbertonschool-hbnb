const API_BASE_URL = 'http://localhost:5000';

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
        const response = await fetch(API_BASE_URL + '/places/' + placeId  + '/reviews')
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