# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtwayland
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtwayland
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Wayland platform support and QtCompositor module
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtwayland
#!RemoteAsset:  sha256:49bf6db800227a6b2c971f4c5d03dd1e81297e7ffb296ce4a96437304f27cb13
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

# fix cmake error by set prefix.
Patch0:         0001-set-prefix.patch

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  wayland-protocols

BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xext)

%description
Qt Wayland provides the Wayland platform plugin for Qt applications and the
QtCompositor module for creating Wayland compositors.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Quick)

%description    devel
Development files for %{name}.

%package        adwaita-decoration
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    adwaita-decoration
Qt decoration plugin implementing Adwaita-like client-side decorations.

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
%doc README
%license LICENSES/*
%{_qt6_libdir}/libQt6WaylandCompositor.so.6*
%{_qt6_libdir}/libQt6WaylandCompositorIviapplication.so.6*
%{_qt6_libdir}/libQt6WaylandCompositorPresentationTime.so.6*
%{_qt6_libdir}/libQt6WaylandCompositorWLShell.so.6*
%{_qt6_libdir}/libQt6WaylandCompositorXdgShell.so.6*
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so.6*
%{_qt6_pluginsdir}/wayland-graphics-integration-server/
%{_qt6_pluginsdir}/wayland-shell-integration/
%{_qt6_qmldir}/QtWayland/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtWaylandCompositor/
%{_qt6_includedir}/QtWaylandCompositorIviapplication/
%{_qt6_includedir}/QtWaylandCompositorPresentationTime/
%{_qt6_includedir}/QtWaylandCompositorWLShell/
%{_qt6_includedir}/QtWaylandCompositorXdgShell/
%{_qt6_includedir}/QtWaylandEglCompositorHwIntegration/
%{_qt6_libdir}/libQt6WaylandCompositor.so
%{_qt6_libdir}/libQt6WaylandCompositorIviapplication.prl
%{_qt6_libdir}/libQt6WaylandCompositorIviapplication.so
%{_qt6_libdir}/libQt6WaylandCompositorPresentationTime.prl
%{_qt6_libdir}/libQt6WaylandCompositorPresentationTime.so
%{_qt6_libdir}/libQt6WaylandCompositorWLShell.prl
%{_qt6_libdir}/libQt6WaylandCompositorWLShell.so
%{_qt6_libdir}/libQt6WaylandCompositorXdgShell.prl
%{_qt6_libdir}/libQt6WaylandCompositorXdgShell.so
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.so
%{_qt6_libdir}/libQt6WaylandCompositor.prl
%{_qt6_libdir}/libQt6WaylandEglCompositorHwIntegration.prl
%{_qt6_libdir}/cmake/Qt6WaylandCompositor/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/cmake/Qt6WaylandClientFeaturesPrivate/
%{_qt6_libdir}/cmake/Qt6WaylandCompositorIviapplication/
%{_qt6_libdir}/cmake/Qt6WaylandCompositorIviapplicationPrivate
%{_qt6_libdir}/cmake/Qt6WaylandCompositorPresentationTime/
%{_qt6_libdir}/cmake/Qt6WaylandCompositorPresentationTimePrivate
%{_qt6_libdir}/cmake/Qt6WaylandCompositorPrivate
%{_qt6_libdir}/cmake/Qt6WaylandCompositorWLShell/
%{_qt6_libdir}/cmake/Qt6WaylandCompositorWLShellPrivate
%{_qt6_libdir}/cmake/Qt6WaylandCompositorXdgShell/
%{_qt6_libdir}/cmake/Qt6WaylandCompositorXdgShellPrivate
%{_qt6_libdir}/cmake/Qt6WaylandEglCompositorHwIntegrationPrivate/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWaylandTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6WaylandClient/*.cmake
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6WaylandCompositor.pc
%{_qt6_libdir}/pkgconfig/Qt6WaylandCompositorIviapplication.pc
%{_qt6_libdir}/pkgconfig/Qt6WaylandCompositorPresentationTime.pc
%{_qt6_libdir}/pkgconfig/Qt6WaylandCompositorWLShell.pc
%{_qt6_libdir}/pkgconfig/Qt6WaylandCompositorXdgShell.pc
%exclude %{_qt6_libdir}/cmake/Qt6WaylandClient/Qt6QWaylandAdwaitaDecoration*.cmake

%files adwaita-decoration
%{_qt6_pluginsdir}/wayland-decoration-client/libadwaita.so
%{_qt6_libdir}/cmake/Qt6WaylandClient/Qt6QWaylandAdwaitaDecoration*.cmake

%files examples
%{_qt6_examplesdir}/wayland/

%changelog
%autochangelog
