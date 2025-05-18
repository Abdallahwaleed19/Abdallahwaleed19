import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.db_file = "sports_system.db"
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.connection.row_factory = sqlite3.Row
            self.create_tables()
            print("تم الاتصال بقاعدة البيانات بنجاح")
        except Exception as e:
            print(f"خطأ في الاتصال بقاعدة البيانات: {str(e)}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("تم قطع الاتصال بقاعدة البيانات")

    def create_tables(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE CHECK(length(username) >= 4 AND length(username) <= 20),
            password TEXT NOT NULL CHECK(length(password) >= 6 AND length(password) <= 25),
            email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
            phone TEXT CHECK(length(phone) >= 10),
            role TEXT NOT NULL CHECK(role IN ('admin', 'manager', 'user')) DEFAULT 'user',
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'suspended', 'banned')),
            last_login TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            event_id INTEGER,
            FOREIGN KEY (event_id) REFERENCES events(event_id)
        )
        """)

        self.execute_query("""
        CREATE TABLE IF NOT EXISTS events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK(length(name) >= 3 AND length(name) <= 25),
            description TEXT CHECK(length(description) >= 10),
            schedule TEXT NOT NULL CHECK(length(schedule) <= 30),
            location TEXT NOT NULL CHECK(length(location) >= 3 AND length(location) <= 30),
            image_name TEXT CHECK(length(image_name) <= 25),
            min_participants INTEGER DEFAULT 1 CHECK(min_participants > 0),
            max_participants INTEGER CHECK(max_participants >= min_participants),
            price REAL DEFAULT 0 CHECK(price >= 0),
            event_type TEXT CHECK(event_type IN ('sports', 'training', 'competition', 'other')),
            status TEXT DEFAULT 'upcoming' CHECK(status IN ('upcoming', 'ongoing', 'completed', 'cancelled')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_by INTEGER,
            FOREIGN KEY (created_by) REFERENCES users(user_id)
        )
        """)

        self.execute_query("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            event_id INTEGER NOT NULL,
            booking_date DATE NOT NULL CHECK(booking_date >= date('now')),
            participants_count INTEGER DEFAULT 1 CHECK(participants_count > 0),
            total_price REAL DEFAULT 0 CHECK(total_price >= 0),
            payment_status TEXT DEFAULT 'pending' CHECK(payment_status IN ('pending', 'paid', 'refunded')),
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'confirmed', 'cancelled', 'completed', 'no_show')),
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
            UNIQUE(user_id, event_id, booking_date)
        )
        """)

        self.execute_query("""
        CREATE TABLE IF NOT EXISTS event_schedules (
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            schedule_date DATE NOT NULL CHECK(schedule_date >= date('now')),
            start_time TIME NOT NULL,
            end_time TIME NOT NULL CHECK(end_time > start_time),
            capacity INTEGER CHECK(capacity BETWEEN 1 AND 1000),
            available_slots INTEGER,
            location_details TEXT,
            is_recurring BOOLEAN DEFAULT 0,
            recurrence_pattern TEXT CHECK(recurrence_pattern IN ('daily', 'weekly', 'monthly') OR recurrence_pattern IS NULL),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
            UNIQUE(event_id, schedule_date, start_time)
        )
        """)

        # تريجر تحديث التاريخ المحدث للأحداث
        self.execute_query("""
        CREATE TRIGGER IF NOT EXISTS update_event_timestamp
        AFTER UPDATE ON events
        BEGIN
            UPDATE events
            SET updated_at = CURRENT_TIMESTAMP
            WHERE event_id = NEW.event_id;
        END;
        """)

        # تريجر تحديث المقاعد المتاحة عند إضافة جدول حدث
        self.execute_query("""
        CREATE TRIGGER IF NOT EXISTS init_available_slots
        AFTER INSERT ON event_schedules
        BEGIN
            UPDATE event_schedules
            SET available_slots = NEW.capacity
            WHERE schedule_id = NEW.schedule_id;
        END;
        """)

        # تريجر تحديث المقاعد عند تأكيد الحجز
        self.execute_query("""
        CREATE TRIGGER IF NOT EXISTS update_available_slots
        AFTER UPDATE ON bookings
        WHEN NEW.status = 'confirmed' AND OLD.status != 'confirmed'
        BEGIN
            UPDATE event_schedules
            SET available_slots = available_slots - NEW.participants_count
            WHERE event_id = NEW.event_id AND schedule_date = NEW.booking_date
              AND available_slots >= NEW.participants_count;
        END;
        """)

        # تريجر إعادة المقاعد عند إلغاء الحجز
        self.execute_query("""
        CREATE TRIGGER IF NOT EXISTS restore_available_slots
        AFTER UPDATE ON bookings
        WHEN NEW.status = 'cancelled' AND OLD.status = 'confirmed'
        BEGIN
            UPDATE event_schedules
            SET available_slots = available_slots + OLD.participants_count
            WHERE event_id = OLD.event_id AND schedule_date = OLD.booking_date;
        END;
        """)

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except Exception as e:
            print(f"خطأ في تنفيذ الاستعلام: {str(e)}")
            return None

    # العمليات الأخرى (مثل إضافة/تحديث/حذف المستخدمين، الأحداث، الحجوزات، الجداول) يتم تعديلها بنفس المنطق مع مراعاة الحقول الجديدة

# مثال: دالة إضافة حدث مع الحقول الجديدة
    def add_event(self, name, description, schedule, location, image_name=None,
                  min_participants=1, max_participants=None, price=0.0,
                  event_type=None, status='upcoming', created_by=None):
        query = """
        INSERT INTO events 
        (name, description, schedule, location, image_name, min_participants, max_participants, price, event_type, status, created_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        return self.execute_query(query, (name, description, schedule, location, image_name,
                                          min_participants, max_participants, price, event_type, status, created_by))
