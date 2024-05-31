
APIENTRY DllMain(HMODULE hModule,
				 DWORD ul_reason_for_call,
				 LPVOID lpReserved)


switch (ul_reason_for_call)
{
case DLL_PROCESS_ATTACH:
	MessageBox(NULL, L"Hello world!", L"Hello world!", NULL)
	break;
case DLL_THREAD_ATTACH:
case DLL_THREAD_DATTACH:
case DLL_PROCESS_DATTACH:
	break;
}
return TRUE;