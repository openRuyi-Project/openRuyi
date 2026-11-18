# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtsensors
%define short_version 6.12

Name:           qt6-qtsensors
Version:        6.12.0
Release:        %autorelease
Summary:        Qt6 - Sensors component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtsensors
#!RemoteAsset:  sha256:861df58be8808cef777a1b531d7bec804d25733ec34e8ebbdafbe27040319090
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6Svg) >= %{version}
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(openssl)

%description
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces. The Qt Sensors API also provides a motion gesture recognition
API for devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_libdir}/libQt6Sensors.so.6*
%{_qt6_libdir}/libQt6SensorsQuick.so.6*
%{_qt6_pluginsdir}/sensors/
%{_qt6_qmldir}/QtSensors/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_includedir}/QtSensors/
%{_qt6_includedir}/QtSensorsQuick/
%{_qt6_libdir}/libQt6Sensors.so
%{_qt6_libdir}/libQt6Sensors.prl
%{_qt6_libdir}/libQt6SensorsQuick.prl
%{_qt6_libdir}/libQt6SensorsQuick.so
%{_qt6_libdir}/cmake/Qt6/FindSensorfw.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Sensors/
%{_qt6_libdir}/cmake/Qt6SensorsPrivate/
%{_qt6_libdir}/cmake/Qt6SensorsQuick/
%{_qt6_libdir}/cmake/Qt6SensorsQuickPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_sensors*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Sensors.pc
%{_qt6_libdir}/pkgconfig/Qt6SensorsQuick.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
