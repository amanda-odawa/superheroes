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