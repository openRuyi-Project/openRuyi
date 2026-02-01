# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           polkit-qt
Version:        0.200.0
Release:        %autorelease
Summary:        Qt 6 bindings for PolicyKit
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/polkit-qt-1
#!RemoteAsset:  sha256:5d3b611c062d2b76a93750bb10c907bfd21d1ff08d0a15dc2cf63e278e1677fb
Source0:        https://download.kde.org/stable/polkit-qt-1/polkit-qt-1-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_EXAMPLES=OFF
BuildOption(conf):  -DQT_MAJOR_VERSION=6

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package        devel
Summary:        Development files for PolicyKit Qt bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for PolicyKit Qt bindings.

%files
%license LICENSES/*
%doc AUTHORS README
%{_libdir}/libpolkit-qt6-core-1.so.1*
%{_libdir}/libpolkit-qt6-gui-1.so.1*
%{_libdir}/libpolkit-qt6-agent-1.so.1*

%files devel
%{_includedir}/polkit-qt6-1/
%{_libdir}/libpolkit-qt6-core-1.so
%{_libdir}/libpolkit-qt6-gui-1.so
%{_libdir}/libpolkit-qt6-agent-1.so
%{_libdir}/pkgconfig/polkit-qt6-1.pc
%{_libdir}/pkgconfig/polkit-qt6-core-1.pc
%{_libdir}/pkgconfig/polkit-qt6-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt6-agent-1.pc
%{_libdir}/cmake/PolkitQt6-1/

%changelog
%{?autochangelog}
