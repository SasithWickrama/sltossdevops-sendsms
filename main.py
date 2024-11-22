import multiprocessing
import random
import time
import db
from log import getLogger
from sendsms import Sendsms
import sendsms
import sys

logger = getLogger('smslog', 'logs/smslog')


def specific_string(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # define the specific string
    # define the condition for random string
    return ''.join((random.choice(sample_string)) for x in range(length))


def sendSmsAuto(x):
    ref = specific_string(15)
    logger.info("Request : %s" % ref + " - " + str(x))
    conn = db.DbConnection.dbconnSmsPrg(self="")
    c = conn.cursor()
    #sql = 'select SEND_CUSTOMER_CONTACT,SEND_MSG,SENT_OWNER,SMS_ID from SMSMSGS1 WHERE SEND_SUCS=0   AND MOD(DBMS_ROWID.ROWID_ROW_NUMBER(SMSMSGS1.ROWID), 10) = ' + str(x)
    sql = "SELECT CUSTOMER_CONTACT FROM TEST_CUS_MOB WHERE STATUS IS NULL  AND MOD(DBMS_ROWID.ROWID_ROW_NUMBER(TEST_CUS_MOB.ROWID), 10) = " + str(x)     
    c.execute(sql)

    for row in c:

        CUSTOMER_CONTACT, = row
        
        print(CUSTOMER_CONTACT)
        
        SEND_MSG ="""Rata wata sabadiyawan aluth wena, Sithum pathum itu wena subama suba aluth avuruddak wewa! SLT-MOBITEL ekma eka sabadiyawa.
Naadu muluthum Inaipugal puthithaagum, Virupangal niraiverum, Iniya puthandu nal vazthukal. SLT- MOBITEL  nigaratra inaippu."""


        try:
            # create a cursor
            Sendsms.sendSms(CUSTOMER_CONTACT, SEND_MSG, 'OSS',CUSTOMER_CONTACT)
            print("msgid " + sendsms.msgid)
            print("smsmsgid " + sendsms.smsmsgid)
            print("msgid_id " + sendsms.msgid_id)
            

            sql = "update TEST_CUS_MOB set STATUS = : sms_rtn where  CUSTOMER_CONTACT= :sms_id"
            #print("sql "+ sql)
            with conn.cursor() as cursor:
                cursor.execute(sql, [sendsms.response, CUSTOMER_CONTACT])
                # cursor.execute(sql)
                conn.commit()
        except conn.Error as error:
            print('Error occurred:' + str(error))
            

def sendSmsAutoTwo(x):
    ref = specific_string(15)
    logger.info("Request : %s" % ref + " - " + str(x))
    conn = db.DbConnection.dbconnSmsPrg(self="")
    c = conn.cursor()
    #sql = 'select SEND_CUSTOMER_CONTACT,SEND_MSG,SENT_OWNER,SMS_ID from SMSMSGS1 WHERE SEND_SUCS=0   AND MOD(DBMS_ROWID.ROWID_ROW_NUMBER(SMSMSGS1.ROWID), 10) = ' + str(x)
    sql = "SELECT CUSTOMER_CONTACT FROM TEST_CUS_MOB1 WHERE STATUS IS NULL AND MOD(DBMS_ROWID.ROWID_ROW_NUMBER(TEST_CUS_MOB1.ROWID), 10) = " + str(x)     
    c.execute(sql)

    for row in c:

        CUSTOMER_CONTACT, = row
        
        print(CUSTOMER_CONTACT)
        
        SEND_MSG ="""Rata wata sabadiyawan aluth wena, Sithum pathum itu wena subama suba aluth avuruddak wewa! SLT-MOBITEL ekma eka sabadiyawa.
Naadu muluthum Inaipugal puthithaagum, Virupangal niraiverum, Iniya puthandu nal vazthukal. SLT- MOBITEL  nigaratra inaippu."""


        try:
            # create a cursor
            Sendsms.sendSmsTwo(CUSTOMER_CONTACT, SEND_MSG, 'OSS',CUSTOMER_CONTACT)
            print("msgid " + sendsms.msgid)
            print("smsmsgid " + sendsms.smsmsgid)
            print("msgid_id " + sendsms.msgid_id)
            

            sql = "update TEST_CUS_MOB1 set STATUS = : sms_rtn where  CUSTOMER_CONTACT= :sms_id"
            #print("sql "+ sql)
            with conn.cursor() as cursor:
                cursor.execute(sql, [sendsms.response, CUSTOMER_CONTACT])
                # cursor.execute(sql)
                conn.commit()
        except conn.Error as error:
            print('Error occurred:' + str(error))


def sendSmsAutoThree(x):
    ref = specific_string(15)
    logger.info("Request : %s" % ref + " - " + str(x))
    conn = db.DbConnection.dbconnSmsPrg(self="")
    c = conn.cursor()
    #sql = 'select SEND_CUSTOMER_CONTACT,SEND_MSG,SENT_OWNER,SMS_ID from SMSMSGS1 WHERE SEND_SUCS=0   AND MOD(DBMS_ROWID.ROWID_ROW_NUMBER(SMSMSGS1.ROWID), 10) = ' + str(x)
    sql = "SELECT CUSTOMER_CONTACT FROM TEST_CUS_MOB2 WHERE STATUS IS NULL AND MOD(DBMS_ROWID.ROWID_ROW_NUMBER(TEST_CUS_MOB2.ROWID), 10) = " + str(x)     
    c.execute(sql)

    for row in c:

        CUSTOMER_CONTACT, = row
        
        print(CUSTOMER_CONTACT)
        
        SEND_MSG ="""Rata wata sabadiyawan aluth wena, Sithum pathum itu wena subama suba aluth avuruddak wewa! SLT-MOBITEL ekma eka sabadiyawa.
Naadu muluthum Inaipugal puthithaagum, Virupangal niraiverum, Iniya puthandu nal vazthukal. SLT- MOBITEL  nigaratra inaippu."""


        try:
            # create a cursor
            Sendsms.sendSmsThree(CUSTOMER_CONTACT, SEND_MSG, 'OSS',CUSTOMER_CONTACT)
            print("msgid " + sendsms.msgid)
            print("smsmsgid " + sendsms.smsmsgid)
            print("msgid_id " + sendsms.msgid_id)
            

            sql = "update TEST_CUS_MOB2 set STATUS = : sms_rtn where  CUSTOMER_CONTACT= :sms_id"
            #print("sql "+ sql)
            with conn.cursor() as cursor:
                cursor.execute(sql, [sendsms.response, CUSTOMER_CONTACT])
                # cursor.execute(sql)
                conn.commit()
        except conn.Error as error:
            print('Error occurred:' + str(error))
            
            
if __name__ == '__main__':
    
    if sys.argv[1] == 'AUTO':
        processes = []
        for i in range(0, 8):
            p = multiprocessing.Process(target=sendSmsAuto, args=(i,))
            processes.append(p)
            p.start()
            
            p2 = multiprocessing.Process(target=sendSmsAutoTwo, args=(i,))
            processes.append(p2)
            p2.start()
            
            p3 = multiprocessing.Process(target=sendSmsAutoThree, args=(i,))
            processes.append(p3)
            p3.start()
            
            
           # multiprocessing_func(i)
        for process in processes:
            process.join()
            
       
            

                
   

