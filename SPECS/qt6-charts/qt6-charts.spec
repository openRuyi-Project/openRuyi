# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtcharts
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-charts
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Charts component
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtcharts
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
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  qt6-base-private-devel
BuildRequires:  qt6-declarative-devel >= %{version}
BuildRequires:  pkgconfig(xkbcommon)

%description
Qt Charts module provides a set of easy to use chart components. It uses the Qt Graphics View Framework, therefore charts can be easily
integrated to modern user interfaces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(Qt6Gui)
Requires:       pkgconfig(Qt6Widgets)
Requires:       pkgconfig(Qt6OpenGLWidgets)
Requires:       pkgconfig(Qt6OpenGL)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6Charts.so.6*
%{_qt6_libdir}/libQt6ChartsQml.so.6*
%{_qt6_qmldir}/QtCharts/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtCharts/
%{_qt6_includedir}/QtChartsQml/
%{_qt6_libdir}/libQt6Charts.so
%{_qt6_libdir}/libQt6Charts.prl
%{_qt6_libdir}/libQt6ChartsQml.so
%{_qt6_libdir}/libQt6ChartsQml.prl
%{_qt6_libdir}/cmake/Qt6Charts/
%{_qt6_libdir}/cmake/Qt6ChartsPrivate/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2*.cmake
%{_qt6_libdir}/cmake/Qt6ChartsQml/
%{_qt6_libdir}/cmake/Qt6ChartsQmlPrivate/
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%{?autochangelog}
