
## Get Bonsai's PCO library
https://github.com/bonsai-rx/pco

## Install PCO SDK 
https://www.pco-tech.com/de/software/development-tools/pcosdk/

## Create DLL folder structure next to Bonsai.Pco 
Externals > pco.sdk > x86 / x64
Copy the relevant DLLs from the SDK to that folder. 
If USB connection, you only need SC2_Cam.dll. sc2_usb.dll is copied to the system at SDK install (see below)

	From the PCO SDK manual:
	The API  base  functionality  is  to  configure  and  control  the  camera  settings  and  to  transfer  the  acquired images from the camera to the PC. These functions are available through function calls inside  the  SC2_Cam.dll. The  SC2_Cam.dll  has  the  capability  to  control  any  PCO camera regardless of the camera type and hardware interface). 


If using a CameraLink connection, also add the relevant dll 

	During installation the following files are copied to the target-directory.
	\bin
	\bin64
	SC2_Cam.dll API executable dynamic link library 
	SC2_cl_me4.dll Interface DLL to Silicon Software ME4 Camera Link framegrabber family 
	SC2_cl_mtx.dll Interface DLL to Matrox Camera Link Solios framegrabber family 
	SC2_cl_nat.dll Interface DLL to National Instruments Camera Link frame grabber family 
	SC2_clhs.dll Interface DLL to CLHS framegrabber 
	SC2_cl_ser.dll Interface DLL to any Camera Link framegrabber compatible to the Camera Link specification. clserxxx interface DLL must be available from the grabber manufactorer. With the sc2_cl_ser DLL all Camera Control commands can be used, but not the functions of the chapter BUFFER MANAGEMENT, IMAGE ACQUISITION and DRIVER MANAGEMENT.

	For the above Camera Link interface DLL’s the Runtime/driver environment of the framegrabber manufacturer must be installed and working properly.

	Additional interfaces are available through the following DLL’s: sc2_1394.dll, sc2_usb.dll, sc2_usb3.dll, sc2_gige.dll, sc2_gige1.dll, sc2_gige2.dll. These interface DLL’s are installed to the system directory during pco.driver installation.

## Compile
Open Bonsai.Pco solution in VS
Compile solution

## Open Bonsai
In Manage Packages' settings, create a new source for the PCO library.
Set the .nupkg directory there (i.e., C:\Bonsai\Source\pco\bin\Release) 
Close settings and go to the PCO library. Install package. 




