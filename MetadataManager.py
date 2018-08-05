#!/usr/bin/env python3
import pyexiv2
import ByteString

# ------edit title metadata
def hasAnyTitle(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.XPTitle' in f_metadata.exif_keys)):
        # print("this file already has title data")
        return True
    # print("this file has no title data")
    return False

def hasTitle(p_filename, y):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def getTitle(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def setTitle(p_filename, y):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def removeTitle(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

# ------edit artist metadata
def hasAnyArtist(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.Artist' in f_metadata.exif_keys)):
        # print("this file already has artist data")
        return True
    # print("this file has no artist data")
    return False

def hasArtist(p_filename, y):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def getArtist(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def setArtist(p_filename, y):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def removeArtist(p_filename, y):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

# -----edit tag metadata

def hasAnyTags(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.XPKeywords' in f_metadata.exif_keys)):
        # print("this file already has tag data")
        return True
    # print("this file has no tag data")
    return False

def hasTags(p_filename, p_tag):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    f_metaData = pyexiv2.ImageMetadata(p_filename)
    f_metaData.read()
    f_keywords = f_metaData['Exif.Image.XPKeywords'];
    f_bustedTagString = pyexiv2.utils.undefined_to_string(f_keywords.value)
    if p_tag in ByteString.stringHexTrim(f_bustedTagString):
        #print("This file already has the tag \"", p_tag ,"\"", sep='')
        return True
    return False

def getTags(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def setTags(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def addTag(p_filename, p_tag):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO

    f_metaData = pyexiv2.ImageMetadata(p_filename)
    f_metaData.read()
    f_keywords = f_metaData['Exif.Image.XPKeywords'];
    key = 'Exif.Image.XPKeywords'
    f_bustedTagString = pyexiv2.utils.undefined_to_string(f_keywords.value)
    # print("freshExifTags. file has these tags:", stringHexTrim(f_bl))
    if p_tag in ByteString.stringHexTrim(f_bustedTagString):
        print("This file already has the tag \"", p_tag, "\"", sep='')
        return
        # or we could just exit the function here
    f_newTagString = ByteString.stringHexify(p_tag) + ";\x00" + f_bustedTagString
    # print("freshExifTags. file will now have these tags:", stringHexTrim(f_newTagString))
    value = pyexiv2.utils.string_to_undefined(f_newTagString)
    f_metaData[key] = pyexiv2.ExifTag(key, value)
    f_metaData.write()
    return
    
    
    
    
    
    
    
    
    return

def removeTag(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

# -------edit description metadata

def hasAnyDescr(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.XPComment' in f_metadata.exif_keys)):
        # print("this file already has description data")
        return True
    # print("this file has no description data")
    return False

def hasDescr(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def getDescr(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def setDescr(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def addDescr(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def removeDescr(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

# ------edit rating metadata

def hasAnyRating(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.Rating' in f_metadata.exif_keys)):
        # print("this file already has rating data")
        return True
    # print("this file has no rating data")
    return False

def hasRating(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def getRating(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def setRating(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

# ------edit metadata that can store source url

def hasAnySrc(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.ImageHistory' in f_metadata.exif_keys)):
        # print("this file already has history/source data")
        return True
    # print("this file has no history/source data")
    return False

def hasSrc(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def getSrc(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def addSrc(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

# -------edit orginal date

def hasAnyOrgDate(p_filename):
    f_metadata = pyexiv2.ImageMetadata(p_filename)
    f_metadata.read()
    #TODO add png support
    if ((p_filename[-4:] == '.jpg') and ('Exif.Image.DateTimeOriginal' in f_metadata.exif_keys)):
        # print("this file already has original date data")
        return True
    # print("this file has no original date data")
    return False

def hasOrgDate(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def getOrgDate(p_filename):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return

def setOrgDate(p_filename, x):
    if len(p_filename) < 5:
        raise Exception('Filename \'{}\' is too short to have any accepted filename extension'.format(p_filename))
    if p_filename[-4:] != '.jpg' and p_filename[-4:] != '.png':
        raise Exception(
            'Filename \'{}\' is not a supported filetype.\n Supported filetypes: jpg, png'.format(p_filename))
    # TODO
    return
