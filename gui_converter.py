#!/usr/bin/env python3
"""
GUI Image to PDF Converter
A simple GUI application for converting images to PDF using tkinter.
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading

# Import the converter class from the main script
try:
    from image_to_pdf_converter import ImageToPDFConverter
except ImportError:
    try:
        from PIL import Image
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter, A4
    except ImportError as e:
        messagebox.showerror("Import Error", 
                           f"Required packages not found: {e}\n\n"
                           "Please install: pip install Pillow reportlab")
        sys.exit(1)


class ImageToPDFGUI:
    """GUI application for image to PDF conversion."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Initialize the converter
        self.converter = ImageToPDFConverter()
        self.selected_images = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Image to PDF Converter", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Image selection section
        ttk.Label(main_frame, text="Select Images:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(buttons_frame, text="Add Images", 
                  command=self.add_images).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(buttons_frame, text="Add Directory", 
                  command=self.add_directory).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Clear All", 
                  command=self.clear_images).pack(side=tk.LEFT, padx=5)
        
        # Image list
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        self.image_listbox = tk.Listbox(list_frame)
        self.image_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for listbox
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.image_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.image_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Options section
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        options_frame.columnconfigure(1, weight=1)
        
        # Page size option
        ttk.Label(options_frame, text="Page Size:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.page_size_var = tk.StringVar(value="A4")
        page_size_combo = ttk.Combobox(options_frame, textvariable=self.page_size_var, 
                                      values=["A4", "Letter"], state="readonly", width=10)
        page_size_combo.grid(row=0, column=1, sticky=tk.W, pady=2)
        
        # Margin option
        ttk.Label(options_frame, text="Margin (points):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.margin_var = tk.StringVar(value="50")
        margin_entry = ttk.Entry(options_frame, textvariable=self.margin_var, width=10)
        margin_entry.grid(row=1, column=1, sticky=tk.W, pady=2)
        
        # Conversion mode
        ttk.Label(options_frame, text="Mode:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.mode_var = tk.StringVar(value="separate")
        mode_frame = ttk.Frame(options_frame)
        mode_frame.grid(row=2, column=1, sticky=tk.W, pady=2)
        
        ttk.Radiobutton(mode_frame, text="Separate PDFs", variable=self.mode_var, 
                       value="separate").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(mode_frame, text="Single PDF", variable=self.mode_var, 
                       value="single").pack(side=tk.LEFT)
        
        # Output section
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Output:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.output_var = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.output_var)
        output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=2)
        ttk.Button(output_frame, text="Browse", 
                  command=self.browse_output).grid(row=0, column=2, pady=2)
        
        # Convert button
        convert_frame = ttk.Frame(main_frame)
        convert_frame.grid(row=6, column=0, columnspan=3, pady=20)
        
        self.convert_button = ttk.Button(convert_frame, text="Convert to PDF", 
                                        command=self.convert_images)
        self.convert_button.pack()
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=8, column=0, columnspan=3, pady=5)
        
        # Configure grid weights for main_frame
        main_frame.rowconfigure(3, weight=1)
    
    def add_images(self):
        """Add individual image files."""
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.gif *.webp"),
            ("All files", "*.*")
        ]
        
        files = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=filetypes
        )
        
        for file in files:
            if file not in self.selected_images:
                self.selected_images.append(file)
                self.image_listbox.insert(tk.END, os.path.basename(file))
        
        self.update_status(f"Selected {len(self.selected_images)} images")
    
    def add_directory(self):
        """Add all images from a directory."""
        directory = filedialog.askdirectory(title="Select Directory with Images")
        
        if directory:
            # Find all image files in the directory
            added_count = 0
            for ext in self.converter.SUPPORTED_FORMATS:
                for file_path in Path(directory).glob(f"*{ext}"):
                    file_str = str(file_path)
                    if file_str not in self.selected_images:
                        self.selected_images.append(file_str)
                        self.image_listbox.insert(tk.END, file_path.name)
                        added_count += 1
                
                # Also check uppercase extensions
                for file_path in Path(directory).glob(f"*{ext.upper()}"):
                    file_str = str(file_path)
                    if file_str not in self.selected_images:
                        self.selected_images.append(file_str)
                        self.image_listbox.insert(tk.END, file_path.name)
                        added_count += 1
            
            if added_count > 0:
                self.update_status(f"Added {added_count} images from directory")
            else:
                messagebox.showinfo("Info", "No supported image files found in the selected directory.")
    
    def clear_images(self):
        """Clear all selected images."""
        self.selected_images.clear()
        self.image_listbox.delete(0, tk.END)
        self.update_status("Cleared all images")
    
    def browse_output(self):
        """Browse for output file or directory."""
        if self.mode_var.get() == "single":
            # Single PDF file
            file_path = filedialog.asksaveasfilename(
                title="Save PDF As",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            if file_path:
                self.output_var.set(file_path)
        else:
            # Directory for separate PDFs
            directory = filedialog.askdirectory(title="Select Output Directory")
            if directory:
                self.output_var.set(directory)
    
    def update_status(self, message):
        """Update the status label."""
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def convert_images(self):
        """Convert the selected images to PDF."""
        if not self.selected_images:
            messagebox.showwarning("Warning", "Please select at least one image.")
            return
        
        try:
            margin = int(self.margin_var.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid margin value. Please enter a number.")
            return
        
        # Update converter settings
        self.converter = ImageToPDFConverter(
            page_size=self.page_size_var.get(),
            margin=margin
        )
        
        # Start conversion in a separate thread
        self.convert_button.configure(state='disabled')
        self.progress.start()
        
        thread = threading.Thread(target=self._convert_thread)
        thread.daemon = True
        thread.start()
    
    def _convert_thread(self):
        """Convert images in a separate thread."""
        try:
            if self.mode_var.get() == "single":
                # Single PDF mode
                output_path = self.output_var.get() or "converted_images.pdf"
                self.converter.convert_multiple_images(self.selected_images, output_path)
                self.root.after(0, lambda: self.conversion_complete(f"Created: {output_path}"))
            
            else:
                # Separate PDFs mode
                output_dir = self.output_var.get() or os.getcwd()
                created_files = []
                
                for i, image_path in enumerate(self.selected_images):
                    try:
                        output_name = Path(image_path).stem + '.pdf'
                        output_path = os.path.join(output_dir, output_name)
                        self.converter.convert_single_image(image_path, output_path)
                        created_files.append(output_path)
                        
                        # Update progress
                        progress_msg = f"Converting {i+1}/{len(self.selected_images)}: {Path(image_path).name}"
                        self.root.after(0, lambda msg=progress_msg: self.update_status(msg))
                    
                    except Exception as e:
                        print(f"Error converting {image_path}: {e}")
                
                completion_msg = f"Conversion completed! Created {len(created_files)} PDF files."
                self.root.after(0, lambda: self.conversion_complete(completion_msg))
        
        except Exception as e:
            error_msg = f"Conversion failed: {str(e)}"
            self.root.after(0, lambda: self.conversion_error(error_msg))
    
    def conversion_complete(self, message):
        """Handle successful conversion completion."""
        self.progress.stop()
        self.convert_button.configure(state='normal')
        self.update_status(message)
        messagebox.showinfo("Success", message)
    
    def conversion_error(self, message):
        """Handle conversion error."""
        self.progress.stop()
        self.convert_button.configure(state='normal')
        self.update_status("Conversion failed")
        messagebox.showerror("Error", message)


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = ImageToPDFGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main() 