from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR,	LPDWORD, DWORD, HANDLE, BOOL

MessageBoxA = windll.user32.MessageBoxA 
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT

print(MessageBoxA)

lpText = LPCSTR(b"world!")
lpCaption = LPCSTR(b"hello")
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001
MB_YESNO = 0x00000004

#MessageBoxA(None, lpText, lpCaption,MB_YESNO)

GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = INT

buffer_size = DWORD(2)
buffer = create_string_buffer(buffer_size.value)

GetUserNameA(buffer,byref(buffer_size))
print(buffer.value)

error = GetLastError()

if error:
	print(error)
	print(WinError(error))

class RECT(Structure):
	_fields_ = [("left",c_long),
				("top",c_long),
				("right",c_long),
				("bottom",c_long)]

rect = RECT()

print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)

rect.left = 1
print(rect.left)

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE,POINTER(RECT))
GetWindowRect.restype = BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

print(rect.left)
print(rect.top)
print(rect.right)

print(rect.bottom)