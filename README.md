# Library Management System

A simple Python library management application with MySQL database and a terminal CLI. Add books by ISBN, organize them into custom shelves/collections, and scan barcodes.

## Features

- Add books to the library by ISBN (looks up metadata via API)
- Custom shelves / collections for organizing books
- View books on a shelf
- Add/remove books from shelves
- Create and delete shelves
- Terminal-based UI for quick ISBN entry
- FastAPI web API (`index.py`)

## Tech Stack

- **Python 3.10+**
- **MySQL** — database
- **mysql-connector-python** — MySQL driver
- **python-dotenv** — environment variables
- **requests** — external API calls
- **opencv-python**, **pyzbar** — barcode decoding
- **rich** — terminal formatting

## License

MIT