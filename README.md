## Get Started

1. Clone the repository
   ```
   git clone https://github.com/hammoh7/TalenView.git
   cd TalenView
   ```
2. Create a virtual environment
   ```
   python -m venv venv
   ```
3. Activate the virtual environment
   - On Windows:-
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:-
     ```
     source venv/bin/activate
     ```
4. Install the required Python packages
   ```
   pip install flask flask-cors python-dotenv Pillow pdf2image google-generativeai
   ```
5. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
6. Setup the Frontend
   - Open different terminal and paste below commands
     ```
     cd frontend
     npm install
     ```
7. Running the application:
   - Start the backend server (Make sure your virtual environment is activated):-
     ```
     python app.py
     ```
     The backend server will start on http://localhost:5000  
   - Start the frontend (in other terminal)
     ```
     npm start
     ```
     The frontend will start on http://localhost:3000
8. Open your web browser and go to `http://localhost:3000`
