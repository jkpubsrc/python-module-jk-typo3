#!/usr/bin/python3




import jk_typo3
import jk_flexdata



TYPO3_DIR_PATH = "/srv/www/Typo3Test"



print()

mgr = jk_typo3.Typo3InstallationMgr(TYPO3_DIR_PATH)

print("Installed version: " + str(mgr.getVersion()))

print()

typo3Settings = jk_flexdata.FlexObject(mgr.getLocalSettings())
dbSettings = typo3Settings.DB.Connections.Default
assert dbSettings.driver == "mysqli"

print("dbHost = " + repr(dbSettings.host))
print("dbPort = " + repr(dbSettings.port))
print("dbName = " + repr(dbSettings.dbname))
print("dbUser = " + repr(dbSettings.user))
print("dbPassword = " + repr(dbSettings.password))

print()




