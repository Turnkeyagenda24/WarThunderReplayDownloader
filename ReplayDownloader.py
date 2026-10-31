import urllib.request
#download = input("Please paste the location in which you want to download the files to.")
#download_location = download.replace("\\", "/")
partnum = int(input("How many replay parts are there? Enter digit and press enter."))
wrpl1Url = input("Please paste part 1 replay url of the match you want to download. Use right click to paste something. Then press enter.")
for counter in range(partnum):
    if counter < 10:
        url = wrpl1Url.replace("0000", "000" + str(counter))
        filename = "000" + str(counter) + ".wrpl"
    elif 10 <= counter < 100:
        url = wrpl1Url.replace("0000", "00" + str(counter))
        filename = "00" + str(counter) + ".wrpl"
    else:
        url = wrpl1Url.replace("0000", "0" + str(counter))
        filename = "0" + str(counter) + ".wrpl"
        
    print(f"Downloading: {filename}")
    urllib.request.urlretrieve(url, filename)
    
    
