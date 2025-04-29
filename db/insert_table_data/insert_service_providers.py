from db.db_connector import get_connection


bus_services_list = [
    "Hanif Enterprise", "Nabil Paribahan", "Shyamoli NR Travels", "TR Travels",
    "Ena Transport", "Green Line Paribahan", "Desh Travels", "Shohagh Paribahan",
    "Soudia Paribahan", "London Express", "Agomoni Express",
    "Silk Line", "Royal Coach", "Relax Transport", "Akota Transport", "Al Mobaraka",
    "Alhamra Paribahan", "Emad Paribahan", "Shanti Paribahan", "Dolphin Paribahan",
    "Labiba Classic", "Shah Ali Paribahan", "S Alam Paribahan",
    "Hili Express", "SB Super Deluxe", "Rajdhani Express"
]


def insert_bus_services():
    try:
        conn = get_connection()
        cur = conn.cursor()

        for service_provider in bus_services_list:
            try:
                cur.execute("INSERT INTO bus_services (service_name) VALUES (%s) ON CONFLICT (service_name) DO NOTHING;", (service_provider,))
                print(f"Inserted: {service_provider}")
            except Exception as e:
                print(f"Failed to insert {service_provider}: {e}")

        conn.commit()
        cur.close()
        conn.close()
        print("All service_names inserted to bus_services table.")
    except Exception as e:
        print("Database connection failed:", e)



if __name__ == "__main__":
    insert_bus_services()
