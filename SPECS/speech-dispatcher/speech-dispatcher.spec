# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           speech-dispatcher
Version:        0.12.1
Release:        %autorelease
Summary:        To provide a high-level device independent layer for speech synthesis
License:        GPL-2.0-or-later AND LGPL-2.1-only
URL:            https://github.com/brailcom/speechd
#!RemoteAsset:  sha256:b14a5238d287d2dcce4dd42bbd66ca65fa228e7e683708267f7b34036f7ba4b4
Source0:        https://github.com/brailcom/speechd/releases/download/%{version}/speech-dispatcher-%{version}.tar.gz
BuildSystem:    autotools

# skip gen man.
Patch0:         0001-disable-man.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-alsa
BuildOption(conf):  --with-pulse
BuildOption(conf):  --with-libao=no
BuildOption(conf):  --with-espeak-ng=no
BuildOption(conf):  --without-oss
BuildOption(conf):  --without-nas
BuildOption(conf):  --without-espeak
BuildOption(conf):  --with-kali=no
BuildOption(conf):  --with-baratinoo=no
BuildOption(conf):  --with-ibmtts=no
BuildOption(conf):  --with-voxin=no
BuildOption(conf):  --sysconfdir=%{_sysconfdir}
BuildOption(conf):  --with-default-audio-method=pulse
BuildOption(conf):  --with-module-bindir=%{_libdir}/speech-dispatcher-modules/
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --with-systemduserunitdir=%{_prefix}/lib/systemd/user/
BuildOption(conf):  --disable-help2man
BuildOption(conf):  --with-flite

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pulseaudio-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(dotconf)
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  texinfo
BuildRequires:  flite-devel

Requires:       python3-speechd = %{version}-%{release}

%description
Common interface to different TTS engines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for speech-dispatcher.

%package     -n python-speechd
Summary:        Python 3 Client API for speech-dispatcher
Provides:       python3-speechd
%python_provide python3-speechd

%description -n python-speechd
Python 3 module for speech-dispatcher.

%install -a
# install -p -m 0644 sound-icons-0.1/* %{buildroot}%{_datadir}/sounds/%{name}/

# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

#Remove %{_infodir}/dir file
rm -f %{buildroot}%{_infodir}/dir

# Move the config files from /usr/share to /etc
mkdir -p %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
mkdir -p %{buildroot}%{_sysconfdir}/speech-dispatcher/modules
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/speechd.conf %{buildroot}%{_sysconfdir}/speech-dispatcher/
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/clients/* %{buildroot}%{_sysconfdir}/speech-dispatcher/clients/
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/modules/* %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/

# Create log dir
mkdir -p -m 0700 %{buildroot}%{_localstatedir}/log/speech-dispatcher/

# Verify the desktop files
desktop-file-validate %{buildroot}%{_datadir}/speech-dispatcher/conf/desktop/speechd.desktop

%post
%systemd_post speech-dispatcherd.service

%preun
%systemd_preun speech-dispatcherd.service

%postun
%systemd_postun_with_restart speech-dispatcherd.service

%files -f %{name}.lang
%license COPYING.LGPL
%doc NEWS README.md
%dir %{_sysconfdir}/speech-dispatcher/
%dir %{_sysconfdir}/speech-dispatcher/clients
%dir %{_sysconfdir}/speech-dispatcher/modules
%config(noreplace) %{_sysconfdir}/speech-dispatcher/speechd.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/clients/*.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/*.conf
%{_bindir}/speech-dispatcher
%{_datadir}/speech-dispatcher/
%dir %{_libdir}/speech-dispatcher-modules/
%{_libdir}/speech-dispatcher-modules/sd_cicero
%{_libdir}/speech-dispatcher-modules/sd_dummy
%{_libdir}/speech-dispatcher-modules/sd_generic
%{_libdir}/speech-dispatcher-modules/sd_openjtalk
%{_libdir}/speech-dispatcher-modules/sd_festival
%dir %{_libdir}/speech-dispatcher
%{_libdir}/speech-dispatcher/spd*.so
%{_datadir}/sounds/speech-dispatcher
%{_mandir}/man1/speech-dispatcher.1*
%dir %attr(0700, root, root) %{_localstatedir}/log/speech-dispatcher/
%{_unitdir}/speech-dispatcherd.service
%{_prefix}/lib/systemd/user/speech-dispatcher.service
%{_prefix}/lib/systemd/user/speech-dispatcher.socket
%{_libdir}/libspeechd.so.2*
%{_libdir}/libspeechd_module.so.0*
%{_infodir}/*
%{_bindir}/spd-conf
%{_bindir}/spd-say
%{_bindir}/spdsend
%{_mandir}/man1/spd-say.1*
%{_libdir}/speech-dispatcher-modules/sd_flite

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/speech-dispatcher.pc

%files -n python-speechd
%{python3_sitearch}/speechd*

%changelog
%autochangelog
