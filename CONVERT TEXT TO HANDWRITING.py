import pywhatkit

# specify the text to be converted
text = "Hello World, This is Venu Here "

# specify the name of the output file (including extension)
filename = "output.png"

# convert the text to handwriting and save it as an image file
pywhatkit.text_to_handwriting(text, filename)
