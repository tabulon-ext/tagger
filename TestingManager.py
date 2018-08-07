#!/usr/bin/env python3
import os
import wget
import requests
import MetadataManager
import pyexiv2

def download_file_from_google_drive(id, destination):
    """downloads files from google drive.
    Found from https://stackoverflow.com/a/39225272"""
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def getGoogleDrivePicture(p_picID, p_outpath):
    """if __name__ == "__main__":
        file_id = 'TAKE ID FROM SHAREABLE LINK'
        destination = 'DESTINATION FILE ON YOUR DISK'
        download_file_from_google_drive(file_id, destination)"""
    f_downloadURL = 'https://drive.google.com/uc?authuser=0&id=' + picID + '&export=download'
    f_filename = wget.download(f_downloadURL, p_outpath)
    download_file_from_google_drive(p_picID, f_filename)
    return f_filename

googlePictures = {'squirrel': '1ZHDchSv9RMxJmdVeepJvvOtTx4T4am3U', 'cat': "1A1Nxr-1mWfFlk9hTVZtzSPfEt6ZC6uzg", 'boxcat':"1oxAPZSBKKTYjdXYYuwpvbKR5grK0aCZY", "frogyellow":'1xMHPQrNyODWTIXQ-PxgWSPbwj7_tGerv', "frogjump":'1nqFSb-hoc1c0-BlTETs0jQn3bzWeGg3T', "titanmeme":"1kRybASv2UVde5wMitn_j1i4x3LklIh6s"}
pictureTags = {'squirrel': ['squirrel'], 'cat': [], 'boxcat':['cat', 'animals', 'cat in a box'], "frogyellow":['frog'], "frogjump":['frog'], "titanmeme":['show screenshots']}
outpath = '/home/hwynn/Pictures'
picID = googlePictures["boxcat"]

def tagSetTest(p_fileEntry, p_tags, p_ExptTags, f_outpath=outpath):
    f_picID = googlePictures[p_fileEntry]
    f_filename = getGoogleDrivePicture(f_picID, f_outpath)
    MetadataManager.setTags(f_filename, p_tags)
    f_newTags = MetadataManager.getTags(f_filename)
    if(f_newTags!=p_ExptTags):
        print("Test FAILED: The file", f_filename, "doesn't have the tags it should.")
        print("Tags expected:", end="")
        for tag1 in p_ExptTags:
            print("\"", tag1, "\"", sep="", end=" ")
        print("Tags found:", end="")
        for tag2 in f_newTags:
            print("\"", tag2, "\"", sep="", end=" ")
        return False
    return True

filename = getGoogleDrivePicture(picID, outpath)
print(filename)



def useageCheck():
    metadata = pyexiv2.ImageMetadata(filename)
    metadata.read()
    print(metadata.exif_keys)
    keywords = metadata['Exif.Image.XPKeywords']
    f_dirtyTagString = pyexiv2.utils.undefined_to_string(keywords.value)
    print("f_dirtyTagString", f_dirtyTagString)
    f_dirtyTagList = f_dirtyTagString.split(';')
    print("f_dirtyTagList", f_dirtyTagList)
    f_tagString = MetadataManager.stringHexTrim(f_dirtyTagString)
    print("f_tagString", f_tagString)
    f_tags1 = f_tagString.split(';')
    print("f_tags1", f_tags1)
    f_tags2 = [MetadataManager.stringHexTrim(x) for x in f_dirtyTagList]
    print("f_tags2", f_tags2)
    f_newdirtyTagList = [MetadataManager.stringHexify(x) for x in f_tags1]
    print("f_newdirtyTagList", f_newdirtyTagList)
    f_newdirtyTagString= ";\x00".join(f_newdirtyTagList)+"\x00\x00"
    print("f_newdirtyTagString", f_newdirtyTagString)
    print()
    print("f_dirtyTagString", f_dirtyTagString)
    f_cleanTagList = MetadataManager.dirtyStr2cleanList(f_dirtyTagString)
    print("f_cleanTagList", f_cleanTagList)
    f_dirtyTagString2 = MetadataManager.cleanList2dirtyStr(f_cleanTagList)
    print("f_dirtyTagString2", f_dirtyTagString2)

    return

useageCheck()

os.remove(filename)
