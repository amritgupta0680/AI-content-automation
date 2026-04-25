from PIL import Image, ImageDraw, ImageFont
import os

def create_social_image(text, platform="linkedin", output="post.png"):
    """Create professional social media image"""
    # Platform-specific dimensions
    sizes = {
        "linkedin": (1200, 628),
        "twitter": (1200, 675),
        "instagram": (1080, 1080)
    }
    size = sizes.get(platform, (1200, 628))
    
    # Create gradient background
    img = Image.new('RGB', size, color=(15, 25, 45))
    draw = ImageDraw.Draw(img)
    
    # Try to load font, fallback to default
    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_text = ImageFont.truetype("arial.ttf", 36)
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
    
    # Title
    title = text[:50] + "..." if len(text) > 50 else text
    draw.text((80, 100), title, fill=(255, 255, 255), font=font_title)
    
    # Subtitle
    subtitle = text[:100] if len(text) > 50 else ""
    if subtitle:
        draw.text((80, 220), subtitle, fill=(200, 200, 200), font=font_text)
    
    # Save
    os.makedirs("outputs", exist_ok=True)
    img.save(f"outputs/{output}")
    return f"outputs/{output}"