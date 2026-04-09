# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kdsoap-ws-discovery-client
Version:        0.4.0
Release:        %autorelease
Summary:        Library for finding WS-Discovery devices in the network
License:        GPL-3.0-or-later
URL:            https://invent.kde.org/libraries/kdsoap-ws-discovery-client/
#!RemoteAsset:  sha256:2cd247c013e75f410659bac372aff93d22d71c5a54c059e137b9444af8b3427a
Source0:        https://download.kde.org/Attic/kdsoap-ws-discovery-client/kdsoap-ws-discovery-client-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WITH_QT6=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(Qt6)
BuildRequires:  qt6-macros

%description
Library for finding WS-Discovery devices in the network using Qt6 and KDSoap.

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KDSoap-qt6)

%description    devel
Development files for %{name}.

%check
# skip tests as obs has no internet.

%files
%doc README.md
%license LICENSES/*
%{_libdir}/libKDSoapWSDiscoveryClient.so.0*

%files devel
%{_includedir}/KDSoapWSDiscoveryClient/
%{_libdir}/cmake/KDSoapWSDiscoveryClient/
%{_libdir}/libKDSoapWSDiscoveryClient.so

%changelog
%autochangelog
