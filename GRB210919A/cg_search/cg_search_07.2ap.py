#!/usr/bin/python3

import sys,os,re
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

#import xlrd

###################
#### must be setted

database='.'
olist=''
s_head='856'
imname='b.asc'
dbname="a.csv"

def cal_upper_lim2():
	df = pd.read_csv('GaiaCatalog0.ASC',skiprows=11,sep='\\s+',header=None)
	head = ['NUMBER','X_IMAGE','Y_IMAGE','MAG_APER','MAGERR_APER','ISOAREA_IMAGE','ALPHA_J2000','DELTA_J2000','THETA_IMAGE','ELONGATION','ELLIPTICITY']
	df.columns = head
	cen_x = (np.min(df['X_IMAGE'])+np.max(df['X_IMAGE']))/2.0
	cen_y = (np.min(df['Y_IMAGE'])+np.max(df['Y_IMAGE']))/2.0
	fit_list = df[(df['MAGERR_APER']>0.05) & (df['MAGERR_APER']<0.5) & (df['ELLIPTICITY']<0.3) &
				  ((df['X_IMAGE']-cen_x)**2+(df['Y_IMAGE']-cen_y)**2 < (0.9*min(cen_x,cen_y))**2)]
	print('##########','Fitting point number of upper limit:',len(fit_list),'##########')
	popt, pcov = curve_fit(lim_func, fit_list['MAGERR_APER'], fit_list['MAG_APER'])
	maggg_lim3 = popt[0] * np.log10(1.0875/3) + popt[1]
	maggg_lim5 = popt[0] * np.log10(1.0875/5) + popt[1]
	x = np.linspace(1e-4,0.5,10000)
	#plt.semilogx()
	plt.plot(x,lim_func(x,popt[0],popt[1]), color='green', label='fit')
	plt.scatter(fit_list['MAGERR_APER'],fit_list['MAG_APER'],marker='.',color='r',label='data')
	plt.vlines(1.0875/3,min(fit_list['MAG_APER'])-0.3,lim_func(0.4,popt[0],popt[1]),linestyles='-.',label='3 sigma')
	plt.vlines(1.0875/5,min(fit_list['MAG_APER'])-0.3,lim_func(0.4,popt[0],popt[1]),color='orange',linestyles='-.',label='5 sigma')
	plt.legend(loc='best')
	plt.xlim(0.01,0.4)
	plt.ylim(min(fit_list['MAG_APER'])-0.3,lim_func(0.4,popt[0],popt[1]))
	plt.gca().invert_yaxis()
	plt.savefig('upper_lim.png',dpi=300)
	#plt.show()
	plt.close()
	mag_lim =[maggg_lim3,maggg_lim5]
	return mag_lim

def lim_func(x,a,b):
	y = a * np.log10(x) + b
	return y

#############################
#######  set

