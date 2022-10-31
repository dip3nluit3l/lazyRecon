#!/usr/bin/env python3
import webbrowser
import pyfiglet
import keyboard
import json
import sys,getopt
text = pyfiglet.figlet_format("LazyHunter")
TARGET = sys.argv[1]

with open("data.json", "r") as file:
    jsonData = json.load(file)
    print(jsonData)
virustotal = jsonData['url'][0]["Virustotal"]
webbrowser.open_new_tab(virustotal + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

cert = jsonData['url'][0]["CRT"]
webbrowser.open_new_tab(cert + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

pld1 = jsonData['url'][0]["pld"]
webbrowser.open_new_tab(pld1 + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

host1 = jsonData['url'][0]["host"]
webbrowser.open_new_tab(host1 + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

table1 = jsonData['url'][0]["table"]
webbrowser.open_new_tab(table1 + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

#dnsTable = jsonData['url'][0]["DNSTable"]
#webbrowser.open_new_tab(dnsTable + TARGET)
#print("Press enter Key to Continue")
#keyboard.wait('enter')

securitytrails = jsonData['url'][0]["securityTrails"]
webbrowser.open_new_tab(securitytrails + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

certsploitter = jsonData['url'][0]["certSplottter"]
webbrowser.open_new_tab(certsploitter + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

portscan = jsonData['url'][0]["portScan"]
webbrowser.open_new_tab(portscan + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

dnsreport = jsonData['url'][0]["dnsReport"]
webbrowser.open_new_tab(dnsreport + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

reversewhois = jsonData['url'][0]["reverseWhoIs"]
webbrowser.open_new_tab(reversewhois + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

whois = jsonData['url'][0]["whoIs"]
webbrowser.open_new_tab(whois + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

dnsanalytics = jsonData['url'][0]["dnsAnalytics"]
webbrowser.open_new_tab(dnsanalytics + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

threatcrowd = jsonData['url'][0]["threatCrowd"]
webbrowser.open_new_tab(threatcrowd + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

securityheaders = jsonData['url'][0]["securityHeaders"]
webbrowser.open_new_tab(securityheaders + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

headers = jsonData['url'][0]["Headers"]
webbrowser.open_new_tab(headers + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

builtwith = jsonData['url'][0]["builtWith"]
webbrowser.open_new_tab(builtwith + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

SSL = jsonData['url'][0]["Ssl"]
webbrowser.open_new_tab(SSL + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

#certdb = jsonData['url'][0]["certDB"]
#webbrowser.open_new_tab(certdb + TARGET)
#print("Press enter Key to Continue")
#keyboard.wait('enter')

transparancyreport = jsonData['url'][0]["transparancyReport"]
webbrowser.open_new_tab(transparancyreport + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

netcraft = jsonData['url'][0]["netCraft"]
webbrowser.open_new_tab(netcraft + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

securinet = jsonData['url'][0]["securiNet"]
webbrowser.open_new_tab(securinet + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

upguard = jsonData['url'][0]["upGuard"]
webbrowser.open_new_tab(upguard + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

Observatory = jsonData['url'][0]["observatory"]
webbrowser.open_new_tab(Observatory + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

acceessefy = jsonData['url'][0]["Accessefy"]
webbrowser.open_new_tab(acceessefy + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

waybackmachine = jsonData['url'][0]["wayBackMachine"]
webbrowser.open_new_tab(waybackmachine + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

#Fofa = jsonData['url'][0]["fofa"]
#webbrowser.open_new_tab(Fofa + TARGET)
#print("Press enter Key to Continue")
#keyboard.wait('enter')

zoomeye = jsonData['url'][0]["zoomEye"]
webbrowser.open_new_tab(zoomeye + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

shodann = jsonData['url'][0]["shodan"]
webbrowser.open_new_tab(shodann + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

censys = jsonData['url'][0]["centSYS"]
webbrowser.open_new_tab(censys + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

docsbyext = jsonData['url'][0]["documentByExtension"]
webbrowser.open_new_tab(docsbyext + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

apachestruds = jsonData['url'][0]["apacheStruds"]
webbrowser.open_new_tab(apachestruds + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

findinpastebin = jsonData['url'][0]["findInPastebin"]
webbrowser.open_new_tab(findinpastebin + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

employeeinlinkedin = jsonData['url'][0]["employeeInLinkedin"]
webbrowser.open_new_tab(employeeinlinkedin + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

loginpages = jsonData['url'][0]["loginPages"]
webbrowser.open_new_tab(loginpages + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

searchforbackdoors = jsonData['url'][0]["searchForBackdoors"]
webbrowser.open_new_tab(searchforbackdoors + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

setupinstalledfiles = jsonData['url'][0]["setupOrInstalledFiles"]
webbrowser.open_new_tab(setupinstalledfiles + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

wpplugins = jsonData['url'][0]["WpPluginDownloadUploads"]
webbrowser.open_new_tab(wpplugins + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

openredir = jsonData['url'][0]["openRedirects"]
webbrowser.open_new_tab(openredir + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

githubdorks = jsonData['url'][0]["githubDorks"]
webbrowser.open_new_tab(githubdorks + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

npmauthreg = jsonData['url'][0]["npmAuthRegistery"]
webbrowser.open_new_tab(npmauthreg + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

dorkregauthdata = jsonData['url'][0]["dorkRegistaryAuthData"]
webbrowser.open_new_tab(dorkregauthdata + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

privatekeys = jsonData['url'][0]["privateKeys"]
webbrowser.open_new_tab(privatekeys + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

puttygen = jsonData['url'][0]["puttyGenPrivateKeys"]
webbrowser.open_new_tab(puttygen + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

sshkeys = jsonData['url'][0]["sshKeysDSA"]
webbrowser.open_new_tab(sshkeys + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

sshkeys2 = jsonData['url'][0]["sshKeysRSA"]
webbrowser.open_new_tab(sshkeys2 + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

mysqldum = jsonData['url'][0]["mySQLDump"]
webbrowser.open_new_tab(mysqldum + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

mysqldumppasswd = jsonData['url'][0]["mySQLDumpPasswd"]
webbrowser.open_new_tab(mysqldumppasswd + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

htpasswd = jsonData['url'][0]["htPasswd"]
webbrowser.open_new_tab(htpasswd + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')

herukuAPIshell = jsonData['url'][0]["herukuAPIKeysSHELL"]
webbrowser.open_new_tab(herukuAPIshell + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')


heruluAPIjson = jsonData['url'][0]["herukuAPIKeysJSON"]
webbrowser.open_new_tab(heruluAPIjson + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')


bashhistory = jsonData['url'][0]["bashHistory"]
webbrowser.open_new_tab(bashhistory + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')


historyfile = jsonData['url'][0]["historyFile"]
webbrowser.open_new_tab(historyfile + TARGET)
print("Press enter Key to Continue")
keyboard.wait('enter')
