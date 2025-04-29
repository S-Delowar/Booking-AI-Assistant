from db.db_connector import get_connection


# Dictionary of table_name and their creation_query
TABLE_QUERIES = {
    "locations": """
        CREATE TABLE IF NOT EXISTS locations (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL
        );
    """,
    "bus_services": """
        CREATE TABLE IF NOT EXISTS bus_services (
            id SERIAL PRIMARY KEY,
            service_name VARCHAR(50) UNIQUE NOT NULL
        );
    """,
    "buses": """
        CREATE TABLE IF NOT EXISTS buses (
            id SERIAL PRIMARY KEY,
            bus_number VARCHAR(50) NOT NULL,
            service_id INT NOT NULL REFERENCES bus_services(id) ON DELETE CASCADE,
            total_seats INT NOT NULL DEFAULT 40,
            price DECIMAL(10, 2) NOT NULL,
            from_location INT REFERENCES locations(id) ON DELETE CASCADE,
            to_location INT REFERENCES locations(id) ON DELETE CASCADE,
            start_time TIME NOT NULL,
            reach_time TIME NOT NULL
        );
    """,
    "discounts": """
        CREATE TABLE IF NOT EXISTS discounts (
            id SERIAL PRIMARY KEY,
            service_id INT NOT NULL REFERENCES bus_services(id) ON DELETE CASCADE,
            from_location INT REFERENCES locations(id) ON DELETE CASCADE,
            to_location INT REFERENCES locations(id) ON DELETE CASCADE,
            discount DECIMAL(10, 2) NOT NULL
        );
    """,
    "bookings": """
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id SERIAL PRIMARY KEY,
            bus_id INT NOT NULL REFERENCES buses(id) ON DELETE CASCADE,
            passenger_name VARCHAR(255) NOT NULL,
            contact_number VARCHAR(20) NOT NULL,
            from_location INT REFERENCES locations(id) ON DELETE CASCADE,
            to_location INT REFERENCES locations(id) ON DELETE CASCADE,
            journey_date DATE NOT NULL,
            journey_time TIME NOT NULL,
            seats_booked INT NOT NULL,
            ticket_price DECIMAL(10, 2) NOT NULL,
            total_price DECIMAL(10, 2) NOT NULL,
            discount_amount DECIMAL(10, 2) NOT NULL,
            net_price DECIMAL(10, 2) NOT NULL
        );
    """
}

# Function for creating all the tables
def create_tables():
    try:
        conn = get_connection()
        cur = conn.cursor()
        for table_name, query in TABLE_QUERIES.items():
            try:
                cur.execute(query)
                print(f"Table '{table_name}' created successfully.")
            except Exception as e:
                print(f"Failed to create table '{table_name}': {e}")

        conn.commit()
        cur.close()
        conn.close()
        print("All table creation queries processed.")
    except Exception as e:
        print("Database connection failed:", e)
        
        
if __name__ == "__main__":
    create_tables()
