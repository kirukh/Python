import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pytesseract

# Optional: Setze Tesseract Pfad (nur für Windows nötig)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Funktion zum Öffnen eines Dateidialogs


def select_image():
    Tk().withdraw()
    return askopenfilename(
        title="Wähle ein Bild mit Buchtitel aus",
        filetypes=[("Bilddateien", "*.jpg *.jpeg *.png *.bmp")]
    )


# Schritt 1: Bild auswählen
image_path = select_image()
if not image_path:
    print("Kein Bild ausgewählt.")
    exit()

# Schritt 2: Bild laden
image = cv2.imread(image_path)
clone = image.copy()

# Schritt 3: ROI (Region of Interest) interaktiv auswählen
roi = cv2.selectROI("Bild - Ziehe ein Rechteck um den Titel",
                    image, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

x, y, w, h = roi
if w == 0 or h == 0:
    print("Kein Bereich ausgewählt.")
    exit()

# Schritt 4: Zuschneiden auf den ausgewählten Bereich
roi_image = clone[y:y+h, x:x+w]

# Schritt 5: Optional: Vorverarbeitung (Graustufen + Threshold)
gray = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Schritt 6: OCR auf dem ausgewählten Bereich
text = pytesseract.image_to_string(thresh, lang='deu')

print("\nErkannter Text im ausgewählten Bereich:\n")
print(text)