#head ['objName', 'objAltName1', 'objAltName2', 'objAltName3', 'objID', 'uniquePspsOBid', 'ippObjID', 'surveyID', 'htmID', 'zoneID', 'tessID', 'projectionID', 'skyCellID', 'randomID', 'batchID', 'dvoRegionID', 'processingVersion', 'objInfoFlag', 'qualityFlag', 'raStack', 'decStack', 'raStackErr', 'decStackErr', 'raMean', 'decMean', 'raMeanErr', 'decMeanErr', 'epochMean', 'posMeanChisq', 'cx', 'cy', 'cz', 'lambda', 'beta', 'l', 'b', 'nStackObjectRows', 'nStackDetections', 'nDetections', 'ng', 'nr', 'ni', 'nz', 'ny', 'gQfPerfect', 'gMeanPSFMag', 'gMeanPSFMagErr', 'gMeanPSFMagStd', 'gMeanPSFMagNpt', 'gMeanPSFMagMin', 'gMeanPSFMagMax', 'gMeanKronMag', 'gMeanKronMagErr', 'gMeanKronMagStd', 'gMeanKronMagNpt', 'gMeanApMag', 'gMeanApMagErr', 'gMeanApMagStd', 'gMeanApMagNpt', 'gFlags', 'rQfPerfect', 'rMeanPSFMag', 'rMeanPSFMagErr', 'rMeanPSFMagStd', 'rMeanPSFMagNpt', 'rMeanPSFMagMin', 'rMeanPSFMagMax', 'rMeanKronMag', 'rMeanKronMagErr', 'rMeanKronMagStd', 'rMeanKronMagNpt', 'rMeanApMag', 'rMeanApMagErr', 'rMeanApMagStd', 'rMeanApMagNpt', 'rFlags', 'iQfPerfect', 'iMeanPSFMag', 'iMeanPSFMagErr', 'iMeanPSFMagStd', 'iMeanPSFMagNpt', 'iMeanPSFMagMin', 'iMeanPSFMagMax', 'iMeanKronMag', 'iMeanKronMagErr', 'iMeanKronMagStd', 'iMeanKronMagNpt', 'iMeanApMag', 'iMeanApMagErr', 'iMeanApMagStd', 'iMeanApMagNpt', 'iFlags', 'zQfPerfect', 'zMeanPSFMag', 'zMeanPSFMagErr', 'zMeanPSFMagStd', 'zMeanPSFMagNpt', 'zMeanPSFMagMin', 'zMeanPSFMagMax', 'zMeanKronMag', 'zMeanKronMagErr', 'zMeanKronMagStd', 'zMeanKronMagNpt', 'zMeanApMag', 'zMeanApMagErr', 'zMeanApMagStd', 'zMeanApMagNpt', 'zFlags', 'yQfPerfect', 'yMeanPSFMag', 'yMeanPSFMagErr', 'yMeanPSFMagStd', 'yMeanPSFMagNpt', 'yMeanPSFMagMin', 'yMeanPSFMagMax', 'yMeanKronMag', 'yMeanKronMagErr', 'yMeanKronMagStd', 'yMeanKronMagNpt', 'yMeanApMag', 'yMeanApMagErr', 'yMeanApMagStd', 'yMeanApMagNpt', 'yFlags', 'distance']

######
ra='raMean' #23
dec='decMean' #24
ra_err='raMeanErr' # 25
dec_err='decMeanErr' # 26
gm='gMeanApMag' # 45
gm_err='gMeanApMagErr' #46
rm='rMeanApMag' #61
rm_err='rMeanApMagErr'#62
im='iMeanApMag' #77
im_err='iMeanApMagErr' #78
zm='zMeanApMag' #93
zm_err='zMeanApMagErr' #94
ym='yMeanApMag' #99
ym_err='yMeanApMagErr' #100
Rm='Rm'
Rm_err='Rm_err'
Im='Im'
Im_err='Im_err'


mm=Rm
mm_err=Rm_err
#global my_head
#my_head=[ra,dec,mm,mm_err]
rmag=[15,23]
rmag_err=0.1


#####
# R=r-0.2936*(r-i)-0.1439 sigma=0.0072

#######################################3333

def rdb(dbname):
	#print(my_head)
	global db_head
	db=open(dbname)
	db_p=db.tell()
	#db.seek(0,0)
	db_data= csv.reader(db)
	result=[]
	db_head=re.split('[,|\n]',db.readline())
	#print(db.readline())
	headlist=[]
	dblen=0
	try :
		global my_head
	except SyntaxWarning:
		pass
	if mm == 'Rm':
		my_head=[ra,dec,rm,rm_err,im,im_err]
		for i in my_head :
			headlist.append(db_head.index(i))
		#print(db_head)
		print(my_head,'\n',headlist)
		headlog=0
		for once in db_data:
			dblen=dblen+1
			headlog=headlog+1
			#print(once)
			if rmag[0] < float(once[headlist[2]]) < rmag[1] :
				if 0 < float(once[headlist[3]]) < rmag_err :
					if float(once[headlist[4]]) > 0:
						r_once=float(once[headlist[2]])
						i_once=float(once[headlist[4]])
						R_once=r_once-0.2936*(r_once-i_once)-0.1439
						R_err=float(once[headlist[3]])
						one=[float(headlog),float(once[headlist[0]]),float(once[headlist[1]]),R_once,R_err]
					else:
						continue
						one=[float(headlog)]
						for j in headlist[0:4]:
							one.append(float(once[int(j)]))
						one[2]=one[2]-0.2
					result.append(one)
	elif mm == 'Im':
		my_head=[ra,dec,im,im_err,rm,rm_err]
		for i in my_head :
			headlist.append(db_head.index(i))
		#print(db_head)
		print(my_head,'\n',headlist)
		headlog=0
		for once in db_data:
			dblen=dblen+1
			headlog=headlog+1
			#print(once)
			if rmag[0] < float(once[headlist[2]]) < rmag[1] :
				if 0 < float(once[headlist[3]]) < rmag_err :
					if  float(once[headlist[4]]) > 0  :
						i_once=float(once[headlist[2]])
						r_once=float(once[headlist[4]])
						I_once=r_once-1.2444*(r_once-i_once)-0.3820
						I_err=float(once[headlist[3]])
						one=[float(headlog),float(once[headlist[0]]),float(once[headlist[1]]),I_once,I_err]
					else:
						continue
						one=[float(headlog)]
						for j in headlist[0:4]:
							one.append(float(once[int(j)]))
						one[2]=one[2]-0.45
					result.append(one)
	else:
		my_head=[ra,dec,mm,mm_err]
		for i in my_head :
			headlist.append(db_head.index(i))
		#print(db_head)
		print(my_head,'\n',headlist)
		headlog=1
		for once in db_data:
			dblen=dblen+1
			#print(once)
			if rmag[0] < float(once[headlist[2]]) < rmag[1] :
				if 0 < float(once[headlist[3]]) < rmag_err :
					one=[float(headlog)]
					for j in headlist:
						one.append(float(once[int(j)]))
					#print(one)
					result.append(one)
			headlog=headlog+1
	db.close()
	print('db : ',len(result),' / ',dblen)
	return np.array(result)



