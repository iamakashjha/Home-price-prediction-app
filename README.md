
# Home Price Prediction App

## Overview

The Home Price Prediction App is a web application built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. The app helps users predict the price of a home based on various parameters like area (in square feet), number of bedrooms (BHK), number of bathrooms, and location. The app uses machine learning models to provide estimated prices based on the input data.

## Features

- **User-friendly Interface**: The app has a simple and intuitive interface that allows users to input their data easily.
- **Dynamic Location Dropdown**: The app fetches the available locations dynamically and displays them in a dropdown list.
- **Price Prediction**: Based on the user's input, the app predicts the home price and displays it in real-time.
- **Machine Learning Model**: The app uses a pre-trained machine learning model to estimate home prices based on historical data.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Machine Learning**: Python, scikit-learn (for the machine learning model)
- **APIs**: Flask for handling API requests
- **Version Control**: Git

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/home-price-prediction-app.git
   cd home-price-prediction-app
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to use the app.

## How It Works

- **Step 1**: The user enters details like area (sqft), number of bedrooms (BHK), number of bathrooms, and selects a location from the dropdown.
- **Step 2**: When the user clicks "Estimate Price," the app sends the input data to the Flask backend via a POST request.
- **Step 3**: The Flask backend processes the request, uses the machine learning model to estimate the home price, and sends the predicted price back to the frontend.
- **Step 4**: The predicted price is displayed on the page.

## File Structure

```
home-price-prediction-app/
├── app.py                 # Flask backend code
├── app.js                 # JavaScript for frontend logic
├── app.css                # CSS for styling the page
├── templates/
│   └── index.html         # HTML for the main page
├── util.py                # Utility functions for loading artifacts and predictions
├── model.pkl              # Trained machine learning model (if applicable)
└── requirements.txt       # List of Python dependencies
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Thanks to the contributors and open-source community for providing valuable resources and libraries to make this app possible.

Thank You  
Akash Jha

## Links

- [LinkedIn](https://www.linkedin.com/in/iamakashjha1/)
- [Project Demo](#) <!-- Replace # with your demo link if available -->

## Contact

For any queries or feedback, feel free to reach out:  
**Email:** iamakashjha@icloud.com
