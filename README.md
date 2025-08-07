# ProtoBreach

> Abusing URL Protocols + Config Manipulation for Sandbox Bypassing  
> **Target:** Edge and Chrome

---

## Overview

1. **Registry Manipulation**  
   - Modify: `HKCU\Classes\{PROTOCOL}`  
   - Replace the value in the `command` key  
   - Add a new key: `\shell\open\command` pointing to your payload

2. **Bypass User Prompts via Whitelist**  
   - Add your protocol and origin to:  
     `AutoLaunchProtocolsComponent\<x.x.x.x>\protocols.json`  
   - This allows silent execution via iframe

3. **Trigger Execution with iframe**  
   - Example:
     ```html
     <iframe src="your-protocol:///">
     ```

---

## Setup

1. Add your site and URL protocol to:
   - `__badboy.hta`
   - `index.html`
   - `create_lnk.py`

2. Run the script to generate the shortcut:
   ```bash
   python3 create_lnk.py

---

## Demo




https://github.com/user-attachments/assets/cbc9ebf7-7f00-4993-814d-768ee96fe9e6




---

## References
1. https://textslashplain.com/2020/02/20/bypassing-appprotocol-prompts/ 
2. https://chromeenterprise.google/policies/?policy=AutoLaunchProtocolsFromOrigins
3. https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/autolaunchprotocolsfromorigins
4. https://stackoverflow.com/questions/62926156/chrome-84-a-website-wants-to-open-this-application-handlers
5. https://blog.0patch.com/2021/12/micropatching-ms-officecmd-remote-code.html
