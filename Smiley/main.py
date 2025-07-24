import cv2
import os
import datetime
import time
import threading
try:
    import pyttsx3
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False
    print("pyttsx3 not available. Voice feedback disabled.")

class SmileSnapAI:
    def __init__(self):
        # Initialize OpenCV cascades
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        
        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        
        # Smile detection state
        self.smile_detected_time = 0
        self.cooldown_period = 3  # Seconds to wait before detecting next smile
        self.last_capture_time = 0
        
        # Create captured folder if it doesn't exist
        self.captured_folder = "captured"
        if not os.path.exists(self.captured_folder):
            os.makedirs(self.captured_folder)
            print(f"Created {self.captured_folder} folder")
        
        # Initialize text-to-speech engine
        if VOICE_AVAILABLE:
            self.tts_engine = pyttsx3.init()
            self.setup_voice()
        
        print("SmileSnap AI initialized successfully!")
        print("Press 'q' to quit the application")
    
    def setup_voice(self):
        """Configure the text-to-speech engine"""
        if VOICE_AVAILABLE:
            try:
                # Set voice properties
                voices = self.tts_engine.getProperty('voices')
                if voices:
                    self.tts_engine.setProperty('voice', voices[0].id)  # Use first available voice
                self.tts_engine.setProperty('rate', 150)  # Speech rate
                self.tts_engine.setProperty('volume', 0.8)  # Volume level
            except Exception as e:
                print(f"Voice setup error: {e}")
    
    def speak_async(self, message):
        """Speak message in a separate thread to avoid blocking"""
        if VOICE_AVAILABLE:
            def speak():
                try:
                    self.tts_engine.say(message)
                    self.tts_engine.runAndWait()
                except Exception as e:
                    print(f"Speech error: {e}")
            
            # Run speech in separate thread
            speech_thread = threading.Thread(target=speak)
            speech_thread.daemon = True
            speech_thread.start()
    
    def capture_smile_photo(self, frame):
        """Capture and save the photo when smile is detected"""
        # Generate timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"smile_{timestamp}.jpg"
        filepath = os.path.join(self.captured_folder, filename)
        
        # Save the photo
        cv2.imwrite(filepath, frame)
        print(f"📸 Smile captured! Saved as: {filename}")
        
        # Speak confirmation message
        self.speak_async("Nice smile!")
        
        return filepath
    
    def detect_faces_and_smiles(self, frame):
        """Detect faces and smiles in the frame"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        smile_detected = False
        current_time = time.time()
        
        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Region of interest for smile detection (lower half of face)
            roi_gray = gray[y + h//2:y + h, x:x + w]
            roi_color = frame[y + h//2:y + h, x:x + w]
            
            # Detect smiles in the face region
            smiles = self.smile_cascade.detectMultiScale(
                roi_gray, 
                scaleFactor=1.8, 
                minNeighbors=20,
                minSize=(25, 25)
            )
            
            if len(smiles) > 0:
                smile_detected = True
                
                # Draw rectangle around smile
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
                
                # Add "Smile Detected!" text
                cv2.putText(frame, "Smile Detected!", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                # Capture photo if cooldown period has passed
                if current_time - self.last_capture_time > self.cooldown_period:
                    self.capture_smile_photo(frame)
                    self.last_capture_time = current_time
            else:
                # Add "Looking for smiles..." text when no smile detected
                cv2.putText(frame, "Looking for smiles...", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        return frame, smile_detected
    
    def run(self):
        """Main application loop"""
        if not self.cap.isOpened():
            print("Error: Could not access webcam")
            return
        
        print("\n🎉 SmileSnap AI is running!")
        print("📹 Webcam feed started - smile for the camera!")
        print("⌨️ Press 'q' to quit")
        
        while True:
            # Capture frame from webcam
            ret, frame = self.cap.read()
            
            if not ret:
                print("Error: Could not read frame from webcam")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Detect faces and smiles
            frame, smile_detected = self.detect_faces_and_smiles(frame)
            
            # Add application title
            cv2.putText(frame, "SmileSnap AI - Smile Detection", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
            # Add instructions
            cv2.putText(frame, "Press 'q' to quit", (10, frame.shape[0] - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Display the frame
            cv2.imshow('SmileSnap AI', frame)
            
            # Check for 'q' key press to quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("\n👋 Thanks for using SmileSnap AI!")
                break
    
    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        if VOICE_AVAILABLE:
            try:
                self.tts_engine.stop()
            except:
                pass

def main():
    """Main function to run SmileSnap AI"""
    app = SmileSnapAI()
    
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n⚡ Application interrupted by user")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        app.cleanup()

if __name__ == "__main__":
    main()
