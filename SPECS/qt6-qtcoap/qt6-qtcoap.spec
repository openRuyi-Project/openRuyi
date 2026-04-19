# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtcoap
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtcoap
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - CoAP component
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtcoap
#!RemoteAsset:  sha256:de077e00ef5a938ee3e86e093ca860e564dcdd00c13f62a8df98515a6a5cf782
Source0:        https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick)

%description
Qt CoAP (API) provides classes and functions to access the CoAP protocol.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Network)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Coap.so.*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtCoap/
%{_qt6_libdir}/libQt6Coap.so
%{_qt6_libdir}/libQt6Coap.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtCoapTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Coap/
%{_qt6_libdir}/cmake/Qt6CoapPrivate/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Coap.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
