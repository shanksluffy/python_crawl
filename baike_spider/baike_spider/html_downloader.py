'''
Created on 2017-7-23

@author: m11wang
'''
import urllib2


class HtmlDownLoader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    



