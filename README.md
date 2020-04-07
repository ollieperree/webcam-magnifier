# Webcam Magnifier

> **_NOTE:_** This is still a work in progress. If you are visually impaired and you want to set something like this up but don't know how, email me at `oliverperree@gmail.com`.

![Screenshot of the magnifier in binary mode (black on yellow)](https://i.postimg.cc/cCcPtcb3/magnifier2.png)
Screenshot of the magnifier in binary mode (black on yellow)

This script mimics the functionality of really expensive  (£1000+) video magnifiers [\[1\]][1][\[2\]][2][\[3\]][3] using an £80 webcam (e.g. [Logitech C920](https://www.amazon.co.uk/dp/B006A2Q81M?tag=duc08-21&linkCode=osi&th=1&psc=1)), a computer and a monitor (maybe £300 if you want to buy a decent-sized dedicated monitor).

Current functionality:

- Binarisation (convert the image to two colours, to make text stand out more).
- Change foreground and background colour of text.
- Zoom in and out (digital zoom)

Intended functionality:

- Improved upsampling using deep neural network "superresolution" (to get a clearer image when zoomed in).

## Should I try this?

If you are visually impaired and you want a video magnifier for reading, then you might as well try a solution like this before buying expensive hardware. When I get round to setting this up for my grandmother I will be able to comment on how it compares to the Clover 10 portable video magnifier (but the quality of the image when zoomed in will almost certainly be worse).

The reason I made this in the first place is so that the camera can be mounted so that a whole page of a book can be seen by the camera (the Clover 10 sits way to close to the page so you have to move it around).

The following image shows the magnifier zoomed in so that a single word fills the screen:

![Screenshot of the magnifier in use showing the word "introduce" which fills the screen and is legible but quite pixellated.](https://i.postimg.cc/13Nj0MkF/magnifer1.png)

At this level of zoom (which is actually just cropping the image of the webcam and scaling it up) the text qulity is poor, but I hope that in future I will be able to process the image give the letters a smoother, clean outline.


## Requirements

- Python 3.7
    - numpy==1.15.4
    - pynput==1.6.3
    - opencv-python==4.1.1.26
- v4l-utils-1.16.6-1

## See also

- [OpenMagnifier](https://github.com/ghoelzl/OpenMagnifier)


[1]: https://shop.rnib.org.uk/magnification/transformer-hd-portable-magnifier-camera-solution.html
[2]: https://shop.rnib.org.uk/magnification/topaz-phd-15-portable-video-magnifier-a49eea.html
[3]: https://shop.rnib.org.uk/magnification/prodigi-duo-20-inch-screen-cctv.html
