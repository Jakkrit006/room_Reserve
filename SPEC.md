# spec.md — โปรแกรมตัดเกรด
 
## เป้าหมาย
ฟังก์ชันแปลงคะแนน 0–100 เป็นเกรด A–F
 
## กติกา
- 80–100 = A, 70–79 = B, 60–69 = C, 50–59 = D, 0–49 = F
- คะแนนนอกช่วง 0–100 หรือไม่ใช่ตัวเลข ให้ raise ValueError
 
## Tech
- Python 3.11, ไฟล์ grade.py, test ด้วย pytest ใน test_grade.py
 
## Acceptance criteria
- AC-1 grade(80) == "A" และ grade(79) == "B" (ขอบเขตต้องถูก)
- AC-2 grade(0) == "F" และ grade(100) == "A"
- AC-3 grade(-1), grade(101), grade("abc") ต้อง ValueError
