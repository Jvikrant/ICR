# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:53:33 2018

@author: jdhruwa
"""
def ExtractText(filepath,inputMethod):
    #print(filepath)
    #API key
    subscription_key = '1888e03e35ed4bbaa1bb1afffdc52ce7'
    assert subscription_key
    
    #input_flag true for url image 
    #false: local input
    input_flag=inputMethod
    
    
    #base url
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    
    text_recognition_url = vision_base_url + "RecognizeText"
    print(text_recognition_url)
    
    #image input url
    #accurate
    if input_flag:
        image_url = filepath
    else:
        image_url= filepath
        image_data=open(image_url, "rb").read()
        
    #inaccurate
    #image_url="http://www.how-ocr-works.com/scanners/hardware2/scanned-form.png"
    
    
    import requests
    
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key}
    
    if not input_flag:
        headers["Content-Type"] = "application/octet-stream"
        
    params   = {'handwriting' : True}
    data     = {'url': image_url}
    
    if input_flag:
        response = requests.post(text_recognition_url, headers=headers, params=params, json=data)
    else:
        response = requests.post(text_recognition_url, headers=headers, params=params, data=image_data)
    
    response.raise_for_status()
    
    operation_url = response.headers["Operation-Location"]
    
    import time
    
    analysis = {}
    while not "recognitionResult" in analysis:
        response_final = requests.get(operation_url, headers=headers)
        analysis       = response_final.json()
        time.sleep(1)
        
    #Getting result
    polygons = [(line["boundingBox"], line["text"]) for line in analysis["recognitionResult"]["lines"]]
    
    from Mandrin import plot_image
    return plot_image(polygons)
