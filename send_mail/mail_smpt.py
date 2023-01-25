# import csv
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_send(subject,sender_email,password,receiver_email,message):

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    # text =message
    html = """\
    <htlm><tbody><tr>
    <td>
      <table align="center" width="600" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px">
    <tbody><tr>
           <td bgcolor="#ffffff" style="background-color:#ffffff">
           
            
            <table align="center" width="500" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px">
       <tbody><tr>
              <td style="color:#2c2c2c;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:18px;line-height:26px;padding-top:48px">
          <table align="left" width="auto" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin:0!important">
            <tbody><tr>
            <td valign="middle" style="color:#000000;font-family:adobe-clean,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px"><img alt="" src="https://ci5.googleusercontent.com/proxy/csGhMc7bD7f-w30_nwvU4AQL30_k-5DSRWhk1HfYiSjfdzzMONZoI4nEPclI5vIVHPBxXL4m8D7YFi80H9iCZcU-2yM8uDVowi-G7-C-S0XaBNRuEhzP5DRRn-b5RMbJeP8=s0-d-e1-ft#https://landing.adobe.com/dam/global/images/acrobat-pro-dc.mnemonic.480x468.png" width="30" height="auto" border="0" hspace="0" vspace="0" style="display:block;vertical-align:top" class="CToWUd" data-bit="iit"></td>
            <td width="10" style="width:10px">&nbsp;</td>
            <td valign="top" style="color:#74777a;font-family:adobe-clean,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px"><img alt="Adobe Acrobat Pro" src="https://ci4.googleusercontent.com/proxy/gz4JXsS6PdbOlu2dr6aC3a38x4tQ8hHJQ0XLQ5IgM2k1dlBS7Nd5nxX4fGOu6IxgT3QzlaPrIgjgi6o2ShQ8WOl0grGx4VDKcTbZMuDVDvaKskrcvfo67fD2xswowUdhjPiaqTl8aTP1jZwkcF8aPgbjKWe1zOsxi6144ZoxjSKj8ud7upC_IvU7HA5Ar7TGlMWIN4ApvFpULer07M3TPz7cJdq_85IHJq0kW-ecOCdcTC8MExk1_3t5xWcqwErNSOqqxgvFYiP3HF8hxnq_1wOXAJq3T8ncWW2Pl71ds6KY8W8JnXiw4VhoR43WF08CbQnvzCPUt1KB6FAh-j5zQsCUV5-D7iq5jvPpogX2n-ik-GVq8cfS1Te1-8ajq518SDyWtbPDp0DSxThMDuwUBjNP958DmBRO=s0-d-e1-ft#https://s7d9.scene7.com/is/image/AdobeDemandCreative/?fmt=png-alpha&amp;size=410,60&amp;wid=410&amp;textAttr=144,strong&amp;resolution=200&amp;textPs=%7B%5C*%5Ciscolortbl%3B74777a%3B%5Cfonttbl%7B%5Cf0%20Adobe%20Clean%20ExtraBold%3B%7D%7D%5Cf0%5Cfs40%5Csl-400%5Cvertalc%5Ckerningoptical%5Ccf1Adobe%20Acrobat%20Pro" width="205" height="30" border="0" hspace="0" vspace="0" style="color:#74777a;font-family:adobe-clean,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;display:block;vertical-align:top" class="CToWUd" data-bit="iit"></td>
            </tr>
          </tbody></table>
        </td>
             </tr>
       <tr>
              <td style="color:#000000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:60px;line-height:66px;padding-top:72px"><strong>Edit PDFs here,
there, anywhere.</strong></td>
             </tr>
           <tr><td>
               <table align="left" width="500" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px">
            
              <tbody><tr>
              <td style="color:#000000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:18px;line-height:26px;padding-top:30px">Add, edit, or remove text and images. Reorder pages so your PDF
tells a clear story. Edits are easy with Acrobat Pro&nbsp;DC.</td></tr></tbody></table>
               </td>
              
             </tr>
             <tr>
              <td style="color:#1473e6;font-family:adobe-clean,Arial,Helvetica,sans-serif;font-size:15px;line-height:20px;padding-top:40px;padding-bottom:36px">
          <a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffd9&amp;e=cDE9R0hNVllDM0Y&amp;s=bnq-P_Ehjo42NF2ac8Qq_I80ukUChicxZbz_AQpa5ZI" style="background-color:#1473e6;border-radius:20px;color:#ffffff;display:inline-block;font-size:16px;line-height:40px;text-align:center;text-decoration:none;width:180px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffd9%26e%3DcDE9R0hNVllDM0Y%26s%3Dbnq-P_Ehjo42NF2ac8Qq_I80ukUChicxZbz_AQpa5ZI&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw1iKBuH8sbByBHIjtYGp6De"><strong>Try it for free</strong></a>
          
        </td>
             </tr>
             
            </tbody></table>
            
               
            <table align="center" width="600" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:600px">
             <tbody><tr>
              </tr><tr>
              <td style="color:#000000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:22px;line-height:28px"><a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffda&amp;e=cDE9R0hNVllDM0Y&amp;s=ILX6rGX-1fxVPU0y8RtHdoi6JdSdePQEKb9ECMgsB1A" style="color:#1473e6" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffda%26e%3DcDE9R0hNVllDM0Y%26s%3DILX6rGX-1fxVPU0y8RtHdoi6JdSdePQEKb9ECMgsB1A&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw0obNqQlbKPeaxq25sUpaR2"><img alt="Edit PDFs here,
there, anywhere." src="https://ci3.googleusercontent.com/proxy/uhupDCXxyRs4OErnMpTGO592OFFZK5mRf066udyLYy7yWCNr1FStVr3oN3y2W2I285a5G830LiYk5limY91o0qxrrBPazRC9hy_XVD-JGZ7QoF57yjqA9Hm85GxBe5sCiGjfZAjlX2A=s0-d-e1-ft#https://landing.adobe.com/dam/2021/images/mwpe-844/dc-acro-cvr-hi-low.en.1200x850.gif" width="600" height="auto" border="0" hspace="0" vspace="0" style="color:#000000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:22px;line-height:28px;display:block;vertical-align:top" class="CToWUd" data-bit="iit">
        </a></td>
             </tr>
            </tbody></table>
                
      </td></tr>
      
    <tr>
    <td bgcolor="#F5F5F5" style="background-color:#f5f5f5">
      
            <table align="center" width="600" border="0" cellpadding="0" cellspacing="0" role="presentation" bgcolor="#ffffff" style="background-color:#ffffff;width:600px">
       <tbody><tr>
        <td width="20" style="width:20px">&nbsp;</td>
        <td width="30" style="width:30px">&nbsp;</td>
              <td style="color:#eb1000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:15px;line-height:20px;padding-top:5px;padding-bottom:5px"><strong>Acrobat's Got It.</strong></td>
        <td width="30" style="width:30px">&nbsp;</td>
        <td width="20" style="width:20px">&nbsp;</td>
             </tr>
            </tbody></table>
        
     
      
      <table align="center" width="500" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px">
     <tbody><tr>
      <td valign="middle" style="padding-top:50px">
        <div style="font-size:0">
          
          <div style="display:inline-block;vertical-align:middle;width:50%;min-width:250px;max-width:100%;width:-webkit-calc(230400px - 48000%);min-width:-webkit-calc(50%);width:calc(230400px - 48000%);min-width:calc(50%)">
          
          <table align="left" border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
           <tbody><tr>
            <td style="color:#eb1000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:12px;line-height:18px"><img alt="Adobe" src="https://ci3.googleusercontent.com/proxy/H8W7VswvB6dsQY0FBp6VXWaJLEoZYiJ4pssW5FaxinYMNGs2FiDIjM11vaH-pRMnqqhinKKpQyTQZl2cQXioItR3xArT58F-Y5F6oYiOkHXDTZy0P7iCDj2RjKTa=s0-d-e1-ft#https://landing.adobe.com/dam/global/images/adobe-logo.classic.160x222.png" width="30" height="auto" border="0" hspace="0" vspace="0" style="color:#eb1000;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:12px;line-height:18px;display:block;vertical-align:top" class="CToWUd" data-bit="iit"></td>
           </tr>
          </tbody></table>
          
          </div>
          
          <div style="display:inline-block;vertical-align:middle;width:50%;min-width:250px;max-width:100%;width:-webkit-calc(230400px - 48000%);min-width:-webkit-calc(50%);width:calc(230400px - 48000%);min-width:calc(50%)">
          
          <table align="right" width="auto" border="0" cellpadding="0" cellspacing="0" role="presentation" style="float:right">
           <tbody><tr>
            <td style="color:#959595;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:12px;line-height:12px"><a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffdb" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffdb&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw2E43FbRi3lDj-sU5bOd7sK"><img alt="Facebook" src="https://ci5.googleusercontent.com/proxy/HtGYEHO_UsQbKaZs-vNiBae8tM_Vh0NQEpFJiggp_sY-QEkexPSnUtxQzeDVx1WGBffREOOCRJO83pREkYNSJVGdJKFWvKNgylci_XfiEcaiPvsb4AJdlYo=s0-d-e1-ft#https://landing.adobe.com/dam/global/images/social/facebook.959595.png" width="9" height="17" border="0" hspace="0" vspace="0" style="display:block;vertical-align:top" class="CToWUd" data-bit="iit"></a></td>
            <td width="30" style="width:30px">&nbsp;</td>
            <td style="color:#959595;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:12px;line-height:12px"><a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffdc" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffdc&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw2HXHZ2UrqQKLa9epyUU2_6"><img alt="LinkedIn" src="https://ci4.googleusercontent.com/proxy/SYKvNcXU_aVzF0W9tk-jSFbT2tIKKHnvTS6ybCGLscEScuZZi8n6C8MRwDZ9hnM8at3oXM9U2Znj0drEQLaqAQwLBaGKIrhlTEbK7enVrE2gCrdVzPSKquQ=s0-d-e1-ft#https://landing.adobe.com/dam/global/images/social/linkedin.959595.png" width="17" height="17" border="0" hspace="0" vspace="0" style="display:block;vertical-align:top" class="CToWUd" data-bit="iit"></a></td>
            <td width="30" style="width:30px">&nbsp;</td>
            <td style="color:#959595;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:12px;line-height:12px"><a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffdd" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffdd&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw1VEjdrnIr6ZjOivGnjgkHf"><img alt="Twitter" src="https://ci3.googleusercontent.com/proxy/gCOtvAcU1lNYc9cdS1wFcigqu0G-7vbqqbP4Cit0ry27YpffTYJkVMODVLAn6kTD0VEtPWnWwER81b4js2gNdiKfncYO48GWhlHBhNpdPLpXNN35_5tNuw=s0-d-e1-ft#https://landing.adobe.com/dam/global/images/social/twitter.959595.png" width="21" height="17" border="0" hspace="0" vspace="0" style="display:block;vertical-align:top" class="CToWUd" data-bit="iit"></a></td>
           </tr>
          </tbody></table>
          
          </div>
        
        </div>
      </td>
       </tr>
      </tbody></table>      
          
      
      
      <table align="center" width="500" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px">
      <tbody><tr>
        <td style="color:#959595;font-family:adobe-clean,Helvetica Neue,Helvetica,Verdana,Arial,sans-serif;font-size:11px;line-height:18px;padding-top:50px;padding-bottom:100px">
          <p id="m_3460555241579610484m_-8097591577830163093reg_foot">Adobe, the Adobe logo, Creative Cloud, the Creative Cloud logo, and Document Cloud are either registered  trademarks or trademarks of Adobe in the United States and/or other countries.<br><br>This is not a comprehensive list of Adobe trademarks. All other trademarks are the property of their respective owners. <a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffde" style="color:#959595;text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffde&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw2LNsVmYFjXsJHGGeEOkS2M">Adobe Trademark Guidelines</a>. <br><br>

© 2023 Adobe Inc. All&nbsp;rights&nbsp;reserved.<br><br>
          This is a marketing email from Adobe Systems Software Ireland Limited, 4-6 Riverwalk, Citywest Business Park, Dublin 24, Ireland.  <a style="TEXT-DECORATION:underline;COLOR:#a1a1a1" href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffdf&amp;e=cDE9JTQwdzVsQ29nMyUyQlowMHZQRkRFVkZQWnd6WkRFdkVkVXRLZzFVangyJTJGMU5id29STWJmanBWUnVpMXd0dEN0c2V6ZFEmcDI9JmxvYz1pbiZwMz0zNQ&amp;s=r5oE6r2SHlxuatNcNE_Z3IyDoz-eoMMreiu82CRhdoA" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffdf%26e%3DcDE9JTQwdzVsQ29nMyUyQlowMHZQRkRFVkZQWnd6WkRFdkVkVXRLZzFVangyJTJGMU5id29STWJmanBWUnVpMXd0dEN0c2V6ZFEmcDI9JmxvYz1pbiZwMz0zNQ%26s%3Dr5oE6r2SHlxuatNcNE_Z3IyDoz-eoMMreiu82CRhdoA&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw3_RlE4K86jUf42mJ60ibTL">Click&nbsp;here</a>  to unsubscribe, or send an unsubscribe request to the address above.<br>
                <br>
                Your privacy is important to us. Please review Adobe's Privacy Policy by clicking here:<br>
                <a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffe0" style="color:#959595;text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffe0&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw1TqMHrS6V5EKeKS6-W1qeK"> www.adobe.com/in/privacy.html</a>.<br>
                <br>
                PLEASE DO NOT REPLY TO THIS MESSAGE. To obtain information on how to contact Adobe, visit the web at <a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffe1" style="color:#959595;text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffe1&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw1fV3t9Z6xuDgapWfL_M_qW"> helpx.adobe.com/in/support.<wbr>html</a>.
                If you have a privacy-related complaint, send it to <a href="mailto:privacy@adobe.com" style="color:#959595;text-decoration:underline" target="_blank">privacy@adobe.com</a>.<br>
                </p><div style="margin-bottom:12px;margin-top:10px;color:#959595"> This email has been sent to
                  <a href="mailto:cqfsg4r8mw@privaterelay.appleid.com" style="color:#959595;text-decoration:underline" target="_blank">cqfsg4r8mw@privaterelay.<wbr>appleid.com</a>
</div>
      <a href="https://t-info.mail.adobe.com/r/?id=he4f4110d,fa60a8d2,be2fffe2&amp;e=cDE9JTQwNm9sZkRpV29UOGZCZ2FIaXJLbElVWUJFOVZGUnd3SUs2OW53MnB2Qk9kNCUzRA&amp;s=Ap0lWHEPhrgdBvstgp2DCChoSyfqOeXmQ1J1PjVadJM" style="color:#959595" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://t-info.mail.adobe.com/r/?id%3Dhe4f4110d,fa60a8d2,be2fffe2%26e%3DcDE9JTQwNm9sZkRpV29UOGZCZ2FIaXJLbElVWUJFOVZGUnd3SUs2OW53MnB2Qk9kNCUzRA%26s%3DAp0lWHEPhrgdBvstgp2DCChoSyfqOeXmQ1J1PjVadJM&amp;source=gmail&amp;ust=1673456831102000&amp;usg=AOvVaw38xm3gyB1kUiqYO0dawBg5">Read online</a>
      </td>
      </tr>
      </tbody></table>
      
      
    </td>
    </tr>
    </tbody></table>
    </td>
  </tr>
</tbody>
</html>
    """

    # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text.as_string(), "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)

    # server.login(sender_email, password)
    with smtplib.SMTP("mail.tikuntech.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())


import csv


with open("output_info.csv", 'r',encoding="utf-8") as file:
  csvreader = csv.reader(file)
#   next()
  for row in csvreader:
    # print(row)
    try:
        sender_email = "datamanagement@tikuntech.com"
        receiver_email = row[5]
        password = "Maidenatlanta123"
        # message=""
        print(row[5])
        subject="Tikuntech"
        message = """\

        This is my first email sent through Python smtplib."""
        mail_send(subject,sender_email,password,receiver_email,message)
    except Exception as err:
        print(err)
        pass
        