##################
#test
#aa=rdb('a.csv')
#exit()

######################



#######################################
#############################
#######  set


#mykey=['ALPHA_J2000','DELTA_J2000','MAG_AUTO','MAGERR_AUTO','MAG_BEST','MAGERR_BEST','ELLIPTICITY']
#mykey=['ALPHA_J2000','DELTA_J2000','MAG_APER','MAGERR_APER','MAG_AUTO','MAGERR_AUTO']
mykey=['ALPHA_J2000','DELTA_J2000','MAG_APER','MAGERR_APER']

mytuo=0.3

ymag_err=0.1

########################################

def rim(imname):
	print(mykey,'\n\n\n\tELLIPTICITY must be the last one.')
	global im_s
	im=open(imname)
	result=[]
	aa=im.readlines()
	isum=0
	headhead={}
	#headlist=[]
	limitlist=[]
	for i in aa:
		once=i.split()
		#print(once)
		if  i[0] == '#' :
			for ii in mykey :
				if ii in i:
					iihead={ii:isum}
					headhead.update(iihead)
					#print(ii ,i)
		elif once == [] :
			continue
		elif  once[0] ==  s_head :
			im_s=[]
			for ii in range(len(mykey)):
				im_s.append(float(once[headhead[mykey[ii]]]))
			im_s.append(once[-1])
		else:
			one=[]
			#print('##################')
			if float(once[-1]) < mytuo :
				for ii in range(len(mykey)):
					#headlist=headhead[mykey[ii]]
					#print(once[headlist])
					one.append(float(once[headhead[mykey[ii]]]))
				#once.append(list(map(float,i.split())))
				#print(ymag_err,one[1])
				if  float(one[3]) < ymag_err :
					#print(one)
					result.append(one)
				elif ( 0.2 < float(one[3]) < 0.4 ):
					limitlist.append(float(one[2]))
		isum=isum+1
	im.close()
	print('\n',im_s,'\nim :',len(result))
	return np.array(result),np.array(limitlist)


#########
#test
#bb=rim('b.asc')


#############################################



##########################
####  set
lim=15


#############

def match(im_data,db_data):
	print('im_data has lines:',len(im_data[0]),'\ndb_data has lines:',len(db_data[0]))
	result=[]
	log=open(s_head+'_'+mm+'_log.txt','w')
	log.write('\t\tmatch\n\n\n')
	for i in im_data:
		ra_err=math.cos(i[1]/180.*math.pi)*3600*(db_data[:,1]-i[0])
		dec_err=3600*(db_data[:,2]-i[1])
		#ra_err=1000*(db_data[:,1]-i[0])
		#dec_err=1000*(db_data[:,2]-i[1])
		#print(ra_err,'   ',dec_err)
		sum_err=np.square(ra_err)+np.square(dec_err)
		#print(min(sum_err))
		sum_err=list(sum_err)
		if min(sum_err) < 10:
			log.write(str(i[:])+'\n')
			log.write(str(db_data[sum_err.index(min(sum_err))][1:])+str(db_data[sum_err.index(min(sum_err))][0])+'\n\n\n')
			#print(min(sum_err))
			#db_data[sum_err.index(min(sum_err))]
			result.append([list(i[:]),list(db_data[sum_err.index(min(sum_err))][:])])
	#print(result)
	print('match ',str(len(result)))
	log.close()
	return result



