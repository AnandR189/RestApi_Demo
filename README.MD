# FirstApi (REST API Demo)

A simple REST API built using Python and FastAPI. This project demonstrates how to set up a basic API structure, handle requests, and manage a virtual environment.

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn

## 🚀 How to Run Locally

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/AnandR189/RestApi_Demo.git](https://github.com/AnandR189/RestApi_Demo.git)
    cd RestApi_Demo
    ```

2.  **Create and activate Virtual Environment**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install fastapi uvicorn
    ```

4.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be live at `http://127.0.0.1:8000`

## 📂 Project Structure

- `main.py`: The entry point of the application.
- `venv/`: (Ignored) Local virtual environment.
