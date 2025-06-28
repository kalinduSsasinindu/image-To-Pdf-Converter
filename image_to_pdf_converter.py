#!/usr/bin/env python3
"""
Image to PDF Converter
A Python script to convert images (JPEG, PNG, BMP, TIFF, etc.) to PDF format.
Supports single image conversion and batch conversion of multiple images.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple
import glob

try:
    from PIL import Image
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.utils import ImageReader
except ImportError as e:
    print(f"Error importing required packages: {e}")
    print("Please install required packages: pip install Pillow reportlab")
    sys.exit(1)


class ImageToPDFConverter:
    """A class to handle image to PDF conversion operations."""
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif', '.webp'}
    
    def __init__(self, page_size='A4', margin=50):
        """
        Initialize the converter.
        
        Args:
            page_size (str): Page size ('A4' or 'Letter')
            margin (int): Margin in points
        """
        self.page_size = A4 if page_size.upper() == 'A4' else letter
        self.margin = margin
        
    def is_supported_format(self, file_path: str) -> bool:
        """Check if the file format is supported."""
        return Path(file_path).suffix.lower() in self.SUPPORTED_FORMATS
    
    def get_image_dimensions(self, image_path: str) -> Tuple[int, int]:
        """Get image dimensions."""
        with Image.open(image_path) as img:
            return img.size
    
    def calculate_image_size(self, image_path: str) -> Tuple[float, float]:
        """
        Calculate the size to fit the image on the PDF page while maintaining aspect ratio.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            Tuple[float, float]: Width and height for the PDF
        """
        img_width, img_height = self.get_image_dimensions(image_path)
        page_width, page_height = self.page_size
        
        # Calculate available space (accounting for margins)
        available_width = page_width - (2 * self.margin)
        available_height = page_height - (2 * self.margin)
        
        # Calculate scaling factors
        width_scale = available_width / img_width
        height_scale = available_height / img_height
        
        # Use the smaller scale to maintain aspect ratio
        scale = min(width_scale, height_scale)
        
        return img_width * scale, img_height * scale
    
    def convert_single_image(self, image_path: str, output_path: str = None) -> str:
        """
        Convert a single image to PDF.
        
        Args:
            image_path (str): Path to the input image
            output_path (str): Path for the output PDF (optional)
            
        Returns:
            str: Path to the created PDF file
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        if not self.is_supported_format(image_path):
            raise ValueError(f"Unsupported image format: {Path(image_path).suffix}")
        
        # Generate output path if not provided
        if output_path is None:
            output_path = str(Path(image_path).with_suffix('.pdf'))
        
        # Calculate image size for PDF
        pdf_width, pdf_height = self.calculate_image_size(image_path)
        page_width, page_height = self.page_size
        
        # Calculate position to center the image
        x = (page_width - pdf_width) / 2
        y = (page_height - pdf_height) / 2
        
        # Create PDF
        c = canvas.Canvas(output_path, pagesize=self.page_size)
        c.drawImage(image_path, x, y, width=pdf_width, height=pdf_height)
        c.save()
        
        print(f"✓ Converted: {image_path} → {output_path}")
        return output_path
    
    def convert_multiple_images(self, image_paths: List[str], output_path: str) -> str:
        """
        Convert multiple images into a single PDF with each image on a separate page.
        
        Args:
            image_paths (List[str]): List of image file paths
            output_path (str): Path for the output PDF
            
        Returns:
            str: Path to the created PDF file
        """
        if not image_paths:
            raise ValueError("No image paths provided")
        
        # Filter out unsupported formats and non-existent files
        valid_paths = []
        for path in image_paths:
            if not os.path.exists(path):
                print(f"⚠ Warning: File not found, skipping: {path}")
                continue
            if not self.is_supported_format(path):
                print(f"⚠ Warning: Unsupported format, skipping: {path}")
                continue
            valid_paths.append(path)
        
        if not valid_paths:
            raise ValueError("No valid image files found")
        
        c = canvas.Canvas(output_path, pagesize=self.page_size)
        page_width, page_height = self.page_size
        
        for i, image_path in enumerate(valid_paths):
            # Calculate image size for PDF
            pdf_width, pdf_height = self.calculate_image_size(image_path)
            
            # Calculate position to center the image
            x = (page_width - pdf_width) / 2
            y = (page_height - pdf_height) / 2
            
            # Add image to current page
            c.drawImage(image_path, x, y, width=pdf_width, height=pdf_height)
            
            # Add new page if not the last image
            if i < len(valid_paths) - 1:
                c.showPage()
            
            print(f"✓ Added to PDF: {image_path}")
        
        c.save()
        print(f"✓ Created multi-page PDF: {output_path}")
        return output_path
    
    def batch_convert_directory(self, directory_path: str, output_dir: str = None) -> List[str]:
        """
        Convert all images in a directory to individual PDF files.
        
        Args:
            directory_path (str): Path to the directory containing images
            output_dir (str): Output directory for PDF files (optional)
            
        Returns:
            List[str]: List of created PDF file paths
        """
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        
        # Find all image files in the directory
        image_files = []
        for ext in self.SUPPORTED_FORMATS:
            pattern = os.path.join(directory_path, f"*{ext}")
            image_files.extend(glob.glob(pattern))
            pattern = os.path.join(directory_path, f"*{ext.upper()}")
            image_files.extend(glob.glob(pattern))
        
        if not image_files:
            print(f"No supported image files found in: {directory_path}")
            return []
        
        # Set output directory
        if output_dir is None:
            output_dir = directory_path
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        created_pdfs = []
        for image_file in image_files:
            try:
                output_pdf = os.path.join(output_dir, Path(image_file).stem + '.pdf')
                self.convert_single_image(image_file, output_pdf)
                created_pdfs.append(output_pdf)
            except Exception as e:
                print(f"✗ Error converting {image_file}: {e}")
        
        print(f"✓ Batch conversion completed. Created {len(created_pdfs)} PDF files.")
        return created_pdfs


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert images to PDF format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python image_to_pdf_converter.py image.jpg
  python image_to_pdf_converter.py image.jpg -o output.pdf
  python image_to_pdf_converter.py img1.jpg img2.png -m -o combined.pdf
  python image_to_pdf_converter.py -d /path/to/images/
  python image_to_pdf_converter.py -d /path/to/images/ --merge-all combined.pdf
        """
    )
    
    # Input options
    parser.add_argument('images', nargs='*', help='Image file(s) to convert')
    parser.add_argument('-d', '--directory', help='Directory containing images to convert')
    
    # Output options
    parser.add_argument('-o', '--output', help='Output PDF file path')
    parser.add_argument('-m', '--merge', action='store_true', 
                       help='Merge multiple images into a single PDF')
    parser.add_argument('--merge-all', help='Merge all images in directory into single PDF')
    
    # PDF options
    parser.add_argument('--page-size', choices=['A4', 'Letter'], default='A4',
                       help='PDF page size (default: A4)')
    parser.add_argument('--margin', type=int, default=50,
                       help='Page margin in points (default: 50)')
    
    args = parser.parse_args()
    
    # Initialize converter
    converter = ImageToPDFConverter(page_size=args.page_size, margin=args.margin)
    
    try:
        if args.directory:
            # Directory mode
            if args.merge_all:
                # Merge all images in directory into one PDF
                image_files = []
                for ext in converter.SUPPORTED_FORMATS:
                    pattern = os.path.join(args.directory, f"*{ext}")
                    image_files.extend(glob.glob(pattern))
                    pattern = os.path.join(args.directory, f"*{ext.upper()}")
                    image_files.extend(glob.glob(pattern))
                
                if image_files:
                    converter.convert_multiple_images(image_files, args.merge_all)
                else:
                    print(f"No supported image files found in: {args.directory}")
            else:
                # Convert each image to separate PDF
                converter.batch_convert_directory(args.directory, 
                                                args.output if args.output else None)
        
        elif args.images:
            # Image file(s) mode
            if args.merge or (len(args.images) > 1 and args.output):
                # Merge multiple images into one PDF
                output_path = args.output or 'merged_images.pdf'
                converter.convert_multiple_images(args.images, output_path)
            else:
                # Convert each image to separate PDF
                for image_path in args.images:
                    converter.convert_single_image(image_path, args.output)
        
        else:
            parser.print_help()
            print("\nError: Please provide either image file(s) or a directory.")
            sys.exit(1)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 