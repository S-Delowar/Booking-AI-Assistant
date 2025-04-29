from db.db_connector import get_connection

# Districts of Bangladesh
districts = [
    "Bagerhat", "Bandarban", "Barguna", "Barisal", "Bhola", "Bogra", "Brahmanbaria",
    "Chandpur", "Chapai Nawabganj", "Chattogram", "Chuadanga", "Comilla", "Cox's Bazar",
    "Dhaka", "Dinajpur", "Faridpur", "Feni", "Gaibandha", "Gazipur", "Gopalganj",
    "Habiganj", "Jamalpur", "Jashore", "Jhalokathi", "Jhenaidah", "Joypurhat",
    "Khagrachhari", "Khulna", "Kishoreganj", "Kurigram", "Kushtia", "Lakshmipur",
    "Lalmonirhat", "Madaripur", "Magura", "Manikganj", "Meherpur", "Moulvibazar",
    "Munshiganj", "Mymensingh", "Naogaon", "Narail", "Narayanganj", "Narsingdi",
    "Natore", "Netrokona", "Nilphamari", "Noakhali", "Pabna", "Panchagarh", "Patuakhali",
    "Pirojpur", "Rajbari", "Rajshahi", "Rangamati", "Rangpur", "Satkhira", "Shariatpur",
    "Sherpur", "Sirajganj", "Sunamganj", "Sylhet", "Tangail", "Thakurgaon"
]

def insert_districts():
    try:
        conn = get_connection()
        cur = conn.cursor()

        for district in districts:
            try:
                cur.execute("INSERT INTO locations (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (district,))
                print(f"Inserted: {district}")
            except Exception as e:
                print(f"Failed to insert {district}: {e}")

        conn.commit()
        cur.close()
        conn.close()
        print("All districts inserted to locations table.")
    except Exception as e:
        print("Database connection failed:", e)



if __name__ == "__main__":
    insert_districts()
