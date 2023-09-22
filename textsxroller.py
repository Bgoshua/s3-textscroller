# scrolling text with MatrixPortal S3 connected to 64x32 RGB display
# don’t forget to install all required libraries

Import time
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_matrixportal.matrixportal import MatrixPortal

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL)

# Set up the display group
display = matrixportal.display
group = displayio.Group()
display.show(group)

# Create a label with "hello world" text
# Color code is set to red 
text = "Hello World"
text_area = label.Label(
    terminalio.FONT, text=text, color=0xFF0000, x=display.width // 2, y=display.height // 2
)
text_area.anchor_point = (0.5, 0.5)
group.append(text_area)

# Calculate initial and final positions for scrolling
start_x = display.width
end_x = -text_area.width

# Speed is controlled from time.sleep 

while True:
    for x in range(start_x, end_x, -1):
        text_area.x = x
        display.show(group)
        matrixportal.display.refresh()
	time.sleep(0.03)
