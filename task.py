import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageOps
import numpy as np

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")
        
        self.image_path = None
        self.original_image = None
        self.current_image = None
        self.image_label = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Кнопка загрузки изображения
        self.load_button = tk.Button(self.root, text="Загрузить изображение", command=self.load_image)
        self.load_button.pack(pady=10)
        
        # Canvas для отображения изображения
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='gray')
        self.canvas.pack(pady=10)
        
        # Фрейм для кнопок преобразований
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        # Кнопки преобразований
        buttons = [
            ("Отразить по вертикали", self.flip_vertical),
            ("Отразить по горизонтали", self.flip_horizontal),
            ("Отразить по главной диагонали", self.flip_main_diagonal),
            ("Отразить по побочной диагонали", self.flip_secondary_diagonal),
            ("Фильтр Сепия", self.apply_sepia),
            ("Увеличить яркость", self.increase_brightness),
            ("Уменьшить яркость", self.decrease_brightness),
            ("Средний цвет", self.show_average_color),
            ("Добавить текст", self.add_text),
            ("Добавить прямоугольник", self.add_rectangle),
            ("Сбросить изменения", self.reset_image)
        ]
        
        for text, command in buttons:
            button = tk.Button(self.button_frame, text=text, command=command)
            button.pack(side=tk.LEFT, padx=5)
    
    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if self.image_path:
            try:
                self.original_image = Image.open(self.image_path)
                self.current_image = self.original_image.copy()
                self.display_image()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")
    
    def display_image(self):
        if self.current_image:
            # Масштабируем изображение для отображения (сохраняя пропорции)
            width, height = self.current_image.size
            ratio = min(800/width, 600/height)
            new_size = (int(width * ratio), int(height * ratio))
            display_image = self.current_image.resize(new_size, Image.LANCZOS)
            
            # Конвертируем для tkinter
            tk_image = ImageTk.PhotoImage(display_image)
            
            # Обновляем canvas
            self.canvas.delete("all")
            self.canvas.config(width=new_size[0], height=new_size[1])
            self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
            self.canvas.image = tk_image  # Сохраняем ссылку
    
    def flip_vertical(self):
        if self.current_image:
            self.current_image = ImageOps.flip(self.current_image)
            self.display_image()
    
    def flip_horizontal(self):
        if self.current_image:
            self.current_image = ImageOps.mirror(self.current_image)
            self.display_image()
    
    def flip_main_diagonal(self):
        if self.current_image:
            self.current_image = self.current_image.transpose(Image.TRANSPOSE)
            self.display_image()
    
    def flip_secondary_diagonal(self):
        if self.current_image:
            self.current_image = self.current_image.transpose(Image.TRANSPOSE)
            self.current_image = ImageOps.flip(self.current_image)
            self.current_image = ImageOps.mirror(self.current_image)
            self.display_image()
    
    def apply_sepia(self):
        if self.current_image:
            sepia_filter = np.array([
                [0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131]
            ])
            
            img_array = np.array(self.current_image)
            sepia_img = np.dot(img_array, sepia_filter.T)
            sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)
            
            self.current_image = Image.fromarray(sepia_img)
            self.display_image()
    
    def change_brightness(self, factor):
        if self.current_image:
            k = simpledialog.askfloat("Яркость", "Введите значение k (0.1-2.0):", minvalue=0.1, maxvalue=2.0)
            if k is not None:
                enhancer = ImageEnhance.Brightness(self.current_image)
                self.current_image = enhancer.enhance(factor * k)
                self.display_image()
    
    def increase_brightness(self):
        self.change_brightness(1.0)
    
    def decrease_brightness(self):
        self.change_brightness(-1.0)
    
    def show_average_color(self):
        if self.current_image:
            img_array = np.array(self.current_image)
            avg_color = np.mean(img_array, axis=(0, 1)).astype(int)
            
            # Создаем новое изображение с средним цветом
            avg_img = Image.new('RGB', (200, 200), tuple(avg_color))
            draw = ImageDraw.Draw(avg_img)
            font = ImageFont.load_default()
            draw.text((10, 10), f"RGB: {tuple(avg_color)}", fill="white", font=font)
            
            # Показываем в новом окне
            avg_img.show()
    
    def add_text(self):
        if self.current_image:
            text = simpledialog.askstring("Текст", "Введите текст:")
            if text:
                x = simpledialog.askinteger("Координата X", "Введите координату X:")
                y = simpledialog.askinteger("Координата Y", "Введите координату Y:")
                if x is not None and y is not None:
                    draw = ImageDraw.Draw(self.current_image)
                    font = ImageFont.load_default()
                    draw.text((x, y), text, fill="red", font=font)
                    self.display_image()
    
    def add_rectangle(self):
        if self.current_image:
            x1 = simpledialog.askinteger("Координата X1", "Введите координату X1:")
            y1 = simpledialog.askinteger("Координата Y1", "Введите координату Y1:")
            x2 = simpledialog.askinteger("Координата X2", "Введите координату X2:")
            y2 = simpledialog.askinteger("Координата Y2", "Введите координату Y2:")
            
            if all(v is not None for v in [x1, y1, x2, y2]):
                draw = ImageDraw.Draw(self.current_image)
                draw.rectangle([x1, y1, x2, y2], outline="blue", width=2)
                self.display_image()
    
    def reset_image(self):
        if self.original_image:
            self.current_image = self.original_image.copy()
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()