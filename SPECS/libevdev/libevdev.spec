# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libevdev
Version:        1.13.5
Release:        %autorelease
Summary:        A wrapper library for evdev devices
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/libevdev/
VCS:            git:https://gitlab.freedesktop.org/libevdev/libevdev
#!RemoteAsset
Source:         https://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-gcov

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python

%description
Library for handling evdev kernel devices. It abstracts the ioctls through typ
e-safe interfaces and provides functions to change the appearance of the devic
e, shipping both the shared libraries and helper utilities.

%package        devel
Summary:        Development files for the libevdev library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libevdev.

%files
%license COPYING
%{_libdir}/libevdev.so.*
%{_bindir}/mouse-dpi-tool
%{_bindir}/libevdev-tweak-device
%{_bindir}/touchpad-edge-detector
%{_mandir}/man3/libevdev.*
%{_mandir}/man1/libevdev-tweak-device.1*
%{_mandir}/man1/mouse-dpi-tool.1*
%{_mandir}/man1/touchpad-edge-detector.1*

%files devel
%{_libdir}/libevdev.so
%{_includedir}/libevdev-1.0/
%{_libdir}/pkgconfig/libevdev.pc

%changelog
%autochangelog
