Ayush Terminology Mapping Service - SIH Prototype
A demonstrative prototype developed for the Smart India Hackathon, addressing the challenge of integrating traditional Indian medicine (Ayush) with modern digital healthcare systems. This project provides a simple yet powerful API and web interface to map Ayush terminologies from the NAMASTE portal to the global ICD-11 (TM2) standard, generating a standards-compliant FHIR resource.

🎯 The Problem
Healthcare data in India is often siloed. A patient's Ayush treatment records rarely integrate with their allopathic medical history in a standardized way. This creates gaps in care, hinders large-scale research, and prevents the seamless inclusion of traditional medicine in the national digital health ecosystem.

This project directly tackles this challenge by building a digital bridge, enabling interoperability between the two systems.

✨ Features (Current Prototype)
This repository contains a functional Minimum Viable Product (MVP) that demonstrates the core workflow:

⚡ Fast API Backend: A lightweight and high-performance API built with Python and FastAPI.

🔍 Live Search: An interactive web interface with an autocomplete widget to search for Ayush terms in real-time.

↔️ Bi-directional Mapping: The backend supports searching by both NAMASTE and ICD-11 terms from our sample dataset.

📄 FHIR-Compliant Output: Successfully generates a structured ProblemList resource in the HL7 FHIR R4 format, proving its ability to integrate with any modern EHR system.

🛠️ Tech Stack
Component

Technology

Rationale

Backend API

FastAPI (Python), Uvicorn

High performance, automatic documentation, and ease of use.

Frontend

HTML, Tailwind CSS, JavaScript

A simple, single-file, and universally compatible web interface.

Data Storage

JSON

A lightweight and portable format for our demonstrative dataset.

📁 Project Structure
The project is intentionally kept simple for this prototype stage:

.
├── main.py                   # The FastAPI backend server logic
├── namaste_icd_mapping.json  # The sample dataset for terminology mapping
├── index.html                # The self-contained frontend application
└── requirements.txt          # Python dependencies for the backend
└── README.md                 # This file

🚀 Getting Started: Instructions to Build and Run
Follow these instructions to get the project running on your local machine.

1. Prerequisites
Python 3.7+

pip (Python package installer)

2. Setup
1. Clone the repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Create and activate a virtual environment (Recommended):

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install the required Python packages:

pip install -r requirements.txt

3. Running the Application
The project has two parts that need to be running: the backend server and the frontend interface.

1. Start the Backend Server:
Run the following command in your terminal from the project's root directory:

uvicorn main:app --reload

You should see output indicating the server is running, typically at http://127.0.0.1:8000. Keep this terminal window open.

2. Launch the Frontend:
No server is needed for the frontend. Simply open the index.html file in your favorite web browser.

You can now interact with the web page, and it will communicate with your locally running backend API.

🔮 Future Scope & Next Steps
This prototype lays the foundation for a much more intelligent and robust system. The logical next steps include:

Database Integration: Migrating from a static JSON file to a scalable database like PostgreSQL.

Advanced AI/NLP: Implementing semantic search using Sentence Transformers (BERT) to handle complex, ambiguous, and colloquial medical terms.

Expanded Dataset: Integrating the full, comprehensive terminologies from the official NAMASTE and ICD-11 sources.

ABHA Integration: Implementing a secure OAuth 2.0 flow to align with India's National Digital Health Mission for patient consent.
