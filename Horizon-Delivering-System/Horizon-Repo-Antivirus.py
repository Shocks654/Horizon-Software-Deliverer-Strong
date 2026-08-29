import os

def execute_silent_repository_scan():
    repository_root = os.path.dirname(os.path.abspath(__file__))
    malware_signatures = ["malware", "virus_payload", "corrupt_core"]
    
    for root, dirs, files in os.walk(repository_root):
        for file in files:
            if file == "Horizon-Base-Deliverer.py":
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    content = f.read()
                    
                if any(signature in content for signature in malware_signatures):
                    print(f"REPO BREACH DETECTED: Infected component located -> {file}")
                    
                    isolated_path = file_path + ".WALL_ISOLATED"
                    os.rename(file_path, isolated_path)
                    print(f"REPO WALL ENGAGED: Locked down asset safely inside -> {isolated_path}")
            except Exception:
                continue

execute_silent_repository_scan()
