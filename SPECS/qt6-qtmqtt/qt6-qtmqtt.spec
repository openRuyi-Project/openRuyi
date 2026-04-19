# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtmqtt
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtmqtt
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Mqtt module
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtmqtt
#!RemoteAsset:  sha256:4c0f246daa2009c8b3b9fb0172970fbb6452a0c2846ed5fe4de87ed4b884f9f9
Source0:        https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  qt6-qtbase-private-devel

%description
The Qt MQTT module provides a standard compliant implementation of the MQTT
protocol specification. It enables applications to act as telemetry displays
and devices to publish telemetry data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Network)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Mqtt.so.6*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtMqtt/
%{_qt6_libdir}/libQt6Mqtt.so
%{_qt6_libdir}/libQt6Mqtt.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMqttTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Mqtt/
%{_qt6_libdir}/cmake/Qt6MqttPrivate/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6Mqtt.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
