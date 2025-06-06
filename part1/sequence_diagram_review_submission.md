# 📝 Situation – Review Submission

This documentation explains the flow and components involved when a user submits a review for a place within the application.

---

## 📘 Documentation

### 🎭 Actors

| Actor             | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **User**          | The individual who wants to leave a review for a specific place.            |
| **API**           | Receives the review submission request and forwards it.                     |
| **BusinessFacade**| A middle layer that handles communication between API and business logic.   |
| **BusinessLogic** | Processes and validates the review data.                                    |
| **Database**      | Stores the submitted review in relation to a user and a place.              |

---

### 🔄 Step-by-Step Flow

1. **User Submits Review**  
   The user fills out and sends a review form including data such as rating, comment, and the target place.

2. **API Handles the Request**  
   The API captures the submission and transfers it to the BusinessFacade.

3. **Facade Forwards to Business Logic**  
   The BusinessFacade relays the request to the BusinessLogic layer for processing.

4. **BusinessLogic Validates Data**  
   The BusinessLogic verifies the review content (e.g., rating range, comment length), checks user authorization, and ensures the referenced place exists.

5. **Review is Persisted**  
   If validation succeeds, the review is saved in the Database, linked to the corresponding user and place.

6. **Success or Error Response**  
   A response is built (success or failure), sent back through BusinessLogic → BusinessFacade → API.

7. **User Receives Feedback**  
   The user is informed that their review was submitted successfully, or receives an error if something went wrong.

## Review submission (Mermaid)

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessFacade
participant BusinessLogic
participant Database

User->>API: Submit Review (place_id, rating, comment)
API->>BusinessFacade: Forward Review Submission
BusinessFacade->>BusinessLogic: Validate and Handle Review
BusinessLogic->>Database: Insert Review Record
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>BusinessFacade: Return Status
BusinessFacade-->>API: Return Confirmation
API-->>User: Review Submitted Successfully
