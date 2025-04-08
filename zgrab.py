import subprocess
import dns.resolver
print("""
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

      
      
=========================================================
DISCLAIMER:

This tool is developed for educational and authorized
security testing purposes only.

Unauthorized use against systems or domains without
explicit permission is strictly prohibited and may
be illegal under applicable laws.

The developer assumes no responsibility for misuse.

Proceed only if you understand and accept this.
=========================================================""")
def get_NS(domain):
    try:
        final_domain = domain.lower()
        answers = dns.resolver.resolve(final_domain, 'NS')
        NS_servers = [ns.to_text().rstrip('.') for ns in answers]
        return NS_servers
    except dns.resolver.NoAnswer:
        print(f"No NS records found for domain: {domain}")
        return []
    except Exception as e:
        print(f"An unknown error occurred while retrieving NS records: {e}")
        return []
    
def downloadzonefile(domain, NS_name, file_name):
    try: 
        output = subprocess.run(
            ['dig', 'AXFR', '@' + NS_name, domain],
            capture_output=True,
            text=True
        )
        
        # Überprüfen, ob Daten im Standard-Ausgabe-Stream vorhanden sind
        if output.stdout:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(output.stdout)
            print(f"Zone file successfully written to {file_name}.")
        else:
            print(f"No zone transfer data received for domain: {domain} from nameserver: {NS_name}.")
            if output.stderr:
                print(f"Error message from dig: {output.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running dig command: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
    except Exception as e:
        print(f"An unknown error occurred during the zone transfer: {e}")

if __name__ == "__main__":
    try:
        # Benutzer nach Domain und Dateinamen fragen
        domain = input("Please insert domain: ")
        file_name = input("Please insert file name: ")
        
        # NS-Server abrufen
        ns_list = get_NS(domain)
        
        if ns_list:
            print("Name Servers:", ns_list)
            # Zone-Transfer starten und in Datei speichern
            downloadzonefile(domain, ns_list[0], file_name)
        else:
            print("No NS records found for the domain.")
    
    except Exception as e:
        print(f"Fehler: {e}")
