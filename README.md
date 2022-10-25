## 🐶 Help and Connect with Street Dogs

<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thank You!
-->

<p align="center">
    Add, Update and help a new street Dog with details and let others know.
    <br />
    <a href="https://www.djangoproject.com/"><strong>Learn more about Django »</strong></a>
    <br />
    <a href="https://github.com/dhananjaypai08/APP-RestAPI/issues">Report Bug</a>
    <br />
  <a href="https://github.com/dhananjaypai08/APP-RestAPI/tree/dogadoption">Project Link</a>
 </p>
 
 ## ✍️ Table of Contents
- [Project Breakdown](#project-breakdown)
- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)

## 🔨 Project Breakdown 
- Building Local API which handles GET, POST and DELETE http requests. 
- Database interaction done by the API.
- Taking input data from frontend and sending it to Core App.
- Processing frontend Info and accessing the data using Locally available API.
- Templating the frontend according to the data received from the backend.

## 💻 About The Project
Building a Rest API handling different HTTP requests. Using the API and servicing on data based on user requirements. Create a Dog with its location, details and an
Image. When a user is passing by that location he can just feed the dog or just say hi to the dog:). Anyone can perform the CRUD operations as everyone 
should know the info and anyone can add the info about lovely street dogs.

### 🔧 Built With
- Frontend:
  - HTML
  - Bootstrap
  - Jinja2
- Backend: 
  - Django
  - SQLite
  - Django Rest Framework
    - Serializers
    - Rest framework
  - Django Rest swagger
    - drf_yasg
  

## 🚀 Getting Started
To get a local copy up and running follow these simple steps.

### 🔨 Installation
1. Clone the repo

```sh
git clone https://github.com/dhananjaypai08/APP-RestAPI/
```

2. Create a Virtual Environment and activate

```sh
python3 -m venv [your_environment_name]
.\[your_environment_name]\Scripts\activate
```

Deactivation of virtual environment
```sh
deactivate
```

3. Installing dependencies and requirements

```sh
cd APP-RestAPI
pip3 install -r requirements.txt
```

4. Running the APP
```sh
python3 manage.py runserver
```

Database migrations
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

## 🧠 Usage
Built version:
- Python v3.10.5
- Django v4.0.1

The Basic goal is to make street dogs location active through this site. 
We know that a street dog's location is not fixed but a person who is very near and dear to that dog knows where the dog resides most of the times. 
And If you happen to go by that location you can just feed the dog or play with that dog if you want.

## 🤠 Contributions 
Open for contributions. Just clone and follow the installation. Make changes and raise a PR detailing about the changes made.

## 🏃♂️ Future Plans
- Filter Dogs based on your current location
- Dog adoption service
- Search feature more dynamic
- More details of dogs
- Individual Page feature for each dog along with an option to provide support

A dog is the only thing on earth that loves you more than you love yourself.
