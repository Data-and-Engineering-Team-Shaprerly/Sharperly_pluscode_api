# Plus Code API

This project is a web API that decodes Plus Codes into latitude and longitude coordinates. It is built using Flask, a lightweight web framework for Python, and deployed on Render.com.

## Features 

- **Decode Plus Codes**: Convert Plus Codes into latitude and longitude coordinates.
- **RESTful API**: Provides a simple interface to interact with the Plus Code decoding functionality.
- **Web Interface**: Basic HTML form for submitting Plus Codes.

## Technologies Used

- **Flask**: Web framework for Python
- **Plus Codes**: Digital addressing system by Google
- **Render.com**: Cloud platform for deployment

## Getting Started

### Prerequisites

- Python 3.10+
- Pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Data-and-Engineering-Team-Shaprerly/Sharperly_pluscode_api.git
    cd Sharperly_pluscode_api
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Locally

1. **Set up Flask environment**:

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

2. **Run the Flask application**:

    ```bash
    flask run
    ```

3. **Access the application**:

    Open your browser and go to `http://127.0.0.1:5000`.

### Deployment on Render.com

1. **Create a new web service** on Render.com.
2. **Connect your GitHub repository**.
3. **Specify the build command**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Specify the start command**:

    ```bash
    gunicorn app:app
    ```

5. **Deploy the service** and access it via the URL provided by Render.com.

## Usage

### Web Interface

- Open the deployed application URL in your browser.
- Enter the Plus Code in the provided form and submit.
- The latitude and longitude coordinates will be displayed.

### API Endpoints

- **GET /**:
    - Returns a welcome message.
- **POST /pluscode**:
    - Request Body: `{"plus_code": "YOUR_PLUS_CODE"}`
    - Response: `{"latitude": LATITUDE, "longitude": LONGITUDE}`

### Example Usage with cURL

```bash
curl -X POST https://your-app-url.onrender.com/pluscode -H "Content-Type: application/json" -d '{"plus_code": "YOUR_PLUS_CODE"}'
```

## Project Structure

```
.
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── templates
│   └── index.html        # HTML template for web interface
└── README.md             # Project documentation
```

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Plus Codes](https://github.com/google/open-location-code)
- [Render.com](https://render.com/)


## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or feedback, please contact [iampatelom@gmail.com].

---
