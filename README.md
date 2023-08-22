**README File Content:**

# Mumbai Home Price Prediction Web Application

## Overview

The Mumbai Home Price Prediction Web Application is a user-friendly interface that allows users to estimate the price of a house in Mumbai based on various input features such as area, number of bedrooms, lift availability, car parking, and location. The application combines front-end technologies (HTML, CSS, JavaScript) with a machine learning model to provide accurate price estimates.

## Features

- **User-friendly Interface:** The web application provides an intuitive and visually appealing interface for users to input their house features and receive estimated price predictions.

- **Dynamic Inputs:** Users can select the area, number of bedrooms, lift availability, car parking, and location from the dropdown menu.

- **Machine Learning Model:** The application employs a machine learning model (linear regression) trained on real data to provide accurate price predictions based on the selected features.

- **Cross-Origin Resource Sharing (CORS):** The server-side code is configured to allow Cross-Origin Resource Sharing, enabling communication between the client and server even if they are hosted on different domains.

## Installation and Usage

### Client-side Code

1. Clone this repository to your local machine.

2. Navigate to the `client` directory.

3. Open `app.html` in a web browser to access the web application.

### Server-side Code

1. Navigate to the `server` directory.

2. Install the required Python packages using the following command:
   
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask server using the following command:
   
   ```
   python server.py
   ```

4. The server will start running, and you can access the API endpoints for location names and home price prediction.

### Usage

1. On the web application, enter the desired area, select the number of bedrooms, indicate lift availability and car parking options, and choose the location from the dropdown.

2. Click the "Estimate Price" button to obtain the estimated price of the house.

```
### Contributing

Contributions to this project are welcome. If you find any issues or want to enhance the project, feel free to create a pull request.
