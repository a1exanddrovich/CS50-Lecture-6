from PIL import Image, ImageFilter

imageBeforeProcessing = Image.open("sample.bmp")
imageAfterProcessing = imageBeforeProcessing.filter(ImageFilter.FIND_EDGES)
imageAfterProcessing.save("sampleOut.bmp")
