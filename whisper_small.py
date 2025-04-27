

from transformers import pipeline

# สร้าง pipeline สำหรับการถอดเสียง
pipe = pipeline(model="openai/whisper-small", task="automatic-speech-recognition")

# เรียกใช้งานโมเดล
result = pipe(
    r"C:\Users\Administrator\Documents\Whisper_pre_trained\news_conversion_thai.wav",
    return_timestamps=True
)

# สร้างไฟล์ .txt และบันทึกผลลัพธ์
with open(r"C:\Users\Administrator\Documents\Whisper_pre_trained\transcription_output.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("ผลลัพธ์ได้ถูกบันทึกในไฟล์ transcription_output.txt")



