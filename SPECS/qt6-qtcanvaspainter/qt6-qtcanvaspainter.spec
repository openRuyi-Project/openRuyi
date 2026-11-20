# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtcanvaspainter
%define short_version 6.12

Name:           qt6-qtcanvaspainter
Version:        6.12.0
Release:        %autorelease
Summary:        Hardware-accelerated 2D painting for Qt
License:        GPL-3.0-only AND BSD-3-Clause AND Zlib AND OFL-1.1
URL:            https://doc.qt.io/qt-6/qtcanvaspainter-index.html
VCS:            git:https://code.qt.io/qt/qtcanvaspainter.git
#!RemoteAsset:  sha256:09c0747c3bef7c58e3154346ca5fe2702ab09f7ad4083243e6d20307245119e2
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_TESTS=ON
BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake >= 3.25
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  qt6-qtbase-private-devel >= %{version}
BuildRequires:  pkgconfig(Qt6Core) >= %{version}
BuildRequires:  pkgconfig(Qt6Test) >= %{version}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{version}
BuildRequires:  pkgconfig(Qt6Gui) >= %{version}
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(Qt6OpenGLWidgets) >= %{version}
BuildRequires:  qt6-qtshadertools-devel >= %{version}

%description
Qt Canvas Painter provides hardware-accelerated 2D painting for Qt Quick,
Qt Widgets and QRhi. It includes the QtCanvas2D QML module.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        examples
License:        BSD-3-Clause AND OFL-1.1
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%check -p
export QT_QPA_PLATFORM=offscreen

%files
%license LICENSES/BSD-3-Clause.txt LICENSES/GPL-3.0-only.txt LICENSES/Qt-GPL-exception-1.0.txt LICENSES/Zlib.txt
%{_qt6_libdir}/libQt6CanvasPainter.so.6*
%{_qt6_libdir}/libQt6Canvas2D.so.6*
%{_qt6_qmldir}/QtCanvas2D/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_bindir}/qcshadergen
%{_qt6_libdir}/libQt6CanvasPainter.so
%{_qt6_libdir}/libQt6CanvasPainter.prl
%{_qt6_libdir}/libQt6Canvas2D.so
%{_qt6_libdir}/libQt6Canvas2D.prl
%{_qt6_includedir}/QtCanvasPainter/
%{_qt6_includedir}/QtCanvas2D/
%{_qt6_libdir}/cmake/Qt6CanvasPainter*/
%{_qt6_libdir}/cmake/Qt6Canvas2DPrivate/
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/pkgconfig/Qt6CanvasPainter.pc
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json

%files examples
%license LICENSES/BSD-3-Clause.txt LICENSES/OFL-1.1.txt
%{_qt6_examplesdir}/

%changelog
%autochangelog
