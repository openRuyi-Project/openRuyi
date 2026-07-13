# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kdnssd
# Full KF6 version (e.g. 6.23.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kdnssd
Version:        6.27.0
Release:        %autorelease
Summary:        Network service discovery using Zeroconf
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kdnssd.git
#!RemoteAsset:  sha256:a60746aca1ce6cfd2fbd20144bc4869d2b00d04b597aedab3dd37a345fb03bb4
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  avahi-devel
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

%package        devel
Summary:        Network service discovery using Zeroconf
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of Zeroconf that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure. Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --without-mo --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libKF6DNSSD.so.*

%files devel
%{_kf6_cmakedir}/KF6DNSSD/
%{_kf6_includedir}/KDNSSD/
%{_kf6_libdir}/libKF6DNSSD.so

%changelog
%autochangelog