##############################


#######


def limit(limitlist):
	limit_lost=int(len(limitlist)**0.5)
	limit_num=np.median(limitlist[limit_lost:-limit_lost])
	return limit_num







############

def line_fit(x,y):
	m_x=np.mean(x)
	m_y=np.mean(y)
	l=range(len(x))
	s_x=0
	s_y=0
	for i in l:
		s_x=s_x+(x[i]-m_x)*y[i]
		s_y=s_y+(x[i]-m_x)**2
	k=s_x/s_y
	b=m_y-k*m_x
	#print(k,b)
	print('y='+str(k)+' * x+'+str(b))
	return k,b



#################################

#############


def fit2(mymagdb,plotname):
	x=[]
	y=[]
	for i in mymagdb:
		x.append(i[0][2:])
		y.append(i[1][3:])
	#x=np.array(x)
	#y=np.array(y)
	#print(y)
	mag_sum=x_x+np.array(y)[:,0]-np.array(x)[:,0]
	#print(mag_sum)
	print(np.mean(mag_sum))
	#x_del=list(x)
	#y_del=list(y)
	mymagdb_del=list(mymagdb)
	mag_del=list(mag_sum)
	#lost=int(len(mag_del)**0.5)
	for i in range(len(mag_sum)):
		#print(i)
		if len(mag_del) <= lim:
			break
		else :
			pass
		mag_mean=np.mean(mag_del)
		mag_max=np.square(mag_del-mag_mean)
		imax=list(mag_max).index(max(mag_max))
		#print(mag_del[imax],x_del[imax],y_del[imax])
		mag_del.remove(mag_del[imax])
		mymagdb_del.remove(mymagdb_del[imax])
		#x_del.remove(x_del[imax])
		#y_del.remove(y_del[imax])
	mean_mag_best=np.mean(mag_del)
	print(mean_mag_best)
	x_del=[]
	y_del=[]
	for i in mymagdb_del:
		#print(i)
		x_del.append(i[0][2:])
		y_del.append(i[1][3:])
	[k,b,y_err]=y_rplot(np.array(x_del),np.array(y_del),[x_x,mean_mag_best,float(err_err)],plotname)
	#############################
	db=open(dbname)
	csvdb=open(s_head+'_my.csv','w')
	wdb=csv.writer(csvdb)
	db_p=db.tell()
	#db.seek(0,0)
	db_data= csv.reader(db)
	#result=[]
	db_head=re.split('[,|\n]',db.readline())
	wdb.writerow(db_head)
	headlist=[]
	poplist=[]
	for i in np.array(mymagdb_del)[:,1]:
		poplist.append(i[0])
	poplist=sorted(poplist,reverse = True)
	headlog=1
	for i in db_data:
		#print(headlog,poplist[-1])
		if headlog == poplist[-1] :
			#print(i[23])
			#print(mymagdb_del[25-len(poplist)])
			wdb.writerow(i)
			poplist.pop()
			if poplist == [] :
				break
		else:
			pass
		headlog=headlog+1
	csvdb.close()
	db.close()
	#################################
	#with open(s_head+'_my.csv','w') as csvdb:
	#	db=csv.writer(csvdb)
	#	db.writerow(my_head)
	#	db.writerows(np.array(mymagdb_del)[:,1])
	limit_num=limit(limitlist)
	mag_limit=k*limit_num+b
	print(str(k*x_x+b))
	print('The uplimit (3) is : '+str(mag_limit)+'  all:'+str(len(limitlist)))
	log=open(s_head+'_'+mm+'_log.txt','a')
	log.write('\n\n######line fit \n')
	log.write('y='+str(k)+' * x+'+str(b)+'\n')
	log.write(str(k*x_x+b))
	log.write('\n\n#######################\n\n')
	log.write(' head    ra     dec    mag_err\n')
	log.write(str(s_head)+'  '+str(im_s[0])+'  '+str(im_s[1])+'  '+str(im_s[3])+'\n\n')
	log.write('The cured magnitude about GRB is '+str(np.mean(mag_del))+' +/- '+str(y_err)+'  .\n\n')
	log.write('The uplimit (3) is : '+str(mag_limit)+'  all:'+str(len(limitlist)))
	log.close()
	return np.mean(mag_del),mag_limit,y_err,k,b


