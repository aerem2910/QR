import tkinter as tk
from tkinter import filedialog
import qrcode
import os

from PIL import ImageTk


class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Генератор QR кода')
        self.root.geometry('500x580')

        self.label = tk.Label(root, text='Вставьте ссылку на ресурс:')
        self.label.pack()

        self.text_input = tk.Entry(root)
        self.text_input.pack(fill=tk.X)
        self.text_input.config(width=30)

        self.paste_button = tk.Button(root, text='Вставить', command=self.paste_text)
        self.paste_button.pack()

        self.generate_save_button = tk.Button(root, text='Сгенерировать и Сохранить QR Code', command=self.generate_and_save_qr_code)
        self.generate_save_button.pack()

        self.qr_label = tk.Label(root)
        self.qr_label.pack()

    def paste_text(self):
        clipboard_text = self.root.clipboard_get()
        self.text_input.delete(0, tk.END)
        self.text_input.insert(0, clipboard_text)

    def generate_and_save_qr_code(self):
        text = self.text_input.get()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color='black', back_color='white')

        qr_photo = ImageTk.PhotoImage(qr_img)

        self.qr_label.config(image=qr_photo)
        self.qr_label.photo = qr_photo

        desktop_path = os.path.expanduser("~")
        file_path = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[('PNG files', '*.png')],
            initialfile='QRCode.png',
            initialdir=desktop_path,
            title='Save QR Code as PNG'
        )
        if file_path:
            qr_img.save(file_path, 'PNG')

if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()





