from avatar import AvatarGenerator

#initialize image generator
obj = AvatarGenerator()

#with default parameters
for i in range(20,35):
    img = obj.CreateAvatar() 
    img.save('images/sample'+str(i)+'.png')

# #with parameters and with border
# img = obj.CreateAvatar(xy_axis=5,pixels=300,background_color='white',border=True,border_width=25) 
# img.save('Advance-Parameters-border.png')

# #with parameters and no border
# img = obj.CreateAvatar(xy_axis=5,pixels=300,background_color='white',border=False) 
# img.save('Advance-Parameters-noborder.png')