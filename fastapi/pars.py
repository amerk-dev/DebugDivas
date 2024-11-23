import pdfplumber
import re
import pandas as pd
import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'debugDivas',
    'user': 'root',
    'password': 'admin',
    'host': 'db',
    'port': '5432'
}

connection = psycopg2.connect(**db_params)

def parse_pdf_to_events(file_path):
    events = []

    with pdfplumber.open(file_path) as pdf:
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
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

                    # 1-я строка: Номер события, наименование, дата начала, страна, количество участников
                    match_event = re.match(r'(\d+)\s+(.+?)\s+(\d{2}\.\d{2}\.\d{4})\s+РОССИЯ\s+(\d+)', event_line)
                    if not match_event:
                        print(f"Failed to match event line: {event_line}")
                        continue

                    event_id, name, start_date, participants = match_event.groups()

                    # 2-я строка: Пол, возраст, дата конца, область, город
                    match_details = re.match(
                        r'(.+?)\s*(от (\d+) лет и старше)?\s*(\d{2}\.\d{2}\.\d{4})\s+(.+?),\s+г\.\s*(.+)', detail_line)
                    if not match_details:
                        print(f"Failed to match detail line: {detail_line}")
                        continue

                    gender_age, _, age, end_date, region, city = match_details.groups()

                    # 3-я строка: Классы и дисциплины
                    class_info = class_line.replace("КЛАСС", "").replace("дисциплины", "").strip().split(',')
                    classes = [item.strip() for item in class_info if not 'дисциплина' in item.lower()]
                    disciplines = [item.strip() for item in class_info if 'дисциплина' in item.lower()]

                    event_data = {
                        "id": event_id,
                        "name": name,
                        "started_at": start_date,
                        "ended_at": end_date,
                        "sex": gender_age.strip(),
                        "min_age": int(age) if age else None,
                        "max_age": 100,
                        "location": region + city,
                        "sport": ', '.join(classes),
                        "seats": int(participants)
                    }
                    events.append(event_data)

                except Exception as e:
                    print(f"Error parsing entry starting at line {i}, error: {e}")

    return events



events = parse_pdf_to_events("eee.pdf")


def setEventValueToDB(events):
    cursor = connection.cursor()
    for event in events:
        insert_query = """
        INSERT INTO events_event 
        (name, sex, min_age, max_age, started_at, ended_at, location, sport, seats) 
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9);
        """
        cursor.execute(insert_query, event["name"], event["sex"], event["min_age"], event["max_age"], event["started_at"], event["ended_at"], event["location"], event["sport"], event["seats"])
    connection.commit()