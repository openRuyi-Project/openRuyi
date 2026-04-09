# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtserialbus
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtserialbus
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - SerialBus component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtserialbus
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6SerialPort) >= %{version}
BuildRequires:  pkgconfig(openssl)

%description
Qt Serial Bus (API) provides classes and functions to access the various
industrial serial buses and protocols, such as CAN, ModBus, and others.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Network)
Requires:       pkgconfig(Qt6SerialPort)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6SerialBus.so.6*
%{_qt6_bindir}/canbusutil
%{_qt6_pluginsdir}/canbus/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtSerialBus/
%{_qt6_libdir}/libQt6SerialBus.so
%{_qt6_libdir}/libQt6SerialBus.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSerialBusTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6SerialBus/
%{_qt6_libdir}/cmake/Qt6SerialBusPrivate/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6SerialBus.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
