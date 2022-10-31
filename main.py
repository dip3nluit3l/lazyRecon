#!/usr/bin/env python3
import webbrowser
import pyfiglet
import keyboard
import json
import sys
text = pyfiglet.figlet_format("LazyHunter")
TARGET = sys.argv[1]
CONTROL = sys.argv[2]
with open("data.json", "r") as file:
    jsonData = json.load(file)
    print(jsonData)
virustotal = jsonData['url'][0]["Virustotal"]
webbrowser.open_new_tab(virustotal + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

cert = jsonData['url'][0]["CRT"]
webbrowser.open_new_tab(cert + TARGET)
print("Press ", CONTROL,  " Key to Continue")
keyboard.wait('CONTROL')

pld1 = jsonData['url'][0]["pld"]
webbrowser.open_new_tab(pld1 + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

host1 = jsonData['url'][0]["host"]
webbrowser.open_new_tab(host1 + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

table1 = jsonData['url'][0]["table"]
webbrowser.open_new_tab(table1 + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

securitytrails = jsonData['url'][0]["securityTrails"]
webbrowser.open_new_tab(securitytrails + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

certsploitter = jsonData['url'][0]["certSplottter"]
webbrowser.open_new_tab(certsploitter + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

portscan = jsonData['url'][0]["portScan"]
webbrowser.open_new_tab(portscan + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

dnsreport = jsonData['url'][0]["dnsReport"]
webbrowser.open_new_tab(dnsreport + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

reversewhois = jsonData['url'][0]["reverseWhoIs"]
webbrowser.open_new_tab(reversewhois + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

whois = jsonData['url'][0]["whoIs"]
webbrowser.open_new_tab(whois + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

dnsanalytics = jsonData['url'][0]["dnsAnalytics"]
webbrowser.open_new_tab(dnsanalytics + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

threatcrowd = jsonData['url'][0]["threatCrowd"]
webbrowser.open_new_tab(threatcrowd + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

securityheaders = jsonData['url'][0]["securityHeaders"]
webbrowser.open_new_tab(securityheaders + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

headers = jsonData['url'][0]["Headers"]
webbrowser.open_new_tab(headers + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

builtwith = jsonData['url'][0]["builtWith"]
webbrowser.open_new_tab(builtwith + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

SSL = jsonData['url'][0]["Ssl"]
webbrowser.open_new_tab(SSL + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

transparancyreport = jsonData['url'][0]["transparancyReport"]
webbrowser.open_new_tab(transparancyreport + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

netcraft = jsonData['url'][0]["netCraft"]
webbrowser.open_new_tab(netcraft + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

securinet = jsonData['url'][0]["securiNet"]
webbrowser.open_new_tab(securinet + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

upguard = jsonData['url'][0]["upGuard"]
webbrowser.open_new_tab(upguard + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

Observatory = jsonData['url'][0]["observatory"]
webbrowser.open_new_tab(Observatory + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

acceessefy = jsonData['url'][0]["Accessefy"]
webbrowser.open_new_tab(acceessefy + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

waybackmachine = jsonData['url'][0]["wayBackMachine"]
webbrowser.open_new_tab(waybackmachine + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

zoomeye = jsonData['url'][0]["zoomEye"]
webbrowser.open_new_tab(zoomeye + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

shodann = jsonData['url'][0]["shodan"]
webbrowser.open_new_tab(shodann + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

censys = jsonData['url'][0]["centSYS"]
webbrowser.open_new_tab(censys + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

docsbyext = jsonData['url'][0]["documentByExtension"]
webbrowser.open_new_tab(docsbyext + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

apachestruds = jsonData['url'][0]["apacheStruds"]
webbrowser.open_new_tab(apachestruds + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

findinpastebin = jsonData['url'][0]["findInPastebin"]
webbrowser.open_new_tab(findinpastebin + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

employeeinlinkedin = jsonData['url'][0]["employeeInLinkedin"]
webbrowser.open_new_tab(employeeinlinkedin + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

loginpages = jsonData['url'][0]["loginPages"]
webbrowser.open_new_tab(loginpages + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

searchforbackdoors = jsonData['url'][0]["searchForBackdoors"]
webbrowser.open_new_tab(searchforbackdoors + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

setupinstalledfiles = jsonData['url'][0]["setupOrInstalledFiles"]
webbrowser.open_new_tab(setupinstalledfiles + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

wpplugins = jsonData['url'][0]["WpPluginDownloadUploads"]
webbrowser.open_new_tab(wpplugins + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

openredir = jsonData['url'][0]["openRedirects"]
webbrowser.open_new_tab(openredir + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

githubdorks = jsonData['url'][0]["githubDorks"]
webbrowser.open_new_tab(githubdorks + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

npmauthreg = jsonData['url'][0]["npmAuthRegistery"]
webbrowser.open_new_tab(npmauthreg + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

dorkregauthdata = jsonData['url'][0]["dorkRegistaryAuthData"]
webbrowser.open_new_tab(dorkregauthdata + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

privatekeys = jsonData['url'][0]["privateKeys"]
webbrowser.open_new_tab(privatekeys + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

puttygen = jsonData['url'][0]["puttyGenPrivateKeys"]
webbrowser.open_new_tab(puttygen + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

sshkeys = jsonData['url'][0]["sshKeysDSA"]
webbrowser.open_new_tab(sshkeys + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

sshkeys2 = jsonData['url'][0]["sshKeysRSA"]
webbrowser.open_new_tab(sshkeys2 + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

mysqldum = jsonData['url'][0]["mySQLDump"]
webbrowser.open_new_tab(mysqldum + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

mysqldumppasswd = jsonData['url'][0]["mySQLDumpPasswd"]
webbrowser.open_new_tab(mysqldumppasswd + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

htpasswd = jsonData['url'][0]["htPasswd"]
webbrowser.open_new_tab(htpasswd + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

herukuAPIshell = jsonData['url'][0]["herukuAPIKeysSHELL"]
webbrowser.open_new_tab(herukuAPIshell + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')


heruluAPIjson = jsonData['url'][0]["herukuAPIKeysJSON"]
webbrowser.open_new_tab(heruluAPIjson + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')


bashhistory = jsonData['url'][0]["bashHistory"]
webbrowser.open_new_tab(bashhistory + TARGET)
print("Press ", CONTROL, " Key to Continue")
keyboard.wait('CONTROL')

historyfile = jsonData['url'][0]["historyFile"]
webbrowser.open_new_tab(historyfile + TARGET)
print("Press ", CONTROL, ", Key to Continue")
keyboard.wait('CONTROL')
