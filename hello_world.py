import ctypes #Import for types used to make windows calls

user_handle = ctypes.WinDLL('User32.dll')#Handle for the user 32 libtreary
k_handle = ctypes.WinDLL('Kernel32.dll')#Handle for the kernel library
Hwnd = None# Handle for the application to which the message box is assigned
lpText = 'Hello World'#Text used in the messag box
lpCaption= 'mosla Rulez!'#caption on top of the message box
uType = 0x00000001#Hexadecimal figure representing the type of message box, in this case a simple ok or cancel message box
response = user_handle.MessageBoxW(Hwnd, lpText, lpCaption, uType)#Call to the actual message box with given parameters
#Check to see if there is an actuall error and print
error = k_handle.GetLastError()
if error != 0:
    print('Error Code: {0}'.format(error))
    exit(1)
#Call to print what the user pressed on the message box
if response == 1:
    print('User Clicked OK!')
elif response == 2:
    print('User Clicked the cancel button')