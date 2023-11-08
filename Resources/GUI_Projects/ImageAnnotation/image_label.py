# import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image, ImageDraw, ImageColor, UnidentifiedImageError


class MissingOptionError(Exception):
    pass


class ImageLabel(ttk.Label):

    def __init__(self, root, **kwargs):
        self._width = 0
        if "filename" in kwargs:
            image_filename = kwargs["filename"]
            del kwargs["filename"]
            self._filename = image_filename
            self._image_obj = Image.open(self._filename)
        else:
            # raise MissingOptionError("required option 'filename' is missing")
            self._filename = None
            self._image_obj = Image.new("RGB", (500, 500), (255, 255, 255))
            d = ImageDraw.Draw(self._image_obj)
            d.line(((0, 0), (500, 500)), fill="gray", width=3)
            d.line(((500, 0), (0, 500)), fill="gray", width=3)
            d.text((250, 250), "ImageLabel", font_size=36,
                   anchor="mm", fill="black")

        if "width" in kwargs:
            self._width = kwargs["width"]
            del kwargs["width"]
        else:
            self._width = self._image_obj.size[0]
        if "test" not in kwargs:
            self._test = False
        else:
            self._test = True
            del kwargs["test"]
        if self._test is False:
            super().__init__(root, **kwargs)
        self._tk_image = None
        self._resize_and_display_image()
        self._original_image = self._image_obj.copy()
        self._last_image = self._image_obj.copy()

    def _resize_and_display_image(self):
        if self._width == 0:
            image_to_convert = self._image_obj
        else:
            size = self._image_obj.size
            height = round(size[1] * self._width / size[0])
            image_to_convert = self._image_obj.resize((self._width, height))
        self._tk_image = ImageTk.PhotoImage(image_to_convert)
        if self._test is False:
            self.configure(image=self._tk_image)

    def add_text(self, x: float, y: float, **kwargs):
        if "text" in kwargs:
            text = kwargs["text"]
        else:
            raise MissingOptionError("Required option `text` is missing")
        if "size" in kwargs:
            size = kwargs["size"]
        else:
            size = 12
        if "color" in kwargs:
            color = kwargs["color"]
        else:
            color = "white"

        self._verify_input(x, y, text, size, color)
        self._last_image = self._image_obj.copy()
        d = ImageDraw.Draw(self._image_obj)
        out_x = round(x * self._image_obj.size[0])
        out_y = round(y * self._image_obj.size[1])
        d.text((out_x, out_y), text, font_size=size, anchor="mm",
               fill=color)
        self._resize_and_display_image()

    def _verify_input(self, x, y, text, size, color="white"):
        self._verify_x_y(x, "x")
        self._verify_x_y(y, "y")
        if type(text) is not str:
            raise TypeError("text argument must be of type <str>")
        if type(size) is not int:
            raise TypeError("size must be of type <int>")
        if type(color) is not str:
            raise TypeError("color must be a string")

    @staticmethod
    def _verify_x_y(x, argument_name: str):
        if type(x) is not float:
            raise TypeError("{} argument must be of type <float>".
                            format(argument_name))
        if x < 0.0 or x > 1.0:
            raise ValueError("{} argument must be between 0.0 and 1.0"
                             .format(argument_name))

    def revert_last_addition(self):
        self._image_obj = self._last_image.copy()
        self._resize_and_display_image()

    def clear_all_text(self):
        self._image_obj = self._original_image.copy()
        self._resize_and_display_image()

    def load_image(self, filename: str):
        result = self._load_and_convert_image_file(filename)
        if result is not False:
            self._filename = filename
            self._image_obj = result
            self._resize_and_display_image()
            self._original_image = self._image_obj.copy()
            self._last_image = self._image_obj.copy()

    @staticmethod
    def _load_and_convert_image_file(filename):
        try:
            image_obj = Image.open(filename)
        except UnidentifiedImageError as err:
            messagebox.showerror("Error loading file", err)
            return False
        else:
            return image_obj

    def width(self, new_width=None):
        if new_width is not None and type(new_width) is not int:
            raise TypeError("width must be specified as an int")
        if new_width is not None:
            self._width = new_width
            self._resize_and_display_image()
        else:
            return self._width


