# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define rname kwayland

Name:           kwayland6
Version:        6.7.4
Release:        %autorelease
Summary:        KDE Wayland library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kwayland
#!RemoteAsset:  sha256:2cb3ad260a0fc07533b1e0e9e294da2ec9be83095a901140e9fab16fa17a550d
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_QCH:BOOL=TRUE

BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  xcb-util
BuildRequires:  qt6-qtbase-gui >= %{qt6_version}
BuildRequires:  qt6-doctools
BuildRequires:  qt6-qtwayland-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.21.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandGlobalPrivate) >= %{qt6_version}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client) >= 1.15.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15.0
BuildRequires:  pkgconfig(wayland-server) >= 1.15.0

%description
KWayland provides a Qt-style Client and Server library wrapper for the Wayland
libraries.

%package        devel
Summary:        KDE Wayland library: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KWayland provides a Qt-style Client and Server library wrapper for the Wayland
libraries.

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kwayland.categories
%{_kf6_debugdir}/kwayland.renamecategories
%{_kf6_libdir}/libKWaylandClient.so.*

%files devel
%doc %{_kf6_qchdir}/KWayland.*
%{_includedir}/KWayland/
%{_kf6_cmakedir}/KWayland/
%{_kf6_libdir}/libKWaylandClient.so
%{_kf6_pkgconfigdir}/KWaylandClient.pc

%changelog
%autochangelog
