# ZoneGrab
 _    _      _                            _        
| |  | |    | |                          | |       
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___  
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                   
                                                   
 ______                 _____           _          
|___  /                |  __ \         | |         
   / /  ___  _ __   ___| |  \/_ __ __ _| |__       
  / /  / _ \| '_ \ / _ \ | __| '__/ _` | '_ \      
./ /__| (_) | | | |  __/ |_\ \ | | (_| | |_) |     
\_____/\___/|_| |_|\___|\____/_|  \__,_|_.__/      
                                                   


                                                  
This tool allows you to retrieve and download a domain's zone file. Any use without explicit permission is prohibited! Unauthorized access to zone files is illegal.


Requirements
To use this tool, you will need:

Python 3 installed on your system. You can download it from here.

The dnspython library to interact with DNS records. You can install it using pip:

bash
Kopieren
Bearbeiten
pip install dnspython
Git installed to clone the repository. You can download it from here.

Access to a domain's zone file, and permission to access it, as this tool performs DNS zone transfers. Unauthorized access is prohibited.

Quick Step-by-Step Guide
Install Python:

If you don’t have Python installed, download and install Python 3 from the official site.

Install Git:

If you don’t have Git installed, download and install it from here.

Clone the Repository:

Open your terminal (or command prompt), and use the following command to clone your GitHub repository:

bash
Kopieren
Bearbeiten
git clone https://github.com/yourusername/yourrepository.git
Replace yourusername/yourrepository with your actual GitHub username and repository name.

Navigate to the Repository Folder:

After cloning, navigate to the directory where the repository was saved:

bash
Kopieren
Bearbeiten
cd yourrepository
Install Required Library:

Run the following command to install the necessary library:

bash
Kopieren
Bearbeiten
pip install dnspython
Run the Script:

Run the script with Python 3:

bash
Kopieren
Bearbeiten
python3 your_script_name.py
Provide the Domain Name:

When prompted, enter the domain name you wish to query.

Enter File Name:

Enter a name for the output file where the zone information will be saved (e.g., output_zone_file.txt).

Review the Output:

The zone file information will be saved in the file you specified, and you can open it with any text editor.


