using Windows.Graphics.Capture;

var picker = new GraphicsCapturePicker();
var hwnd = WinRT.Interop.WindowNative.GetWindowHandle(User 1 - Anki);
WinRT.Interop.InitializeWithWindow.Initialize(picker, hwnd);
GraphicsCaptureItem item = await picker.PickSingleItemAsync();
