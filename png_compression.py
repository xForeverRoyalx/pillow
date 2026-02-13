from PIL import Image
import os


def compress_png_logo(input_path, output_path, quality=85, max_width=800):
    """
    Compress PNG image for web use while maintaining transparency

    Args:
        input_path: Path to input PNG file
        output_path: Path for compressed output file
        quality: Quality for JPEG conversion (0-100), only used if converting to JPEG
        max_width: Maximum width for resizing (maintains aspect ratio)
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            print(f"Original image size: {img.size}")
            print(f"Original file size: {os.path.getsize(input_path) / 1024:.1f} KB")

            # Convert RGBA to RGB if saving as JPEG (removes transparency)
            # Keep as PNG to preserve transparency for logos
            if img.mode in ('RGBA', 'LA'):
                print("Image has transparency - keeping as PNG")
                output_format = 'PNG'
                output_path = output_path.replace('.jpg', '.png').replace('.jpeg', '.png')
            else:
                output_format = 'PNG'

            # Resize if image is too large
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"Resized to: {img.size}")

            # Save with optimization
            if output_format == 'PNG':
                # For PNG: use optimize and reduce colors if possible
                img.save(output_path, 'PNG', optimize=True)
            else:
                # For JPEG: use quality setting
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(output_path, 'JPEG', optimize=True, quality=quality)

            # Print results
            compressed_size = os.path.getsize(output_path) / 1024
            compression_ratio = (1 - compressed_size / (os.path.getsize(input_path) / 1024)) * 100

            print(f"Compressed file size: {compressed_size:.1f} KB")
            print(f"Compression ratio: {compression_ratio:.1f}%")
            print(f"Saved as: {output_path}")

    except Exception as e:
        print(f"Error processing image: {e}")


def main():
    input_file = "c:/assets/quickerqr_logo_raw.png"

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found in current directory")
        return

    # Generate output filename
    base_name = os.path.splitext(input_file)[0]
    output_file = f"outputs/{base_name}_compressed.png"

    print("Compressing PNG logo for web use...")
    print("=" * 40)

    # Compress with default settings (good for web logos)
    compress_png_logo(input_file, output_file, max_width=800)

    # Optional: Create additional versions
    print("\n" + "=" * 40)
    print("Creating smaller version...")
    small_output = f"outputs/{base_name}_small.png"
    compress_png_logo(input_file, small_output, max_width=400)

    print("\n" + "=" * 40)
    print("Creating tiny version for favicons/thumbnails...")
    tiny_output = f"outputs/{base_name}_tiny.png"
    compress_png_logo(input_file, tiny_output, max_width=128)


if __name__ == "__main__":
    main()