; EasyCopy Installer Script
; Save as EasyCopyInstaller.iss
; Compile with Inno Setup Compiler

#define MyAppName "EasyCopy"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "Candy_man"
#define MyAppExeName "EasyCopy.exe"

[Setup]
AppId={{A8D7D4B7-9A56-4D3C-BB21-3F4EAA11C001}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=installer
OutputBaseFilename=EasyCopy-{#MyAppVersion}
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
Source: "dist\EasyCopy\EasyCopy.exe"; DestDir: "{app}"; Flags: ignoreversion

; Assets folder
Source: "dist\EasyCopy\assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

; Internal runtime files
Source: "dist\EasyCopy\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\EasyCopy"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall EasyCopy"; Filename: "{uninstallexe}"
Name: "{autodesktop}\EasyCopy"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch EasyCopy"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
