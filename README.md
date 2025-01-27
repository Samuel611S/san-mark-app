# Glasses Registration System

A desktop application for managing glasses sales and customer data, built using Python and SQLite.

## Features

- Add, update, and delete records for glasses sales.
- Store customer information including prescriptions, lens types, and coatings.
- Search for customers by name or phone number.
- Intuitive and responsive user interface with Tkinter.
- Integrated database (SQLite) for secure and efficient data management.
- Multi-language support for labels (English and Arabic).
- Navigation through input fields using arrow keys.
- Refresh and clear options for seamless management.
- Plays audio feedback upon actions.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samuel611s/san-mark-app.git
   cd san-mark-app
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place the required media files (`save.mp3`, `sanmark.jpg`) in the project directory.

4. Run the application:

   ```bash
   python app.py
   ```

## Dependencies

- `tkinter` - For building the GUI.
- `tkcalendar` - For date selection.
- `pygame` - For audio feedback.
- `Pillow` - For image processing.
- `sqlite3` - For database management.

## Usage

1. Launch the application.
2. Fill out the form to add a new record.
3. Use the search bar to find existing records.
4. Double-click on a record in the table to edit it.
5. Use the buttons to save, delete, or refresh records.

## Project Structure

- `app.py`: Main application file.
- `requirements.txt`: List of dependencies.
- `new_stmark.db`: SQLite database file (created automatically).
- `save.mp3`: Audio file for feedback.
- `sanmark.jpg`: Logo image for the application.

## Contributing

Feel free to fork this repository and submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

