from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np

# โหลดโมเดล BERT แบบ SBERT
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")  # รองรับภาษาไทย

# โหลด CSV
csv_path = "mental_health_chatbot_responses_1.csv"
df = pd.read_csv(csv_path)

# ตรวจสอบว่ามีคอลัมน์ที่ต้องใช้ไหม
if "Question" not in df.columns or "Answer" not in df.columns:
    raise ValueError("CSV ต้องมีคอลัมน์ 'Question' และ 'Answer'")

# แปลงข้อความเป็นเวกเตอร์ (Embedding)
question_embeddings = np.vstack([model.encode(q) for q in df["Question"]])

# สร้าง FAISS index
index = faiss.IndexFlatL2(question_embeddings.shape[1])
index.add(question_embeddings)

# ฟังก์ชันค้นหาคำตอบจาก CSV
def retrieve_context(query, top_k=3):
    query_embedding = model.encode(query).reshape(1, -1)  # ทำให้เป็น 2D array
    distances, indices = index.search(query_embedding, top_k)
    return df.iloc[indices[0]]["Answer"].tolist()

# เริ่มต้น Chatbot
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # ดึงข้อมูลที่เกี่ยวข้องจาก CSV
    context = retrieve_context(user_input)

    # รวม context และ user input เพื่อสร้างคำตอบ
    response = " ".join(context)

    print("Bot:", response)