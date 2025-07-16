class Document:
    def __init__(self, title):
        self.title = title

    def print_preview(self):
        return "📝 Hujjatni oldindan korish mavjud emas."


class WordDocument(Document):
    def print_preview(self):
        return f"📄 Word hujjat korinishi: '{self.title}.docx' — Matn, sarlavhalar va jadval mavjud."


class PdfDocument(Document):
    def print_preview(self):
        return f"📕 PDF hujjat korinishi: '{self.title}.pdf' — Rasm, matn va himoya sozlamalari mavjud."


word_doc = WordDocument("Hisobot")
pdf_doc = PdfDocument("Shartnoma")

print(word_doc.print_preview())

print(pdf_doc.print_preview())
