import cv2

def hide_data(image_path, secret_message, output_path):

    data = ''.join(format(ord(i), '08b') for i in secret_message)
    data_len = len(data)
    data_index = 0


    img = cv2.imread(image_path)

    for row in img:
        for pixel in row:
            for color in range(3):  
                if data_index < data_len:
                    
                    pixel[color] = int(format(pixel[color], '08b')[:-1] + data[data_index], 2)
                    data_index += 1
                if data_index >= data_len:
                    break
            if data_index >= data_len:
                break
        if data_index >= data_len:
            break

    
    cv2.imwrite(output_path, img)

def retrieve_data(image_path):
    img = cv2.imread(image_path)
    binary_data = ""

    for row in img:
        for pixel in row:
            for color in range(3):
                binary_data += format(pixel[color], '08b')[-1]

    
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte:
            message += chr(int(byte, 2))

    return message


image_path = r'V:\Projects\AICTE\download.jpg'
output_path = r'V:\Projects\AICTE\secret_image.png'


secret_message = input("Enter the secret message to hide: ")
key = input("Enter a key : ")


hide_data(image_path, secret_message, output_path)
print(f'Message "{secret_message}" hidden in image.')


retrieved_message = retrieve_data(output_path)
print(f'The hidden message is: "{retrieved_message}"')
