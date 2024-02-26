import requests 

url = 'http://facebook.com/'  
## η λύση μου
with requests.get(url) as response:  
    print(f"Website headers are {url} \n, {response.headers} \n\n")
    server = response.headers.get("Server")
    
    if server:
        print(f"The server is {server}")
        
    else:
        print("No server found")
        
    cookies = response.headers.get('Set-Cookie')
    
    if cookies:
        cookies = cookies.split(',')
        for cookie in cookies:   
            print(f"The cookie is {cookie}")
    else:
        print("No cookie found")
    