import hashlib
import requests
import os

def check_network_integrity():
    local_file = os.path.expanduser('~/the-peculiar-library/ontology/padi-v3.ttl')
    # Pointing to your public GitHub raw content
    remote_hash_url = "https://raw.githubusercontent.com/PeculiarLibrarian/the-peculiar-library/main/ontology/padi.sha256"
    
    if not os.path.exists(local_file):
        print("🚨 ERROR: Local PADI file not found!")
        return

    # Calculate local hash
    with open(local_file, "rb") as f:
        local_hash = hashlib.sha256(f.read()).hexdigest()
    
    # Fetch remote authority hash
    try:
        response = requests.get(remote_hash_url, timeout=10)
        if response.status_code == 200:
            remote_hash = response.text.split()[0]
            
            if local_hash == remote_hash:
                print("✅ NETWORK CONSENSUS ACHIEVED: Local node matches Global Embassy.")
            else:
                print("🚨 ECLIPSE ATTACK DETECTED: Local data differs from Global Authority!")
                print(f"Local:  {local_hash}")
                print(f"Remote: {remote_hash}")
        else:
            print(f"⚠️ REMOTE CHECK FAILED: GitHub returned status {response.status_code}")
    except Exception as e:
        print(f"⚠️ NETWORK OFFLINE: Operating in Sovereign Isolation Mode.")

if __name__ == "__main__":
    check_network_integrity()
