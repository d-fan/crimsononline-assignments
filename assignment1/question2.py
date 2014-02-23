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
    
    def __init__(self, headline, content, creator, related_image):
        self.headline = headline
        self.content = content
        self.creator = creator
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
                                    {"related_image": self.related_image.__str__()}]))
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
        self.headline = loaded['headline']
        self.content  = loaded['content']
        self.creator  = loaded['creator']
        self.related_image = Picture(loaded['related_image'])

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    def __init__(self, image_file, creator):
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
        return self.image_file