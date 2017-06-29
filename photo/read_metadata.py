# -*-coding: utf-8 -*-
# just a sample for using python-pyexiv2 Library
# pyexiv2 is a Python binding to exiv2,
#        the C++ library for manipulation of EXIF, IPTC and XMP image metadata.
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import pyexiv2
import os

path = '/Users/zch/Z_HF/恒丰资料/HR'
for file in os.listdir(path):
    print 'file:' + os.path.join(path, file)
    if os.path.splitext(file)[1].upper() in ('.JPEG', '.JPG'):
        print '--------------------------------------------------------------'
        metadata = pyexiv2.ImageMetadata(os.path.join(path, file))
        metadata.read()
        try:
            print len(metadata)
            for key in sorted(metadata.keys()):
                print key
                print '%s : %' % (key, metadata[key])
                print metadata[key].value

            print metadata['Exif.Image.DateTime'].value.strftime('%A %d %B %Y, %H:%M:%S')
            print metadata['Exif.Image.ImageDescription'].value
            print metadata['Exif.Image.Software'].value
            print metadata['Exif.Image.ExifTag'].value
            key = 'Exif.Photo.UserComment'
            value = 'A comment.'
            metadata[key] = pyexiv2.ExifTag(key, value)
            # metadata[key] = value    # this a shotcut method as the previous line.
            metadata.write()
            print metadata[key].value
            metadata[key].value = 'A new comment.'
            metadata.write()
            print metadata[key].value
        except Exception, e:
            print e

        print '--------------------------------------------------------------'
    else:
        pass
