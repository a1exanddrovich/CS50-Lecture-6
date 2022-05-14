from PIL import Image, ImageFilter

imageBeforeProcessing = Image.open("sample.bmp")
imageAfterProcessing = imageBeforeProcessing.filter(ImageFilter.BoxBlur(1))
imageAfterProcessing.save("sampleOut.bmp")




