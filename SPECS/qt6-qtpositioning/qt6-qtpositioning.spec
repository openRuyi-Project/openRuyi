# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtpositioning
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtpositioning
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Positioning component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtpositioning
#!RemoteAsset:  sha256:abb311ef1bd6e39f090d22480e265d13f8537d2e2f4c88f22d6519547f46be23
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6SerialPort) >= %{version}
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0

%description
The Qt Positioning APIs gives developers the ability to determine a position
by using a variety of possible sources, including satellite, or wifi, or
text file, and so on.

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
%{_qt6_libdir}/libQt6Positioning.so.6*
%{_qt6_libdir}/libQt6PositioningQuick.so.6*
%{_qt6_pluginsdir}/position/
%{_qt6_qmldir}/QtPositioning/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtPositioning/
%{_qt6_includedir}/QtPositioningQuick/
%{_qt6_libdir}/libQt6Positioning.so
%{_qt6_libdir}/libQt6Positioning.prl
%{_qt6_libdir}/libQt6PositioningQuick.so
%{_qt6_libdir}/libQt6PositioningQuick.prl
%{_qt6_libdir}/cmake/Qt6Positioning/
%{_qt6_libdir}/cmake/Qt6PositioningPrivate/
%{_qt6_libdir}/cmake/Qt6PositioningQuick/
%{_qt6_libdir}/cmake/Qt6PositioningQuickPrivate/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Positioning.pc
%{_qt6_libdir}/pkgconfig/Qt6PositioningQuick.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
