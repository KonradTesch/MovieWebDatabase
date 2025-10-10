# My Movie Database

A personal movie database web application built with Flask, allowing multiple users to manage their own movie collections. This project demonstrates full-stack web development skills including database design, API integration, and responsive web interfaces.

## 🎯 Project Overview

This application enables users to create personal movie collections by searching for films through the OMDB API. Each user can maintain their own database of movies with automatic poster fetching and detailed movie information.

## ✨ Features

- **Multi-user Support**: Create and manage multiple user accounts
- **Movie Search**: Search and add movies using the OMDB API
- **Automatic Data Fetching**: Automatically retrieves movie details including:
  - Title, Director, Release Year
  - Movie Posters
- **Movie Management**: 
  - Update movie titles
  - Delete movies from collection
- **Responsive Design**: Clean, mobile-friendly interface
- **Error Handling**: Custom 404 pages and API error management

## 🛠 Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **API Integration**: OMDB API for movie data

## 📁 Project Structure

```
movie-database/
├── app.py                 # Main Flask application
├── data_manager.py        # Database operations and API calls
├── models.py              # SQLAlchemy database models
├── .env                   # Environment variables (API keys)
├── .gitignore            # Git ignore rules
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css         # CSS styling
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # User listing page
│   ├── movies.html       # Movie collection page
│   └── 404.html          # Error page
└── data/
    └── movies.db         # SQLite database file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- OMDB API Key (free from [omdbapi.com](http://www.omdbapi.com/))

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie-database
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file in project root
   echo "API_KEY=your_omdb_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📖 Usage

1. **Create a User**: Start by creating a new user account on the home page
2. **Add Movies**: Click on a user to access their movie collection
3. **Search Movies**: Enter a movie title (and optionally year) to search via OMDB API
4. **Manage Collection**: Update movie titles or delete movies as needed

## 🏗 Architecture & Design Patterns

### Database Design
- **User Model**: Stores user information with auto-incrementing ID
- **Movie Model**: Contains movie metadata with foreign key relationship to User
- **Relationship**: One-to-Many (User → Movies)

### Code Organization
- **Separation of Concerns**: Clear separation between data logic, web routes, and templates
- **MVC Pattern**: Models, Views (templates), Controllers (Flask routes)
- **Error Handling**: Custom exception classes and comprehensive error management

### Key Technical Decisions
- **SQLAlchemy ORM**: Provides database abstraction and prevents SQL injection
- **Template Inheritance**: Jinja2 base templates for consistent UI
- **API Integration**: External movie data enrichment via OMDB API
- **Environment Configuration**: Secure API key management

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all users |
| POST | `/users` | Create new user |
| GET | `/users/<id>/movies` | Show user's movies |
| POST | `/users/<id>/movies` | Add movie to user |
| POST | `/users/<id>/movies/<id>/update` | Update movie title |
| POST | `/users/<id>/movies/<id>/delete` | Delete movie |

## 🧪 Testing

The application includes comprehensive error handling for:
- Invalid API responses
- Missing movie data
- Database connection issues
- User input validation

## 📝 Skills Demonstrated

This project showcases:
- **Full-Stack Development**: Backend API development and frontend UI design
- **Database Management**: SQLAlchemy ORM, database design, migrations
- **API Integration**: External service integration and error handling
- **Web Technologies**: Flask framework, HTML/CSS, template engines
- **Software Architecture**: Clean code principles, separation of concerns
- **Version Control**: Git workflow and project organization
- **Environment Management**: Configuration management and deployment preparation

## 👨‍💻 Author

**Konrad Tesch** - Aspiring Software Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/konrad-tesch/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KonradTesch)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:konrad.tesch@gmx.de)

**Connect with me:**
- 💼 [LinkedIn](https://www.linkedin.com/in/konrad-tesch/) - Professional network and career updates
- 🔧 [GitHub](https://github.com/KonradTesch) - More projects and code samples  
- 📧 [Email](mailto:konrad.tesch@gmx.de) - Direct contact for opportunities

---

*This project was created to demonstrate web development skills and showcase practical experience with modern development tools and practices.*
