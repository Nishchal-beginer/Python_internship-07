import os
from PIL import Image

def batch_resize_images(input_folder, output_folder, size=(800, 800)):
    """
    Resizes all images in the input folder and saves them to the output folder.

    :param input_folder: Path to folder containing images
    :param output_folder: Path where resized images will be saved
    :param size: Tuple (width, height)
    """

    # Create output folder if needed
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    img = img.resize(size)
                    img.save(output_path)
                    print(f"Resized: {filename}")

            except Exception as e:
                print(f"Error resizing {filename}: {e}")

    print("Batch resizing complete!")

# -----------------------------------
# ✅ CALL THE FUNCTION *HERE* (outside)
# -----------------------------------
batch_resize_images(
    r"d:\Internships\Python internship\Python_internship-07\input_folder",
    r"d:\Internships\Python internship\Python_internship-07\output_folder",
    size=(800, 800)
)
