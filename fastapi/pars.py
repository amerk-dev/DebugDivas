from datetime import datetime
import pdfplumber
import re
import psycopg2
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Database connection parameters
db_params = {
    'dbname': 'debugDivas',
    'user': 'root',
    'password': 'admin',
    'host': 'db',
    'port': '5432'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

PDF_URL = "https://storage.minsport.gov.ru/cms-uploads/cms/II_chast_EKP_2024_14_11_24_65c6deea36.pdf"
TEMP_PDF_FILE = "temp_event.pdf"

def download_pdf(url, file_path):
    try:
        response = requests.get(url, headers=headers, verify=False)
            
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')


    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to download PDF file: {e}")

def parse_pdf_to_events(file_path):
    events = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    print(f"No text found on page {page_num + 1}.")
                    continue

                lines = text.strip().split('\n')

                for i in range(0, len(lines) - 2, 3):
                    try:
                        event_line = lines[i]
                        detail_line = lines[i + 1]
                        class_line = lines[i + 2]

                        match_event = re.match(r'(\d+)\s+(.+?)\s+(\d{2}\.\d{2}\.\d{4})\s+РОССИЯ\s+(\d+)', event_line)
                        if not match_event:
                            print(f"Failed to match event line: {event_line}")
                            continue

                        event_id, name, start_date, participants = match_event.groups()

                        match_details = re.match(
                            r'(.+?)\s*(от (\d+) лет и старше)?\s*(\d{2}\.\d{2}\.\d{4})\s+(.+?),\s+г\.\s*(.+)',
                            detail_line)
                        if not match_details:
                            print(f"Failed to match detail line: {detail_line}")
                            continue

                        gender_age, _, age, end_date, region, city = match_details.groups()

                        class_info = class_line.replace("КЛАСС", "").replace("дисциплины", "").strip().split(',')
                        classes = [item.strip() for item in class_info if 'дисциплина' not in item.lower()]
                        disciplines = [item.strip() for item in class_info if 'дисциплина' in item.lower()]

                        if gender_age == "мужчины":
                            gender_age = 1
                        elif gender_age == "женщины":
                            gender_age = 2
                        else:
                            gender_age = 0

                        start_date = datetime.strptime(start_date, "%d.%m.%Y").strftime("%Y-%m-%d")
                        end_date = datetime.strptime(end_date, "%d.%m.%Y").strftime("%Y-%m-%d")

                        event_data = {
                            "ekp_id": event_id,
                            "name": name,
                            "started_at": start_date,
                            "ended_at": end_date,
                            "sex": gender_age,
                            "min_age": int(age) if age else 12,
                            "max_age": 100,
                            "location": region + " " + city,
                            "sport": ', '.join(classes),
                            "seats": int(participants)
                        }
                        events.append(event_data)

                    except Exception as e:
                        print(f"Error parsing entry starting at line {i}, error: {e}")

    except Exception as e:
        print(f"Failed to parse PDF: {e}")
    return events

def setEventValueToDB():
    download_pdf(PDF_URL, TEMP_PDF_FILE)

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        events = parse_pdf_to_events(TEMP_PDF_FILE)

        for event in events:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Check if entry with the given ekp_id already exists
            check_query = """
                SELECT COUNT(*) FROM events_event WHERE ekp_id = %s;
            """
            cursor.execute(check_query, (event["ekp_id"],))
            count = cursor.fetchone()[0]

            if count > 0:
                update_query = """
                    UPDATE events_event 
                    SET name = %s, gender = %s, min_age = %s, max_age = %s, 
                        started_at = %s, ended_at = %s, location = %s, 
                        sport_type = %s, seats = %s, created_at = %s 
                    WHERE ekp_id = %s;
                """
                cursor.execute(update_query, (
                    event["name"],
                    event["sex"],
                    event["min_age"],
                    event["max_age"],
                    event["started_at"],
                    event["ended_at"],
                    event["location"],
                    event["sport"],
                    event["seats"],
                    created_at,
                    event["ekp_id"]
                ))
            else:
                insert_query = """
                    INSERT INTO events_event 
                    (ekp_id, name, gender, min_age, max_age, started_at, ended_at, location, sport_type, seats, created_at) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(insert_query, (
                    event["ekp_id"],
                    event["name"],
                    event["sex"],
                    event["min_age"],
                    event["max_age"],
                    event["started_at"],
                    event["ended_at"],
                    event["location"],
                    event["sport"],
                    event["seats"],
                    created_at
                ))

        connection.commit()
        return "Данные из PDF успешно спаршены и сохранены в БД"

    except Exception as e:
        connection.rollback()
        return f"Ошибка выполнения операции с БД: {e}"
    finally:
        cursor.close()
        connection.close()
        if os.path.exists(TEMP_PDF_FILE):
            os.remove(TEMP_PDF_FILE)