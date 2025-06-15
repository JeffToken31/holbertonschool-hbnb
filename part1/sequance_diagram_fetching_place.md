# 📍 Situation – Fetching a List of Places

This documentation explains the flow and components involved when a user requests a list of available places based on specific criteria.

---

## 📘 Documentation

### 🎭 Actors

| Actor             | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **User**          | The person searching for available places, possibly with filters.           |
| **API**           | Receives the request for place listings and forwards it.                    |
| **BusinessFacade**| A layer that coordinates between the API and the internal logic.            |
| **BusinessLogic** | Applies filtering logic and prepares query conditions.                      |
| **Database**      | Fetches the data of places matching the filters provided.                   |

---

### 🔄 Step-by-Step Flow

1. **User Requests Place List**  
   The user triggers a search by specifying criteria such as location, price range, or available amenities.

2. **API Captures the Request**  
   The API receives the search query and passes it to the BusinessFacade.

3. **BusinessFacade Transfers the Request**  
   The BusinessFacade forwards the data to the BusinessLogic layer.

4. **BusinessLogic Processes the Query**  
   The logic parses and sanitizes the criteria, builds the appropriate database query, and ensures data integrity.

5. **Query is Executed on the Database**  
   The Database searches for places matching the requested filters.

6. **Matching Results are Returned**  
   The Database sends back the list of places to the BusinessLogic.

7. **Final Response is Built and Sent Back**  
   The BusinessLogic formats the results, returns them to the API via the BusinessFacade, and the API sends the response to the user.

8. **User Sees the List**  
   The user receives the filtered list of available places matching their request.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessFacade
participant BusinessLogic
participant Database

User->>API: Request List of Places (criteria)
API->>BusinessFacade: Forward Filtering Request
BusinessFacade->>BusinessLogic: Handle Filtering and Query
BusinessLogic->>Database: Query Matching Places
Database-->>BusinessLogic: Return Place List
BusinessLogic-->>BusinessFacade: Return Results
BusinessFacade-->>API: Send List
API-->>User: Display List of Places
