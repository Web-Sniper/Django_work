from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# Create your views here.
def index_view(request):
    return render(request,'index.html')
