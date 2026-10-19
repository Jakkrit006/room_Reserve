# plan.md — แผนการทำงานโปรแกรมเกรด

## เป้าหมาย
สร้างฟังก์ชัน grade() ใน grade.py แปลงคะแนน 0-100 เป็นเกรด A-F
พร้อม test ด้วย pytest ใน test_grade.py

## Tasks

### Task 1: เขียน grade.py
- สร้าง grade.py พร้อมฟังก์ชัน grade(score)
- ตรวจ input: ต้องเป็น int/float และอยู่ในช่วง 0-100 ไม่งั้น raise ValueError
- คืนค่า A/B/C/D/F ตามเกณฑ์ใน spec.md
- ตรวจ: รัน grade() ด้วยค่าตัวอย่างจาก acceptance criteria

### Task 2: เขียน test_grade.py
- ใช้ pytest เขียน test ครอบคลุม acceptance criteria ทั้ง 3 ข้อ
  - boundary: grade(80) == "A", grade(79) == "B"
  - boundary: grade(0) == "F", grade(100) == "A"
  - invalid: grade(-1), grade(101), grade("abc") ต้อง raise ValueError
- ตรวจ: python -m pytest -q ผ่านทั้งหมด

## สถานะ
- [ ] Task 1: เขียน grade.py
- [ ] Task 2: เขียน test_grade.py

## หมายเหตุ
- ทำทีละ task แล้วหยุดให้ตรวจตาม AGENTS.md
