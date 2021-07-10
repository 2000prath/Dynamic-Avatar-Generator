
# Dynamic Profile Image Generator
This library will help you to generate profile image for newly registered user on your application, like GitHub create profile picture for new users E.g. <br>
 <br>
![75605781 (2)](https://user-images.githubusercontent.com/40172813/125158648-02982e00-e190-11eb-912d-2c55b1051019.png)


## Generated images
![generatedimg](https://user-images.githubusercontent.com/40172813/125158557-9a494c80-e18f-11eb-956a-d49f42a6a6db.png)

## Usage
```python
import avatar

#initialize image generator
obj = GenerateImage()

#image block size with rows and columns
row_columns = 5
pixel_size = 300
background_color = 'lightgrey'
img = obj.BitImage(row_columns,pixel_size,background_color) 
```
 
`img.show()` to open generated image <br>
`img.save('image.png')` to save image with image name <br>
`obj.toBase64(img)` to get Base64 value of generated image <br>


