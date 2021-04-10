from PIL import Image
from PIL import ImageGrab
import pytesseract
import pyperclip
import time

'''
This loop is always running. Whenever the clipboard changes,
it checks to see if it was an image and if it is
it extracts the text and places it into the clipboard.
'''
def main():
    # Set path to tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

    recent_value = ''
    while True:
        tmp_value = pyperclip.paste()
        if recent_value != tmp_value:
            recent_value = tmp_value
            print('Clipboard value changed!')
            
            # This if statement checks if the change in the clipboard was an image
            if len(recent_value.strip()) == 0:
                image_text = get_image_from_clipboard()

                # Set the clipboard text to be the extracted text from the image
                pyperclip.copy(image_text)
        time.sleep(0.1)
'''
This function returns the text in an image stripped of all new lines
'''
def get_text_from_image(image):
    return pytesseract.image_to_string(image).replace('\n', ' ').replace('\r', ' ')

def get_image_from_clipboard():
    # Get the image from the clipboard and extract the text from it
    im = ImageGrab.grabclipboard()
    image_text = get_text_from_image(im)

    return image_text
    

if __name__ == '__main__':
    main()