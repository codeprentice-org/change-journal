# Import library
from py_topping.data_connection.sharepoint import da_tran_SP365
# Create connection
user_id="Aryan@carbonterra.earth"
password_id="Habibilaagebeshi1@"
sp = da_tran_SP365(site_url = 'https://carbonterra-my.sharepoint.com/:u:/g/personal/pbordioug_carbonterra_earth/EZzyhKvGhSpHqz9_r3fnslgBkmoqFdfkwdaMYq6doXWxTg?e=lc9qgc',user=user_id,password=password_id)
# Create download path from download URL
download_path = sp.create_link('https://carbonterra-my.sharepoint.com/personal/pbordioug_carbonterra_earth/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fpbordioug%5Fcarbonterra%5Fearth%2FDocuments%2FAttachments%2FSaskGrid%5F2015%5FQUARTERSECTION%2Ezip')
# Download file

    #sh_config.sh_client_id = 'f668a789-e9c0-4a61-8c25-b48cc8bbaccf'
    #sh_config.sh_client_secret = 'm7{7![TbVZcEbg3]:CMqjU4r6Qh%Gd5|n|O4UTwp'
sp.download(sharepoint_location = download_path
            ,local_location = '/home/ahnaf.ryan/')



## command to download zip file
#wget --cookies=on --load-cookies cookies.txt --keep-session-cookies --user Aryan@carbonterra.earth --password Habibilaagebeshi1@  "https://carbonterra-my.sharepoint.com/personal/pbordioug_carbonterra_earth/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fpbordioug%5Fcarbonterra%5Fearth%2FDocuments%2FAttachments%2FSaskGrid%5F2015%5FQUARTERSECTION%2Ezip"