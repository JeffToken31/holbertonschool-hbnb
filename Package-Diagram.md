```mermaid
classDiagram
    %% Présentation
    class PresentationLayer {
        <<Interface>>
        +ServiceAPI
    }

    %% Domaine Métier
    class BusinessLogicLayer {
        +ServicesApp
        +Basemodel
        +UserService
        +PlaceService
        +ReviewService
        +AmenityService
    }

    %% Accès aux Données
    class PersistenceLayer {
        +DatabaseAccess
    }

    %% Relations
    PresentationLayer --> BusinessLogicLayer : Facade Pattern (via ServicesApp)
    BusinessLogicLayer --> PersistenceLayer : Database Operations
```
