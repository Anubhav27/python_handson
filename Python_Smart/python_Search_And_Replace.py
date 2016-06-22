__author__ = 'Anubhav'

import os
propfile='C:\\Pure_Patterns\\'

"""
with open(os.path.join(propfile,'MDM_Fixpack.properties'),'r') as f:
    newlines = []
    for line in f.readlines():
        if line.__contains__('Database ,Operational Server ,'):
                newlines.append(line.replace('Database ,Operational Server ,', 'Database ,Operational Server , Reference DataManagement UI ,Business Administration UI ,'))
        elif line.__contains__('com.ibm.mdm.install.iu.localization.feature,com.ibm.im.mdm.db.feature,com.ibm.im.mdm.app.feature'):
                newlines.append(line.replace('com.ibm.mdm.install.iu.localization.feature,com.ibm.im.mdm.db.feature,com.ibm.im.mdm.app.feature','com.ibm.mdm.install.iu.localization.feature,com.ibm.im.mdm.db.feature,com.ibm.im.mdm.app.feature,com.ibm.mdm.ba.webapp.feature,com.ibm.mdm.rdm.webapp.feature'))
        else:
                newlines.append(line)
with open(os.path.join(propfile,'MDM_Fixpack.properties'), 'w') as f:
    for line in newlines:
                    f.write(line)
"""

def searchAndReplace_Fixpack_Properties(propfile):
	'''
		search and replace properties in MDM fixpack properties
	'''

	with open(os.path.join(propfile,'02000/MDM_Fixpack.properties'), 'r') as f:
            newlines = []
            for line in f.readlines():
                if line.__contains__('Database ,Operational Server ,'):
                    newlines.append(line.replace('Database ,Operational Server ,', 'Database ,Operational Server , Reference DataManagement UI ,Business Administration UI ,'))
                elif line.__contains__('com.ibm.mdm.install.iu.localization.feature,com.ibm.im.mdm.db.feature,com.ibm.im.mdm.app.feature'):
                    newlines.append(line.replace('com.ibm.mdm.install.iu.localization.feature,com.ibm.im.mdm.db.feature,com.ibm.im.mdm.app.feature','com.ibm.mdm.install.iu.localization.feature,com.ibm.im.mdm.db.feature,com.ibm.im.mdm.app.feature,com.ibm.mdm.ba.webapp.feature,com.ibm.mdm.rdm.webapp.feature'))
                else:
                    newlines.append(line)

        with open(os.path.join(propfile,'02000/MDM_Fixpack.properties'), 'w') as f:
            for line in newlines:
                f.write(line)



searchAndReplace_Fixpack_Properties(propfile)





