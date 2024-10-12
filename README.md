# RecipeManagement-API

## Description

This project is a **RecipeManagement-API** developed with **FastAPI** in Python. The system allows users to manage cooking recipes, plan weekly menus, and generate shopping lists based on the ingredients needed for the selected recipes. It also suggests recipes based on the available ingredients in the users' inventory.

### Features

- **User Management**: Users can register, authenticate (using JWT or OAuth2), and manage their profiles. Personal or family/group accounts can be created for collaborative menu planning.
- **Recipe Creation and Management**: Users can create, edit, and search for recipes. Each recipe includes ingredients, instructions, and possibly nutritional data.
- **Recipe Categorization**: Recipes are categorized by type of food, difficulty, preparation time, etc.
- **Search and Filtering**: Users can search and filter recipes based on various criteria.
- **Menu Planning**: Users can select recipes for specific days, create recurring menus (e.g., breakfast, lunch, dinner), and visualize menus in a calendar.
- **Shopping Lists**: Generate shopping lists based on the ingredients needed for the recipes selected in the menu.
- **Notification Microservice**: Send reminders and notifications to users about their menus, shopping lists, and meal preparation reminders.
- **Inventory Management**: Users can log ingredients in their pantry, track quantities and expiration dates, and receive recipe suggestions based on available ingredients.

### Usage Scenarios

- **Adding Ingredients to Inventory**: Users can add ingredients to their personal inventory.
- **Searching Recipes Based on Available Ingredients**: Users can check their inventory and receive recipe suggestions.
- **Menu Planning with Suggested Recipes**: Plan a weekly menu using recipes suggested based on available inventory.

## Requirements

- Python 3.8 or higher
- Docker

## Dependencies

All required packages are listed in the `requirements.txt` file.

## Installation

Follow these steps to set up and run the API:

1. **Clone the repository**:

```bash
git clone git@github.com:blandoncj/RecipeManagement-API.git
cd recipe-management
```

2. **Create a Virtual Environment (optional but recommended)**:

```bash
python -m venv venv
```

3. **Activate the virtual environment**:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

4. **Install required packages**:

```bash
pip install -r fastapi/requirements.txt
```

5. **Build the Docker images**:

Make sure you have Docker installed and running. Then execute:

```bash
docker compose build
docker compose up -d
```

6. **Run database migrations**:

After the container is running, you may need to apply database migrations. Use the following command:

```bash
docker exec -it backend_rm /bin/bash 
alembic upgrade head
```

## Accessing the Application

Once the containers are running, you can access the following services:

- **API**: http://localhost:8000
- **Adminer**: http://localhost:8080

You can use tools like **Postman** or **curl** to interact with the API at the specified endpoint.

Thank you for your interest in the project! If you have any questions or suggestions, feel free to reach out.

### Key Changes:

- Added a new **Accessing the Application** section to provide clear information about how to access the API and Adminer after setting up the project.

## Contributors

- [Jacobo Blandón](https://github.com/blandoncj)
- [Johan Peña López](https://github.com/Johan0425)
