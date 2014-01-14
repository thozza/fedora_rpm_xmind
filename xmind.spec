%define __jar_repack 0

%define version_suffix 201311050558

Name:		xmind
Version:	3.4.0
Release:	1%{?dist}
Summary:	Brainstorming and Mind Mapping
Group:      Applications/Productivity
License:    EPL or LGPLv3
URL:		http://www.xmind.net/
Source0:    http://www.xmind.net/xmind/downloads/%{name}-portable-%{version}.%{version_suffix}.zip
Source1:    xmind.sh
Source2:    xmind.png
Source3:    xmind.xml
Source4:    xmind.desktop
ExcludeArch:ppc ppc64 arm s390x sparc
BuildRequires:unzip	
BuildRequires: desktop-file-utils
Requires: java

%description
XMind is an open source project that contributes to building a cutting-edge brainstorming/mind-mapping facility, focused on both usability and extendability. It helps people in capturing ideas into visually self-organized charts and sharing them for collaboration and communication. Currently supporting mind maps, fishbone diagrams, tree diagrams, org-charts, logic charts, and even spreadsheets. Often used for knowledge management, meeting minutes, task management, and GTD. 

%prep
#option -c is not working, it does not create specified dir
#%setup -q -c "%{name}-portable-%{version}"
%setup -q -c

%ifarch x86_64
    rm -r XMind_Linux XMind_Windows XMind_Mac_OS_X_64bit
    mv XMind_Linux{_64bit,}
%else
    rm -r XMind_Linux_64bit XMind_Windows XMind_Mac_OS_X_64bit
    # remove several files from Commons related to x86_64
    find -name *x86*64* | xargs rm -rf
%endif

#tweak paths in config file
sed -i "s@^\.\./Commons@%{_javadir}/%{name}@g" XMind_Linux/XMind.ini 


%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

cp -af ./Commons/* %{buildroot}%{_javadir}/%{name}
cp -af ./XMind_Linux/* %{buildroot}%{_datadir}/%{name}
cp -af %{SOURCE1} %{buildroot}%{_bindir}/%{name}
cp -af %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -af %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/%{name}.xml


cp -af %{SOURCE4} %{buildroot}/xmind.desktop
desktop-file-install                          \
--add-category="Office"                       \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}/xmind.desktop


%files
%defattr(-,root,root)
%doc *.txt *.html
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_javadir}/%{name}
%{_datadir}/%{name}


%changelog
* Tue Jan 14 2014 Tomas Tomecek <ttomecek@redhat.com> - 3.4.0-1
- rebase to 3.4.0


