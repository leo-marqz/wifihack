import subprocess
from typing import List
from wifi_profile import WifiProfile

def get_wifi_profiles()->List[WifiProfile]:
    profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    profile_names:list = []
    wifi_profiles = [WifiProfile]
    for profile in profiles:
        if 'All User Profile' in profile:
            profile = profile.split(':')
            profile_names.append(profile[1].strip())

    for profile_name in profile_names:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('ISO-8859-1').split('\n') 
        passwords = [line.split(':')[1].strip() for line in result if 'Key Content' in line]
        for password in passwords:
            wp = WifiProfile(profile_name, password)
            wifi_profiles.append(wp)

    return wifi_profiles        

if __name__ == '__main__':
    wifi_profiles = get_wifi_profiles()
    for wp in wifi_profiles:
        print(wp)