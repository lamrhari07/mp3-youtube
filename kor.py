import re, urllib.request, urllib.parse, webbrowser


open_Url = urllib.request.urlopen
down_url = urllib.request.urlretrieve
data_url = urllib.parse.urlencode



url_input = input("Enter your URL of youtube vedio HERE: ")
    


class openSong:
    def __init__(self, open_Url, down_url, data_url, url_input ): 
        self.open_Url = open_Url
        self.down_url = down_url
        self.data_url = data_url
        self.url_input = url_input
 
        
    def v_title(self):
        try:
            webpage = urllib.request.urlopen(url_input).read()
            title = str(webpage).split('<title>')[1].split('</title>')[0]

        except:
            webpage = urllib.request.urlopen(url_input).read()
            title = str(webpage).split('<title>')[1].split('</title>')[0].decode("uft-8")
    
        return title
    
    def valid(self):
        global url_input 
        if "youtube.com/" not in url_input:
            # try to get the search result and exit upon error
            try:
                query_string = data_url({"search_query" : url_input})
                html_content = open_Url("http://www.youtube.com/watch?v=" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                print("search_results")
                
            except:
                print('Network Error')
                return None
            downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
        
        else:      # For a link
            downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video='+ url_input
            song = openSong.v_title(url_input)
            try:
                print('Downloading %s' % song)
                # code a progress bar for visuals? this way is more portable than wget
                down_url(downloadLinkOnly, filename='%s.mp3' % song)
                urllib.request.urlcleanup()  # clear the cache created by urlretrieve
            except:
                print('Error downloading %s' % song)
                return None
    def Open_brow(self):  
        webbrowser.open("%s" % url_input)
   
def main():
    t = openSong(open_Url, down_url, data_url, url_input) #, kw_input, split_url )
    t.v_title()
    t.valid()
    t.Open_brow()
if __name__ == "__main__":
    main()
