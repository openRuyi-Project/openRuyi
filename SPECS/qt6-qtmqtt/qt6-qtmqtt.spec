# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtmqtt
%define short_version 6.12

Name:           qt6-qtmqtt
Version:        6.12.0
Release:        %autorelease
Summary:        Qt6 - Mqtt module
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtmqtt
#!RemoteAsset:  sha256:55b2ac2938c6057aebd1df5366860d277ebda445f960111fba0998fedeced700
Source0:        https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake >= 3.16
BuildRequires:  ninja
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
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

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
