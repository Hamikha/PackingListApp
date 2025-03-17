
# AI Packing List Generator

## Project Overview
The **AI Packing List Generator** is a Flask-based web application that leverages **generative AI** to create customized packing lists for various trips. By providing trip details such as type, duration, and weather, the AI suggests essential and optional items tailored to the user’s needs.

## Features

- **Customizable Packing Lists**: Users can input the trip type (e.g., "weekend camping"), trip duration, and weather conditions.
- **Generative AI**: Utilizes Grok from xAI via **langchain-groq** to generate accurate and personalized packing lists.
- **Responsive UI**: Modern and user-friendly interface built with **HTML**, **CSS**, and **JavaScript**.
- **Deployment Options**: Can be easily deployed locally or on **EC2**.

## Getting Started

Follow these steps to set up and run the application locally:

### 1. Clone the repository

```bash
git clone https://github.com/Hamikha/ai-packing-list-generator
```

### 2. Set up a Virtual Environment

Navigate to the project folder and create a virtual environment.

```bash
cd ai-packing-list-generator
python3 -m venv venv
```

Activate the virtual environment:

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scriptsctivate
  ```

### 3. Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your **Grok API Key**.

```
GROK_API_KEY=your-grok-api-key-here
```

### 5. Run the Application

Start the Flask app locally:

```bash
python app.py
```

The app will be accessible at `http://127.0.0.1:5000/` in your browser.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Flask** for creating a lightweight and flexible web framework.
- **Grok** from xAI and **langchain-groq** for generative AI-powered list generation.
- **PostgreSQL** for database storage.
