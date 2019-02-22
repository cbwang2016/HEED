#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: captcha/__init__.py

import os
from PIL import Image
from .preprocess import ImageProcessor

try:
    from .classifier import KNN, SVM, RandomForest
except ModuleNotFoundError:
    loaded=False
else:
    loaded=True

__all__ = ["CaptchaRecognizer",]


class CaptchaRecognitionResult:

    def __init__(self, code, segs, spans):
        self.code = code
        self.segs = tuple(segs)
        self.spans = tuple(spans)

    def __repr__(self):
        return '<%s: %r>' % (
                self.__class__.__name__,
                self.code,
            )

    def __eq__(self, other):
        return self.code == other

if loaded:

    class CaptchaRecognizer(object):

        Classifier = SVM

        def __init__(self):
            self.clf = self.__class__.Classifier()

        def recognize(self, img):
            img = img.convert("1")

            img = ImageProcessor.denoise8(img, repeat=1)
            img = ImageProcessor.denoise24(img, repeat=1)

            segs, spans = ImageProcessor.crop(img)

            Xlist = [self.clf.feature(segImg) for segImg in segs]
            chars = self.clf.predict(Xlist)
            captcha = "".join(chars)

            return CaptchaRecognitionResult(captcha, segs, spans)

else:

    class CaptchaRecognizer:
        pass