import pyperclip as pc

while True:
    s = pc.waitForNewPaste()
    res = s.replace(' ', '_')
    res += '.py'
    pc.copy(res)
