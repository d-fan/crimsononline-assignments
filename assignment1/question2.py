import json
from PIL import Image

class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    
    def __init__(self, headline = None, content = None, creator = None, related_image = None):
        self.headline = headline
        self.content = content
        self.creator = creator
        if isinstance(related_image, Picture):
            # Created from a Picture object
            self.related_image = related_image
        else:
            # Create the picture from a string
            self.related_image = Picture(related_image)

    def show(self):
        print("Headline: " + self.headline + 
              "\nAuthor: " + self.creator + 
              "\nContent: " + self.content)
        self.related_image.show()

    def save(self, filename):
        try:
            with open(filename, 'w') as f:
                f.write(json.dumps([{"headline":self.headline},
                                    {"content": self.content},
                                    {"creator": self.creator},
                                    {"related_image": [{"image_file": self.related_image.image_file},
                                                       {"creator": self.related_image.creator}]}]))
        except IOError as e:
            print "IOError {0}: {1}".format(e.errno, e.strerror)
            return

    def load(self, filename):
        try:
            with open(filename, 'r') as f:
                encoded = f.read();
        except IOError as e:
            print "IOError {0}: {1}".format(e.errno, e.strerror)
            return
        loaded = json.loads(encoded)
        self.headline = loaded[0]['headline']
        self.content  = loaded[1]['content']
        self.creator  = loaded[2]['creator']
        self.related_image = Picture(loaded[3]['related_image'][0]['image_file'], 
                                     loaded[3]['related_image'][1]['creator'])

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    def __init__(self, image_file, creator = None):
        self.image_file = image_file
        self.creator = creator

    def show(self):
        try:
            im = Image.open(self.image_file)
            im.show()
        except IOError as e:
            print "IOError {0}: {1}".format(e.errno, e.strerror)
            return

    def __str__(self):
        return json.dumps([{"image_file":self.image_file},{"creator":self.creator}])