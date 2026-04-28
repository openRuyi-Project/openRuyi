# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtsvg
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtsvg
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Support for rendering and displaying SVG
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://code.qt.io/qt/qtsvg.git
#!RemoteAsset:  sha256:c02f355a58f3bbcf404a628bf488b6aeb2d84a94c269afdb86f6e529343ab01f
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xkbcommon)

%description
Scalable Vector Graphics (SVG) is an XML-based language for describing
two-dimensional vector graphics. Qt provides classes for rendering and
displaying SVG drawings in widgets and on other paint devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
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
%{_qt6_libdir}/libQt6Svg.so.6*
%{_qt6_libdir}/libQt6SvgWidgets.so.6*
%{_qt6_pluginsdir}/iconengines/libqsvgicon.so
%{_qt6_pluginsdir}/imageformats/libqsvg.so

%files devel
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_includedir}/QtSvg/
%{_qt6_includedir}/QtSvgWidgets/
%{_qt6_libdir}/libQt6Svg.so
%{_qt6_libdir}/libQt6Svg.prl
%{_qt6_libdir}/libQt6SvgWidgets.so
%{_qt6_libdir}/libQt6SvgWidgets.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake
%{_qt6_libdir}/cmake/Qt6Svg/
%{_qt6_libdir}/cmake/Qt6SvgPrivate/
%{_qt6_libdir}/cmake/Qt6SvgWidgets/
%{_qt6_descriptionsdir}/*.json
%{_qt6_metatypesdir}/*.json
%{_qt6_libdir}/pkgconfig/Qt6Svg.pc
%{_qt6_libdir}/pkgconfig/Qt6SvgWidgets.pc
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
