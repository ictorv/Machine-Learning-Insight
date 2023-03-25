from collections import Iterable 
import numpy as np
import time
import cv2
import csv

def flatten(lis):
    for itm in lis:
        if isinstance(itm,Iterable) and not isinstance(itm, str):
            for x in flatten(itm):
                yield x
        else:
            yield itm

embeddingFile="output/embeddings.pickle"
embeddingModel="openface_nn4.small2.v1.t7"
recognizerFile="output/recognizer.pickle"
labelEncFile="output/le.pickle"
conf=0.5

print("[INFO]")