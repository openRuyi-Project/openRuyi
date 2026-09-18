# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libjaylink
Version:        0.5.0
Release:        %autorelease
Summary:        A library to access SEGGER J-Link and compatible devices
# Note: future versions of libjaylink changed to LGPL-2.1-or-later
License:        GPL-2.0-or-later
URL:            https://gitlab.zapb.de/libjaylink/libjaylink
VCS:            git:https://gitlab.zapb.de/libjaylink/libjaylink
#!RemoteAsset:  sha256:235b12d161b29d813026704f335536a6a916646ea2058302e4ca45ca2cd81325
Source:         https://gitlab.zapb.de/%{name}/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(bash-completion)

Requires:       libusb

%description
%{name} is a shared library written in C to access SEGGER J-Link and compatible devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%files
%{_libdir}/libjaylink.so.0.2.2
%{_libdir}/libjaylink.so.0

%files devel
%{_includedir}/%{name}/version.h
%{_includedir}/%{name}/libjaylink.h
%{_libdir}/pkgconfig/libjaylink.pc
%{_libdir}/libjaylink.so

%changelog
%autochangelog
