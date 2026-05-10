#define MyAppName "cdyCopy"
#define MyAppVersion "1.1.0"
#define MyAppPublisher "Candy_man"
#define MyAppExeName "cdyCopy.exe"

[Setup]
AppId={{A8D7D4B7-9A56-4D3C-BB21-3F4EAA11C001}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=installer
OutputBaseFilename=cdyCopy-{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
PrivilegesRequired=admin
LicenseFile=LICENSE

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"; Flags: checkablealone

[Files]
; Main EXE
Source: "dist\cdyCopy\cdyCopy.exe"; DestDir: "{app}"; Flags: ignoreversion

; Assets
Source: "dist\cdyCopy\icon.png"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\cdyCopy\config.ini"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; Internal runtime files
Source: "dist\cdyCopy\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\cdyCopy"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall cdyCopy"; Filename: "{uninstallexe}"
Name: "{autodesktop}\cdyCopy"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch cdyCopy"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
