# AyuBridge

## Overview
This project is a demonstrative prototype developed to address the challenge of integrating traditional Indian medicine (Nāṭural Ayurveda, Yoga, Unani, Siddha, Homeopathy) with modern digital healthcare systems. It provides an API and web interface to map Ayush terminologies from the NAMASTE portal to global ICD-11 (TM2) standards, generating compliant HL7 FHIR resources.

## Problem Statement
Healthcare data in India is often siloed, with Ayush treatment records rarely integrated in a standardized manner with allopathic medical data. This fragmentation leads to gaps in patient care, hinders population-level research, and prevents seamless inclusion of traditional medicine in the national digital health ecosystem. 
This project builds a digital bridge for interoperability between these systems.

## Live Demo
Try the working prototype here: https://namaste-api-one.vercel.app

## Source Code
The full source code can be found at: https://github.com/saipradeeps/AyuBridge-NAMASTE-API.git

## Features
- **FastAPI Backend:** Lightweight, high-performance API in Python with automatic interactive documentation.
- **Live Search:** Interactive web interface with autocomplete for Ayush terminology search.
- **Bi-directional Mapping:** Supports searching by both NAMASTE and ICD-11 codes using a sample dataset.
- **FHIR-Compliant Output:** Generates standardized ProblemList FHIR R4 resources compatible with modern EHRs.

## Tech Stack
- Backend API uses FastAPI (Python) and Uvicorn for async high performance and auto-generated docs. 
- The frontend is built with simple HTML, Tailwind CSS, and JavaScript for universal compatibility. 
- Data storage uses JSON for lightweight and portable demonstration.

## Project Structure
Main files include:
- `main.py`: FastAPI backend server logic
- `namaste_icd_mapping.json`: Sample data for terminology mapping
- `index.html`: Self-contained frontend application
- `requirements.txt`: Python dependencies
- `README.md`: This file


## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps to run locally

1. Clone the repository:
git clone https://github.com/saipradeeps/AyuBridge-NAMASTE-API.git  
cd AyuBridge-NAMASTE-API

2. Create and activate a virtual environment:  
On macOS/Linux:  
python3 -m venv venv  
source venv/bin/activate  

On Windows:  
python -m venv venv  
.\venv\Scripts\activate  

3. Install dependencies:
pip install -r requirements.txt

4. Run the backend API server:
uvicorn main:app --reload

5. Open `index.html` in a modern web browser to access the frontend interface.

## Usage
- Perform live real-time searches for Ayush terms.
- View mapped ICD-11 codes side-by-side.
- Generate and download standardized FHIR ProblemList resources.
- Use API endpoints documented in the interactive Swagger UI.

## Future Work
- Move from JSON data to a scalable PostgreSQL database.
- Integrate semantic search using advanced NLP models like Sentence Transformers (BERT).
- Expand datasets to include full official NAMASTE and ICD-11 terminologies.
- Add OAuth 2.0 flow compliant with ABHA and National Digital Health Mission.

## Contribution
Contributions via pull requests are welcome. Please follow project coding standards and include relevant tests.

## License
This project is licensed under the MIT License.

***
This README summarizes project scope, usage, and technical details with convenient links to live demo and codebase.