#################################
#or_mag2,y_err=fit2(mymagdb,mm)


########### plot

def y_rplot(x,y,y_r,plotname):
	import matplotlib.pyplot as plt
	#print(x[:,0],y[:,0])
	s=np.mean(np.square(y[:,1]))
	#print(s)
	y_err=(y_r[2]**2+s)**0.5
	#print(y_err)
	#s=np.sqrt(s)
	k,b=line_fit(x[:,0],y[:,0])
	x_line=list(x[:,0])
	x_line.append(y_r[0])
	x_line=np.array(x_line)
	#print(x_x,x)
	y_line=k*x_line+b
	fig, ax = plt.subplots()
	ax.set_title('Plot real/ins')
	plt.ylabel('real_mag')
	plt.xlabel('ins_mag')
	plt.errorbar(x[:,0],y[:,0],xerr=x[:,1] ,yerr=y[:,1] ,fmt='.k')
	plt.errorbar(y_r[0],y_r[1],xerr=y_r[2],yerr=y_err)
	plt.plot(x_line,y_line,'-r')
	#plt.show()
	plt.savefig(s_head+'_'+plotname+'.eps')
	plt.close()
	return [k,b,y_err]



########
workpath = os.path.dirname(os.path.abspath(sys.argv[0]))
print (workpath)



######################################################
#####################################################
######################################################
#
#		real worke
#
#

try  :
	inp=open('./cg_search','r')
	aa=inp.readlines()
	for i in aa :
		#i=i.split()[0]
		#print(len(i))
		if len(i) == 1 :
			continue
		elif '#' in i[0] :
			continue
		elif 'WCS_RA' in i:
			WCS_RA=i.split('=')[1].split()[0]
		elif 'WCS_DEC' in i:
			WCS_DEC=i.split('=')[1].split()[0]
		elif 'radius' in i:
			radius=i.split('=')[1].split()[0]
		elif 'imname' in i:
			#print(i.split('='))
			imname=i.split('=')[1].split()[0]
		elif 'dbname' in i:
			dbname=i.split('=')[1].split()[0]
		elif 's_head' in i:
			s_head=i.split('=')[1].split()[0]
		elif 'mm' in i:
			mm=i.split('=')[1].split()[0]
			#print(mm)
			if mm == 'g':
				mm=gm
				mm_err=gm_err
			elif mm == 'r':
				mm=rm
				mm_err=rm_err
			elif mm == 'i':
				mm=im
				mm_err=im_err
			elif mm == 'z':
				mm=zm
				mm_err=zm_err
			elif mm == 'y':
				mm=ym
				mm_err=ym_err
			elif mm == 'R':
				mm=Rm
				mm_err=Rm_err
			elif mm == 'I':
				mm=Im
				mm_err=Im_err
			else:
				print('mm have some error.["g","r","i","z","y","R","I"]')
				exit()
		elif 'rmag=' in i:
			print(i)
			rmag=i.split('=')[1].split()
			rmag=list(map(float,rmag))
			print(rmag)
		elif 'rmag_err' in i:
			rmag_err=float(i.split('=')[1].split()[0])
		elif 'mytuo' in i:
			mytuo=float(i.split('=')[1].split()[0])
		elif 'ymag_err' in i:
			ymag_err=float(i.split('=')[1].split()[0])
		elif 'lim' in i:
			lim=float(i.split('=')[1].split()[0])
		else:
			print('unknow input ,miss them.')
	try :
		open(dbname,'r')
		print('db ready')
	except:
		os.system('wget -nd -nc "https://catalogs.mast.stsci.edu/api/v0.1/panstarrs/dr1/mean?ra='+str(WCS_RA)+'&amp;dec='+str(WCS_DEC)+'&radius='+str(radius)+'&nDetections.gte=1&amp&pagesize=50001&format=csv"')
		os.system('cp ./mean\?ra\='+str(WCS_RA)+'\&amp\;dec\='+str(WCS_DEC)+'\&radius\='+str(radius)+'\&nDetections.gte\=1\&amp\&pagesize\=50001\&format\=csv  ./'+str(dbname))
		print('check your dbdata,it was setted '+str(dbname))
