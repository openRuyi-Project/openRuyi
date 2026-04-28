# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qt3d
%define real_version 6.10.1
%define short_version 6.10

%bcond system_assimp 0

Name:           qt6-qt3d
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Qt3D QML bindings and C++ APIs
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://code.qt.io/qt/qt3d.git
#!RemoteAsset:  sha256:60593fd54f7b1e48dc67ddce0f1113e4593878872539677104c92926ef039c9a
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON
%if %{with system_assimp}
BuildOption(conf):  -DFEATURE_qt3d_system_assimp=ON
%else
BuildOption(conf):  -DFEATURE_qt3d_system_assimp=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  qt6-qtbase-static >= %{version}
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6ShaderTools) >= %{version}
BuildRequires:  qt6-qtimageformats >= %{version}
%if %{with system_assimp}
BuildRequires:  pkgconfig(assimp) >= 5.0.0
%endif

%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Quick3D)

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
%{_qt6_libdir}/libQt63D*.so.6*
%{_qt6_pluginsdir}/geometryloaders/
%{_qt6_pluginsdir}/renderers/
%{_qt6_pluginsdir}/renderplugins/
%{_qt6_pluginsdir}/sceneparsers/
%{_qt6_qmldir}/Qt3D/
%{_qt6_qmldir}/QtQuick/Scene2D/
%{_qt6_qmldir}/QtQuick/Scene3D/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_libdir}/cmake/Qt63D*/
%{_qt6_includedir}/Qt3D*/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/cmake/Qt6/FindWrapQt3DAssimp.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/Qt3DTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/libQt63D*.prl
%{_qt6_libdir}/libQt63D*.so
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt63DAnimation.pc
%{_qt6_libdir}/pkgconfig/Qt63DCore.pc
%{_qt6_libdir}/pkgconfig/Qt63DExtras.pc
%{_qt6_libdir}/pkgconfig/Qt63DInput.pc
%{_qt6_libdir}/pkgconfig/Qt63DLogic.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuick.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickAnimation.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickExtras.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickInput.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickLogic.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickRender.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickScene2D.pc
%{_qt6_libdir}/pkgconfig/Qt63DQuickScene3D.pc
%{_qt6_libdir}/pkgconfig/Qt63DRender.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
