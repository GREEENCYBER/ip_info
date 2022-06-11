try:
    from desighn import banner as baner
except:
    print("here is not desighn file")
try:
    import ipapi
except:
    print("please install ip api")
try:
    import os
except:
    print("please install os")
try:
    from time import sleep as sleep
except:
    print("please install time")
while(True):
    
        os.system("cls" or "clear");baner()
        Target = input("Enter Your Target IP: ")
        os.system("cls" or "clear");baner()
        sleep(2)
        info = ipapi.location(f"{Target}")
        print("Ip: "+Target)
        sleep(2)
        print("city: "+info["city"])
        sleep(2)
        print("region: "+info["region"])
        sleep(2)
        print("region code: "+info["region_code"])
        sleep(2)
        print("country: "+info["country"])
        sleep(2)
        print("country name: "+info["country_name"])
        sleep(2)
        print("country_code: "+info["country_code"])
        sleep(2)
        print("org: "+info["org"])
        sleep(2)
        print("languages: "+info["languages"])
        sleep(2)
        print("timezone: "+info["timezone"])
        sleep(2)
        print("county code number: "+info["country_calling_code"])
        sleep(5)
        print("Done!!!")
    
