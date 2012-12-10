Name:			dcmo5
Version:		11.2
Release:		%mkrel 2

Summary:	Thomson MO5 emulator
Group:		Emulators
License:	GPLv3+
URL:		http://dcmo5.free.fr/
Source0:	http://dcmo5.free.fr/v11/download/%{name}v11.0.tar.gz
Source1:	http://dcmo5.free.fr/v11/download/%{name}v%{version}.tar.gz
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Source4:	%{name}.rom
Patch0:		dcmo5v11.2-user_directory.patch.bz2
BuildRequires:  SDL-devel
BuildRequires:  SDL_ttf-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

#Provides: dcmo5

%description
DCMO5 is an emulator for the Thomson MO5 system.

%prep
%setup -q -a 1 -c %{name}-%{version}-%{release}
%patch0 -p0

%build
%make

%install
rm -rf %{buildroot}
# binary
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 dcmo5 %{buildroot}%{_bindir}/
# icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{_sourcedir}/%{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}%{_liconsdir}
install -m 644 %{_sourcedir}/%{name}-16.png %{buildroot}%{_liconsdir}/%{name}.png
# xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DCMO5
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF
# rom
install -d -m 755 %{buildroot}%{_datadir}/apps/dcmo5
install -m 644 %{_sourcedir}/%{name}.rom %{buildroot}%{_datadir}/apps/dcmo5

%files
%defattr(-,root,root)
%doc documentation/dcmo5v11.css documentation/dcmo5v11en.html documentation/dcmo5v11fr.html documentation/index.html licence/dcmo5v11-licence.txt licence/gpl-3.0.txt licence/lgpl-3.0.txt licence/vera-copyright.txt
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/apps/%{name}/%{name}.rom

%clean
rm -rf %{buildroot}



%changelog
* Tue Aug 02 2011 Andrey Bondrov <abondrov@mandriva.org> 11.2-2mdv2012.0
+ Revision: 692795
- imported package dcmo5


* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@zarb.org> 11.2-1plf2009.1
-  contributed by Jean-Christophe Cardot (<plf@cardot.net>)

* Mon Oct 27 2008 Jean-Christophe Cardot <plf@cardot.net> 11.0-1plf
- release
