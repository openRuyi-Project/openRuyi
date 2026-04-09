# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openal-soft
Version:        1.25.1
Release:        %autorelease
Summary:        Software implementation of the OpenAL 3D audio API
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
#!RemoteAsset:  sha256:4c2aff6f81975f46ecc5148d092c4948c71dbfb76e4b9ba4bf1fce287f47d4b5
Source0:        https://openal-soft.org/openal-releases/openal-soft-%{version}.tar.bz2
BuildSystem:    cmake

BuildOption(conf):  -DALSOFT_CPUEXT_NEON=OFF
BuildOption(conf):  -DALSOFT_INSTALL_CONFIG=ON
BuildOption(conf):  -DALSOFT_INSTALL_HRTF_DATA=ON
BuildOption(conf):  -DALSOFT_EXAMPLES=ON
BuildOption(conf):  -DALSOFT_INSTALL_EXAMPLES=ON
BuildOption(conf):  -DALSOFT_UTILS=ON
BuildOption(conf):  -DALSOFT_INSTALL_UTILS=ON
BuildOption(conf):  -DALSOFT_NO_CONFIG_UTIL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(sndfile)

%description
OpenAL Soft is an LGPL-licensed, cross-platform, software implementation of the
OpenAL 3D audio API. It provides capabilities for playing audio in a virtual
3D environment.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for openal-soft.

%install -a
install -D -p -m 0644 alsoftrc.sample %{buildroot}%{_sysconfdir}/openal/alsoft.conf

%files
%doc README.md ChangeLog
%dir %{_sysconfdir}/openal
%config(noreplace) %{_sysconfdir}/openal/alsoft.conf
%{_libdir}/libopenal.so.1*
%{_datadir}/openal/
%exclude %{_datadir}/openal/alsoftrc.sample
%exclude %{_datadir}/openal/presets/presets.txt
%{_bindir}/openal-info
%{_bindir}/alsoft-config
%{_bindir}/aldebug
%{_bindir}/aldirect
%{_bindir}/alhrtf
%{_bindir}/allafplay
%{_bindir}/allatency
%{_bindir}/almultireverb
%{_bindir}/alplay
%{_bindir}/alrecord
%{_bindir}/alreverb
%{_bindir}/alstream
%{_bindir}/altonegen

%files devel
%{_includedir}/AL/
%{_libdir}/cmake/OpenAL/
%{_libdir}/libopenal.so
%{_libdir}/pkgconfig/openal.pc

%changelog
%autochangelog
