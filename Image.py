from pywhatkit import image_to_ascii_art
import os

def get_image_path():
    while True:
        image_path = input('Enter the image path: ')
        if os.path.exists(image_path):
            return image_path
        else:
            print('No such file or directory! Please try again.')

def main():
    image_path = get_image_path()
    output_text_file = 'art.txt'

    image_to_ascii_art(image_path, output_text_file)

    with open(output_text_file, 'r') as file:
        ascii_art_text = file.read()

    print(ascii_art_text)

if __name__ == "__main__":
    main()
