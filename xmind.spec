%define __jar_repack 0

#%%define version_suffix 201504270119

Name:       xmind
Version:    3.7.8
Release:    1%{?dist}
Summary:    Brainstorming and Mind Mapping
Group:      Applications/Productivity
License:    EPL or LGPLv3
URL:        http://www.xmind.net
Source0:    https://www.xmind.net/xmind/downloads/%{name}-8-update8-linux.zip
Source1:    xmind.sh
Source2:    xmind.png
Source3:    xmind.xml
Source4:    xmind.desktop
ExcludeArch:ppc ppc64 arm s390x sparc
BuildRequires: unzip
BuildRequires: desktop-file-utils
BuildRequires: chrpath
BuildRequires: java-devel
AutoReqProv: no
Requires: java = 1.8
Requires: gtk2
Requires: lame
Requires: glib2


%description
XMind is an open source project that contributes to building a cutting-edge brainstorming/mind-mapping facility, focused on both usability and extendability. It helps people in capturing ideas into visually self-organized charts and sharing them for collaboration and communication. Currently supporting mind maps, fishbone diagrams, tree diagrams, org-charts, logic charts, and even spreadsheets. Often used for knowledge management, meeting minutes, task management, and GTD. 

%prep
%setup -q -c

%ifarch x86_64
    mv XMind{_amd64,}
%else
    mv XMind{_i386,}
%endif

#tweak paths in config file
sed -i "s@^\.\./plugins@%{_javadir}/%{name}/plugins@g" XMind/XMind.ini


%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/icons/gnome/48x48/mimetypes

cp -af ./configuration %{buildroot}%{_javadir}/%{name}
cp -af ./features %{buildroot}%{_javadir}/%{name}
cp -af ./fonts %{buildroot}%{_javadir}/%{name}
cp -af ./plugins %{buildroot}%{_javadir}/%{name}
cp -af ./XMind/* %{buildroot}%{_datadir}/%{name}
cp -af %{SOURCE1} %{buildroot}%{_bindir}/%{name}
cp -af %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -af %{SOURCE2} %{buildroot}%{_datadir}/icons/gnome/48x48/mimetypes/application-%{name}.png
cp -af %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

cp -af %{SOURCE4} %{buildroot}/xmind.desktop
desktop-file-install                          \
--add-category="Office"                       \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}/xmind.desktop


%post
/usr/bin/update-desktop-database &> /dev/null || :
/usr/bin/update-mime-database %{?rhel:-n} %{_datadir}/mime &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/gnome &>/dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/gnome &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/gnome &>/dev/null || :
fi


%files
%defattr(-,root,root)
%doc readme.txt
%license xpla.txt lgpl-3.0.html epl-v10.html
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/gnome/48x48/mimetypes/application-%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_javadir}/%{name}
%{_datadir}/%{name}


%changelog
* Tue Aug 14 2018 Tomas Hozza <thozza@redhat.com> - 3.7.8-1
- Update to 3.7.8
- Clean up SPEC from unused code
- Update Requires based on setup.sh script from upstream

* Tue Aug 14 2018 Tomas Hozza <thozza@redhat.com> - 3.6.51-2
- Added some changes from Oliver Haessler made in RHEL-7 CSB

* Fri Sep 16 2016 Tomas Tomecek <ttomecek@redhat.com> - 3.6.51-1
- 3.6.51 update

* Tue Mar 08 2016 Tomas Tomecek <ttomecek@redhat.com> - 3.6.1-1
- 3.6.1 update

* Fri Aug 15 2014 Tomas Hozza <thozza@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Tue Jan 14 2014 Tomas Tomecek <ttomecek@redhat.com> - 3.4.0-1
- rebase to 3.4.0


