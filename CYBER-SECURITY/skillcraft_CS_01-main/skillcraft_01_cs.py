from PIL import Image
import random

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()
    
    for i in range(width):
        for j in range(height):
            # Swap pixel with a random pixel
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pixels[i, j], pixels[x, y] = pixels[x, y], pixels[i, j]
    
    return image

def apply_math_operation(image, operation):
    width, height = image.size
    pixels = image.load()
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            
            if operation == 'add':
                r = (r + 50) % 256
                g = (g + 50) % 256
                b = (b + 50) % 256
            elif operation == 'subtract':
                r = (r - 50) % 256
                g = (g - 50) % 256
                b = (b - 50) % 256
            elif operation == 'multiply':
                r = (r * 2) % 256
                g = (g * 2) % 256
                b = (b * 2) % 256
            elif operation == 'divide':
                r = (r // 2) % 256
                g = (g // 2) % 256
                b = (b // 2) % 256
            
            pixels[i, j] = (r, g, b)
    
    return image

def main():
    # Load the image
    image_path = input("Enter the path of the image: ")
    image = Image.open(image_path)
    
    # Choose the operation
    operation = input("Choose an operation - (swap, add, subtract, multiply, divide): ").lower()
    
    if operation == 'swap':
        encrypted_image = swap_pixels(image)
    elif operation in ['add', 'subtract', 'multiply', 'divide']:
        encrypted_image = apply_math_operation(image, operation)
    else:
        print("Invalid operation")
        return
    
    # Save the encrypted image
    encrypted_image_path = input("Enter the path to save the encrypted image: ")
    encrypted_image.save(encrypted_image_path)
    
    print(f"Encrypted image saved to {encrypted_image_path}")

if __name__ == "__main__":
    main()
