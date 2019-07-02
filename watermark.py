import os

print('Adds logo.png to video file')

infile = input("Enter input filename: ")
outfile = input("Enter output filename: ")

os.system('ffmpeg -i ' + infile + ' -vf "movie=logo.png [watermark]; [in][watermark] overlay=main_w-overlay_w:main_h-overlay_h [out]" ' + outfile)
