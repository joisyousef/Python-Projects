from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
LPCTSTR = c_char_p
SIZE_T = c_size_t

OpenProcess = kernel32.OpenProcess
OpenProcess.argstypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
OpenProcess.restype = wintypes.HANDLE

VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argstypes = (wintypes.HANDLE, wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAllocEx.restype = wintypes.LPVOID

WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argstypes = (wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, SIZE_T, POINTER(SIZE_T))
WriteProcessMemory.restype = wintypes.BOOL 

GetModuleHandle = kernel32.GetModuleHandle
GetModuleHandle.argstypes = (wintypes.LPCTSTR)
GetModuleHandle.restype = wintypes.HANDLE 

GetProcAddress = kernel32.GetProcAddress 
GetProcAddress.argstypes = (wintypes.HANDLE, LPCTSTR)
GetModuleHandle.restype = wintypes.LPCVOID

class _SECURITY_ATTRIBITES(Structure):
	_fields_ = [('nLength', wintypes.DWORD),
				('lpSecurityDescriptor', wintypes.LPVOID),
				('bInheritHandle', wintypes.BOOL),]

_SECURITY_ATTRIBITES = _SECURITY_ATTRIBITES
LPSECURITY_ATTRIBITES = POINTER(_SECURITY_ATTRIBITES)
LPTHREAD_START_ROUTINE = wintypes.LPVOID

CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argstypes = (wintypes.HANDLE, LPSECURITY_ATTRIBITES, SIZE_T, LPTHREAD_START_ROUTINE, wintypes.LPVOID, wintypes.DWORD, wintypes.LPDWORD)
CreateRemoteThread.restype = wintypes.HANDLE

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_READWRITE = 0x04
EXECUTE_IMMEDIATELY = 0x0
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0x00000FFF)

dll = b"C:\\Users\\youse\\Document\\python201\\hello_world.dll"

pid = 7012

handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not handle:
	raise WinError()

print("Handle obtained => {0:x}".format(handle))

remote_memory = VirtualAllocEx(handle, False, len(dll) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)

if not remote_memory:
	raise WinError()

print("Memory Allocated => {0:x}".hex(remote_memory))

write = WriteProcessMemory(handle, remote_memory, dll, len(dll) + 1, None)

if not write:
	raise WinError()

print("Bytes written => {}".format(dll))

load_lib = GetProcAddress(GetModuleHandle(b"kernel32.dll") , b"LoadLibraryA")

print("LoadLibrary address =>".hex(load_lib))

rthread = CreateRemoteThread(handle, None, 0, load_lib, remote_memory)