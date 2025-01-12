import pywhatkit as kit
import time

def Play_Youtube_Videos(keywords):
    try:
        kit.playonyt(keywords)
        print("Found Result")
    except Exception as e:
        print(f"Search Not Found{e}")

def Search_On_Google(keywords):
    try:
        kit.search(keywords)
        print("Found Result")
    except Exception as e:
        print(f"Search Not Found{e}")

def send_whatsapp_message(phone_number, message, hour, minute):
    """
    Sends a WhatsApp text message at a specific time.
    """
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_whatsapp_image(phone_number, image_path, caption):
    """
    Sends an image on WhatsApp immediately.
    """
    try:
        kit.sendwhats_image(phone_number, image_path, caption)
        print("Image sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_whatsapp_video(phone_number, video_path):
    """
    Sends a video on WhatsApp.
    """
    print("For videos, you'll need to upload them manually via WhatsApp Web.")
    print(f"Video path: {video_path}")

# Example usage:
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Schedule a text message")
    print("2. Send an image")
    print("3. Send a video")
    print("4. Seacrh Youtube Videos")
    print("5. Search with Keywords")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        phone = input("Enter the phone number (with country code): ")
        msg = input("Enter the message: ")
        send_time = input("Enter time in HH:MM format (24-hour): ").split(":")
        hour, minute = int(send_time[0]), int(send_time[1])
        send_whatsapp_message(phone, msg, hour, minute)
    elif choice == '2':
        phone = input("Enter the phone number (with country code): ")
        img_path = input("Enter the image file path: ")
        caption = input("Enter the image caption: ")
        send_whatsapp_image(phone, img_path, caption)
    elif choice == '3':
        phone = input("Enter the phone number (with country code): ")
        vid_path = input("Enter the video file path: ")
        send_whatsapp_video(phone, vid_path)
    elif choice =='4':
        word = input("Enter a Keyword (in double quotation): ")
        Play_Youtube_Videos(word)
    elif choice =='5':
        word = input("Enter a Keyword (in double quotation):")
        Search_On_Google(word)
    else:
        print("Invalid choice.")
