# Superheroes API
A Flask API that tracks superheroes and their superpowers. This project follows a structured approach using Flask, SQLAlchemy, and RESTful API design.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Seeding the Database](#seeding-the-database)
- [Contributing](#contributing)
- [License](#license)

## Features
- Create, Read, Update, and Delete (CRUD) superheroes
- Assign and manage superpowers for heroes
- Maintain relationships between heroes and superpowers
- Input validations to ensure data integrity

## Technologies Used
- Python
- Flask
- SQLAlchemy
- SQLite (default database)

## Installation
1. Fork and clone the repository, then navigate to it:
   ```sh
   git clone https://github.com/amanda-odawa/superheroes.git
   cd superheroes
   ```
2. Install dependencies using Pipenv:
   ```sh
   pipenv install
   ```
3. Activate the virtual environment:
   ```sh
   pipenv shell
   ```
4. Set up the database:
   ```sh
   flask db upgrade
   ```

## Usage
Run the Flask application:
```sh
python app.py
```
The API will be accessible at `http://127.0.0.1:5555/`.

## API Endpoints
| Method | Endpoint              | Description                  |
|--------|-----------------------|------------------------------|
| GET    | `/heroes`             | Get all heroes               |
| GET    | `/heroes/:id`         | Get a hero by ID             |
| GET    | `/powers`             | Get all superpowers          |
| GET    | `/powers/:id`         | Get a superpower by ID       |
| PATCH  | `/powers/:id`         | Update a superpower          |
| POST   | `/hero_powers`        | Assign a power to a hero     |


## Database Models
- **Hero**: Represents a superhero with attributes like name and identity.
- **Power**: Represents a superpower with attributes like name and description.
- **HeroPower**: A join table linking heroes to their superpowers with an assigned strength level.

## Seeding the Database
To seed the database with sample data, run:
```sh
python seed.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
1. Fork the repository
2. Create a new branch 
    ```sh
    git checkout -b Your-Feature-Name
    ```
3. Make your changes
4. Commit changes 
    ```sh
    git commit -m 'Added new feature'
    ```
5. Push to GitHub 
    ```sh
    git push origin Your-Feature-Name
    ```
6. Submit a pull request

## License
This project is licensed under the MIT License.
