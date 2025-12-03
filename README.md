# [Project Name]

A simple Python script to [briefly describe what the script does, e.g., extract sales data from Google Sheets].

## 📋 Prerequisites

Before running the script, ensure you have:

1.  **Python 3.8+** installed.
2.  A **Google Cloud Service Account** with the JSON key file.
3.  Enabled the **Google Sheets API** and **Google Drive API** in your console.

## 🛠️ Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/your-repo.git](https://github.com/yourusername/your-repo.git)
    cd your-repo
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Credentials**
    * Place your Google Cloud JSON key in the root folder.
    * Rename it to `credentials.json` (or update the script to match your filename).
    * **Important:** Share your target Google Sheet with the `client_email` found inside your JSON file.

## 🚀 Usage

Run the script from the terminal:

```bash
python extract_sheet_test.py