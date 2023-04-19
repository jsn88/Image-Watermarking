import customtkinter as ct
from customtkinter import filedialog as fd
from CTkMessagebox import CTkMessagebox
import filetype

ct.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class MainWindow(ct.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Image Watermarking v0.1")
        self.geometry(f"{500}x{100}")
        self.minsize(500,100)
        
        # configure grid
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_columnconfigure((0,1,2), weight=1)
        
        self.label_instruction = ct.CTkLabel(self, text='1. Start by uploading your water mark image.')
        self.label_instruction.grid(row=0, column=0, padx=0, pady=10, columnspan=2)
        self.label_instruction2 = ct.CTkLabel(master=self, text='2. You can now upload your image for processing.')
        self.label_instruction2.grid(row=1, column=0, padx=0, pady=0, columnspan=2)
        
        self.button_watermark = ct.CTkButton(self, command=self.load_watermark, text='Upload watermark')
        self.button_watermark.grid(row=0, column=2, padx=0, pady=0)
        
        self.button_image = ct.CTkButton(self, command=self.load_image, text='Upload image')
        self.button_image.grid(row=1, column=2, padx=0, pady=0)
    
    def show_error(self, atitle, msg):
        return CTkMessagebox(title=atitle, message=msg, icon="cancel", option_1='Yes', option_2='No')
    
    def load_dialog(self):
        file_location = fd.askdirectory()
        return file_location
    
    def load_watermark(self):
        file = fd.askopenfilename()
        check_file = filetype.guess(file)

        if not check_file == 'Jpeg' or check_file == 'Png':
            msg = self.show_error("Wrong type", "You provided wrong file type, ")
            # return self.load_watermark()
            if msg.get() == 'Yes':
                self.load_watermark()
                
    def load_image(self):
        print("loading image for processing")
        
        