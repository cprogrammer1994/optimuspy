#include <Windows.h>
#include <Python.h>


extern "C" {
#ifdef _MSC_VER
	_declspec(dllexport) DWORD NvOptimusEnablement = 0x00000001;
	_declspec(dllexport) int AmdPowerXpressRequestHighPerformance = 0x00000001;
#else
	__attribute__((dllexport)) DWORD NvOptimusEnablement = 0x00000001;
	__attribute__((dllexport)) int AmdPowerXpressRequestHighPerformance = 0x00000001;
#endif
}


int main() {
	int argc = 0;
	LPWSTR * argv = CommandLineToArgvW(GetCommandLineW(), &argc);
	Py_Main(argc, argv);
}
