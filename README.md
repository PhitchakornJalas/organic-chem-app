# 🧪 ChemGraph - Organic Chemistry Knowledge 

ChemGraph เป็นเว็บแอปพลิเคชันสำหรับสำรวจและจัดการข้อมูลสารเคมีอินทรีย์ หมู่ฟังก์ชัน และปฏิกิริยาเคมี โดยใช้ฐานข้อมูลแบบกราฟ (**Neo4j**) เพื่อแสดงความสัมพันธ์ของข้อมูลอย่างมีประสิทธิภาพ

---

## 🚀 ฟีเจอร์หลัก (Key Features)

*   **Search & Explore:** ค้นหาสารเคมีและหมู่ฟังก์ชันผ่านชื่อ IUPAC หรือชื่อภาษาไทย
*   **Admin Dashboard:** ระบบหลังบ้านสำหรับจัดการข้อมูล เพิ่ม แก้ไข และลบ สารเคมี
*   **Interactive Visuals:** แสดงโครงสร้างหมู่ฟังก์ชันและตัวอย่างสารเคมีที่เกี่ยวข้อง
*   **Authentication:** ระบบสมาชิกที่แยกสิทธิ์ระหว่าง User ทั่วไป และ Admin

---

## 🛠 การติดตั้งและใช้งาน (Installation & Setup)

โปรเจกต์นี้รองรับการใช้งานผ่าน **Docker** เพื่อความสะดวกในการตั้งค่า Environment ทั้งหมด

### 1. สิ่งที่ต้องมี (Prerequisites)
*   ติดตั้ง [Docker Desktop](https://www.docker.com/products/docker-desktop/)
*   ติดตั้ง [Git](https://git-scm.com/)

### 2. ขั้นตอนการรันโปรเจกต์ (Step-by-Step)

1.  **ตั้งค่า Environment (Optional):**
    สร้างไฟล์ `.env` ที่โฟลเดอร์หลัก (Root) เพื่อระบุค่าการเชื่อมต่อ (หากไม่ได้ตั้งค่า ระบบจะใช้ค่า Default ใน `docker-compose.yml`)
    ```env
    NEO4J_URI=bolt://neo4j:7687
    NEO4J_USER=neo4j
    NEO4J_PASSWORD=password123
    FLASK_SECRET_KEY=your_secret_key
    ```

2.  **Build และสั่งรันด้วย Docker Compose:**
    ใช้คำสั่งนี้เพื่อสร้าง Container ของ Flask และ Neo4j พร้อมกัน
    ```bash
    docker-compose up --build
    ```

3.  **เข้าใช้งานแอปพลิเคชัน:**
    *   **Website:** เปิด Browser ไปที่ [http://localhost:5000](http://localhost:5000)
    *   **Neo4j Browser:** เข้าไปดู Database ได้ที่ [http://localhost:7474](http://localhost:7474)
        *   **User:** `neo4j`
        *   **Password:** `password123`

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

*   `main.py`: ไฟล์หลักสำหรับรัน Flask Server และจัดการ Route ต่างๆ
*   `templates/`: ไฟล์ HTML (Jinja2) สำหรับแสดงผลหน้าเว็บ
*   `static/`: ไฟล์ CSS, JavaScript และรูปภาพประกอบ
*   `docker-compose.yml`: ไฟล์ตั้งค่าบริการ Docker (Flask App & Neo4j Database)
*   `Dockerfile`: ขั้นตอนการสร้าง Image สำหรับ Flask แอปพลิเคชัน

---

## 📝 ข้อมูลทดสอบเบื้องต้น (Initial Data)

สำหรับการเริ่มต้นใช้งานครั้งแรก คุณสามารถดูคำสั่ง Cypher Query เพื่อนำเข้าข้อมูลจำลอง (Initial Data) เช่น หมู่ฟังก์ชันและสารเคมีตัวอย่างได้ที่ไฟล์:

👉 **[initdata.md](initdata.md)**
