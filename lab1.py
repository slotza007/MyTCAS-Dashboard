import requests
import pandas as pd

# โหลดข้อมูลหลักสูตร
url = 'https://my-tcas.s3.ap-southeast-1.amazonaws.com/mytcas/courses.json?ts=197e33cef91'
resp = requests.get(url)
resp.raise_for_status()
data = resp.json()

# คำที่เกี่ยวข้องกับ AI/คอมพิวเตอร์
keywords = ['ปัญญาประดิษฐ์', 'AI', 'คอมพิวเตอร์']

# กรองเฉพาะหลักสูตรวิศวกรรมที่เกี่ยวกับ AI/คอมพิวเตอร์
filtered = []
for c in data:
    name_th = c.get('program_name_th', '')
    is_engineering = any(word in name_th for word in ['วิศวกรรมศาสตรบัณฑิต', 'วศ.บ.', 'วศบ.'])
    is_ai_related = any(kw in name_th for kw in keywords)
    if is_engineering and is_ai_related:
        filtered.append(c)

# เตรียมข้อมูล: มหาวิทยาลัย, หลักสูตร, ค่าเทอม
results = []
for c in filtered:
    university = c.get('university_name_th', '')
    program = c.get('program_name_th', '')
    cost = c.get('cost', '')
    if cost:
        results.append({
            'มหาวิทยาลัย': university,
            'หลักสูตร': program,
            'ค่าเทอม': cost
        })

# สร้าง DataFrame และบันทึกเป็น Excel
df = pd.DataFrame(results)
df.to_excel('engineering_ai_programs_full.xlsx', index=False)

print(f"บันทึกไฟล์ engineering_ai_programs_full.xlsx เรียบร้อย จำนวน {len(results)} รายการ")
