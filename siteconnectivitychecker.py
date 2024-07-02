import urllib.request as urllib

def check_connectivity(url):
    print("checking connectivity...")
    response=urllib.urlopen(url)
    print(f"connected to {url} successfully")
    print("the response code is " + response.getcode())

print("This is a site connectivity checker")
i_url=input("Enter the url of the site you want to check: ")
check_connectivity(i_url)