except FileNotFoundError :
	print('cg_search will be write')
	inflie='###### for YU cg_search ###### \n\n\
### center  WCS_RA WCS_DEC of image  (degree) \n\n\
WCS_RA= \n\
WCS_DEC= \n\
### radius (degree,commend <0.12)\n\
radius=0.12 \n\n\
### imname(*.asc) \n\n\
imname=GaiaCatalog0.ASC\n\n\
### dbname(*.csv) \n\n\
dbname= mean\n\n\
### number of souce in *.asc \n\n\
s_head= \n\n\
### mm should be setted [g,r,i,z,y,R,I]  \n\n\
mm= \n\n\
###  range of mag in  star catalogue. \n\n\
rmag=14 23 \n\n\
### max of mag_err in  star catalogue.\n\n\
rmag_err=0.1 \n\n\
###  .....  \n\n\
mytuo=0.3 \n\n\
### max of ymag_err in image. \n\n\
ymag_err=0.1 \n\n\
### How many standard stars will be used  \n\n\
lim=15 '
	filename=open('cg_search','w')
	filename.write(inflie)
	filename.close()
	exit()
#except IndexError:
#	print('check your cg_search , insure each  parameter is ready.' )
#	exit()


#auto=True
auto=False

if auto :
	imname=str(input('imname is :'))
	try :
		imname
	except :
		print('imname should be setted .')
		exit()
	dbname=str(input('dbname is :'))
	try :
		dbname
	except :
		print('dbname should be setted auto.')
		exit()
		#continue
	s_head=str(input('s_head(source number) is :'))
	try :
		s_head
	except :
		print('dbname should be setted .')
		exit()
		#continue
	mm=str(input('input [g,r,i,z,y,R,I] :'))
	try :
		mm
		if mm == 'g':
			mm=gm
			mm_err=gm_err
		elif mm == 'r':
			mm=rm
			mm_err=rm_err
		elif mm == 'i':
			mm=im
			mm_err=im_err
		elif mm == 'z':
			mm=zm
			mm_err=zm_err
		elif mm == 'y':
			mm=ym
			mm_err=ym_err
		elif mm == 'R':
			mm=Rm
			mm_err=Rm_err
		elif mm == 'I':
			mm=Im
			mm_err=Im_err
		else:
			print('mm have some error.["g","r","i","z","y","R","I"]')
			exit()
	except :
		print('mm should be setted ["g","r","i","z","y","R","I"].')
		exit()
		#continue
	try :
		rmag=np.array(input('range of mag in  star catalogue. '))
		rmag[0]
		rmag[1]
	except :
		print('rmag will be setted by auto [15,23] .')
		rmag=[15,23]
	try :
		rmag_err=float(input('max of mag_err in  star catalogue. '))
	except :
		print('rmag_err will be setted by auto 0.1 .')
		rmag_err=0.1
	try :
		mytuo=float(input('max of tuo in  image.'))
	except :
		print('mytuo will be setted by auto 0.3 .')
		mytuo=0.3
	try :
		ymag_err=float(input('max of mag_err in  image. '))
	except :
		print('ymag_err will be setted by auto 0.1 .')
		ymag_err=0.1
	try :
		lim=float(input('number of  standard  star . '))
	except :
		print(' number of  standard  star will be setted 15.')
		lim=15



#######
print('\n\n\n\t\tdata read   \n\n\n')

#

im_data,limitlist=rim(imname)
db_data=rdb(dbname)

######
print('\n\n\n\t\tdata match')

print('im :'+str(len(im_data)),'\ndb :'+str(len(db_data)))
mymagdb=match(im_data,db_data)




#or_mag =oy_mag+sr_mag-sy_mag

x_x=im_s[2] # 选取mag_ap作为仪器星等
err_err=im_s[3]
#or_mag1=fit1(mymag,'fit1')

or_mag2,mag_limit,y_err,k,b=fit2(mymagdb,mm)

#or_mag3=line_fit(mymag,'line_fit')
print('\n\n#######################\n\n')
print(' head   ra     dec    mag_err')
print(s_head,im_s[0],im_s[1],im_s[3])
magins_lim = cal_upper_lim2()
maggg_lim3 = k * magins_lim[0] + b
maggg_lim5 = k * magins_lim[1] + b
print('(old) The uplimit magnitude in 3 sigma is :'+str(mag_limit))
print('(new) The uplimit magnitude in 3 sigma is :'+str(maggg_lim3))
print('(new) The uplimit magnitude in 5 sigma is :'+str(maggg_lim5))
print('The cured magnitude about GRB is ',or_mag2,' +/- ',y_err,'  .\nDone\n')
