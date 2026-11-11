# Library Management System (LibraryOS)

A simple Python library management application with MySQL database and a terminal CLI. Add books by ISBN, organize them into custom shelves/collections, and scan barcodes.In the future, this project might be an app to store and manage any type of media product (books,movies,games,etc.)

## Features

- Add books to the library by ISBN (looks up metadata via API [google books api  and open librar api])
- Custom shelves / collections for organizing books
- View books on a shelf
- Add/remove books from shelves
- Create and delete shelves
- Terminal-based UI for quick ISBN entry

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
