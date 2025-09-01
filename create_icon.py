from PIL import Image, ImageDraw
import os

# Create a simple water drop icon
def create_water_icon():
    size = 64
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Water drop shape
    center_x, center_y = size // 2, size // 2 + 5
    
    # Main drop body (circle)
    drop_radius = 20
    draw.ellipse([center_x - drop_radius, center_y - drop_radius, 
                  center_x + drop_radius, center_y + drop_radius], 
                 fill=(52, 152, 219, 255))
    
    # Drop top (teardrop point)
    points = [
        (center_x, center_y - 35),  # Top point
        (center_x - 8, center_y - 20),  # Left curve
        (center_x + 8, center_y - 20)   # Right curve
    ]
    draw.polygon(points, fill=(52, 152, 219, 255))
    
    # Highlight
    draw.ellipse([center_x - 6, center_y - 10, center_x + 2, center_y - 2], 
                 fill=(174, 214, 241, 180))
    
    img.save('water_icon.ico', format='ICO', sizes=[(32, 32), (48, 48), (64, 64)])
    print("Icon created: water_icon.ico")

if __name__ == "__main__":
    try:
        create_water_icon()
    except ImportError:
        print("Installing Pillow...")
        os.system("pip install Pillow")
        create_water_icon()