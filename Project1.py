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







"""
This Python code is using the `ctypes` library to interact with the Windows API functions, specifically to perform code injection into a remote process. Here's a breakdown of what the code does:

1. Imports necessary modules from `ctypes` and `ctypes.wintypes`.
2. Retrieves handles to various Windows API functions from the `kernel32.dll` library.
3. Defines necessary data types and constants for Windows API function parameters.
4. Defines a structure `_SECURITY_ATTRIBITES` and its pointer `LPSECURITY_ATTRIBITES`.
5. Allocates a handle to a remote process using `OpenProcess` with full access rights (`PROCESS_ALL_ACCESS`).
6. Allocates virtual memory in the remote process using `VirtualAllocEx`.
7. Writes the path of a DLL file (`dll`) into the allocated virtual memory of the remote process using `WriteProcessMemory`.
8. Retrieves the handle of the `kernel32.dll` module in the remote process using `GetModuleHandle`.
9. Retrieves the address of the `LoadLibraryA` function in the remote `kernel32.dll` module using `GetProcAddress`.
10. Creates a remote thread in the target process using `CreateRemoteThread`. This new thread will execute the `LoadLibraryA` function with the parameter being the address of the allocated virtual memory containing the DLL path.

In summary, this code is a basic implementation of DLL injection into a remote process on Windows. The DLL specified in the `dll` variable is loaded into the target process using the `LoadLibraryA` function, executed in a new remote thread created with `CreateRemoteThread`. This technique is commonly used for various purposes, including injecting code into other processes for debugging, monitoring, or malicious activities.
"""