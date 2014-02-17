Summary:	Thomson MO5 emulator
Name:		dcmo5
Version:	11.2
Release:	3
License:	GPLv3+
Group:		Emulators
Url:		http://dcmo5.free.fr/
Source0:	http://dcmo5.free.fr/v11/download/%{name}v11.0.tar.gz
Source1:	http://dcmo5.free.fr/v11/download/%{name}v%{version}.tar.gz
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Source4:	%{name}.rom
Patch0:		dcmo5v11.2-user_directory.patch.bz2
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_ttf)

%description
DCMO5 is an emulator for the Thomson MO5 system.

%files
%doc licence/dcmo5v11-licence.txt licence/gpl-3.0.txt licence/lgpl-3.0.txt licence/vera-copyright.txt
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/%{name}/%{name}.rom

#----------------------------------------------------------------------------

%prep
%setup -q -a 1 -c %{name}-%{version}-%{release}
%patch0 -p0
sed -i s/cc/"gcc %{optflags}"/g makefile

%build
%make

%install
# binary
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 dcmo5 %{buildroot}%{_bindir}/

# icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}%{_liconsdir}
install -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png

# xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DCMO5
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

# rom
install -d -m 755 %{buildroot}%{_datadir}/apps/dcmo5
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/apps/dcmo5/%{name}.rom

