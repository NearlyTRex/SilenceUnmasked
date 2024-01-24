; Silence Unmasked
; Waterstone Productions

[Setup]
AppId={{38F8139D-CF6E-482B-A163-07855633AE60}
AppName=Silence Unmasked
AppVerName=Silence Unmasked 1.0
AppPublisher=Waterstone Productions
AppPublisherURL=http://www.wsprod.com/
AppSupportURL=http://www.wsprod.com/
AppUpdatesURL=http://www.wsprod.com/
DefaultDirName={pf}\Silence Unmasked
DefaultGroupName=Silence Unmasked
OutputBaseFilename=Setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "Game\*"; DestDir: "{app}\Game"; Excludes: "*.svn"; Flags: ignoreversion
Source: "Manager\*"; DestDir: "{app}\Manager"; Excludes: "*.svn"; Flags: ignoreversion
Source: "Media\*"; DestDir: "{app}\Media"; Excludes: "*.svn"; Flags: ignoreversion
Source: "Meta\*"; DestDir: "{app}\Meta"; Excludes: "*.svn"; Flags: ignoreversion

[Icons]
Name: "{group}\Silence Unmasked"; Filename: "{app}\Game\gamestone.exe"; IconFilename: "{app}\Media\Icon.ico"; WorkingDir: "{app}\Game"
Name: "{commondesktop}\Silence Unmasked"; Filename: "{app}\Game\gamestone.exe"; IconFilename: "{app}\Media\Icon.ico"; WorkingDir: "{app}\Game"; Tasks: desktopicon

[Run]
Filename: "{app}\Game\gamestone.exe"; Description: "{cm:LaunchProgram,Silence Unmasked}"; Flags: nowait postinstall skipifsilent








