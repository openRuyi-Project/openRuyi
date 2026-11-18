# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtgraphs
%define short_version 6.12

Name:           qt6-qtgraphs
Version:        6.12.1
Release:        %autorelease
Summary:        The Qt Graphs module enables you to visualize data in 3D
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://doc.qt.io/qt-6/qtgraphs-index.html
VCS:            git:https://code.qt.io/qt/qtgraphs.git
#!RemoteAsset:  sha256:41bf52c13ab64e69037604187ba8d20463b9d1db292d8e2ad89e1be04a14298d
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DFEATURE_graphs_2d_high_quality_backend=ON
BuildOption(conf):  -DFEATURE_graphs_2d_high_performance_backend=ON

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
BuildRequires:  pkgconfig(Qt6Quick3D) >= %{version}
BuildRequires:  pkgconfig(Qt6CanvasPainter) >= %{version}

%description
The Qt Graphs module enables you to visualize data in 3D as bar,
scatter, and surface graphs. It's especially useful for visualizing
depth maps and large quantities of rapidly changing data.

%package        devel
Summary:        Development Files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Gui)
Requires:       pkgconfig(Qt6Quick)
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
%license LICENSES/*
%{_qt6_libdir}/libQt6Graphs.so.6*
%{_qt6_libdir}/libQt6Graphs2DImpl.so.6*
%{_qt6_libdir}/libQt6GraphsWidgets.so.6*
%{_qt6_qmldir}/QtGraphs/
%{_qt6_qmldir}/QtGraphs2D/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_includedir}/QtGraphs/
%{_qt6_includedir}/QtGraphs2DImpl/
%{_qt6_includedir}/QtGraphsWidgets/
%{_qt6_libdir}/libQt6Graphs.so
%{_qt6_libdir}/libQt6Graphs2DImpl.so
%{_qt6_libdir}/libQt6Graphs2DImpl.prl
%{_qt6_libdir}/libQt6Graphs.prl
%{_qt6_libdir}/libQt6GraphsWidgets.so
%{_qt6_libdir}/libQt6GraphsWidgets.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtGraphsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Graphs/
%{_qt6_libdir}/cmake/Qt6Graphs2DImpl/
%{_qt6_libdir}/cmake/Qt6GraphsPrivate/
%{_qt6_libdir}/cmake/Qt6GraphsWidgets/
%{_qt6_libdir}/cmake/Qt6GraphsWidgetsPrivate/
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6Graphsplugin*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphs2dimplplugin*.cmake
%{_qt6_libdir}/pkgconfig/Qt6Graphs.pc
%{_qt6_libdir}/pkgconfig/Qt6Graphs2DImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6GraphsWidgets.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_graphs*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
