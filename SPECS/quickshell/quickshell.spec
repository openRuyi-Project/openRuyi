# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.10.0

%bcond tests 1
%bcond crash_handler 0

Name:           quickshell
Version:        0.3.0
Release:        %autorelease
Summary:        QtQuick-based desktop shell toolkit
License:        LGPL-3.0-only
URL:            https://quickshell.outfoxxed.me
VCS:            git:https://git.outfoxxed.me/quickshell/quickshell.git
#!RemoteAsset:  sha256:f4821f9084cab04bd2b5384cc92b9726aecc4ce3eb27200dca24edc67da3b6e5
Source0:        https://git.outfoxxed.me/quickshell/quickshell/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DBUILD_SHARED_LIBS=OFF
BuildOption(conf):  -DDISTRIBUTOR=%{_vendor_name}
BuildOption(conf):  -DINSTALL_QMLDIR=%{_qt6_qmldir}
BuildOption(conf):  -DNO_PCH=ON
%if %{with tests}
BuildOption(conf):  -DBUILD_TESTING=ON
%else
BuildOption(conf):  -DBUILD_TESTING=OFF
%endif
%if %{with crash_handler}
BuildOption(conf):  -DCRASH_HANDLER=ON
%else
BuildOption(conf):  -DCRASH_HANDLER=OFF
%endif
BuildOption(conf):  -DUSE_JEMALLOC=OFF
BuildOption(conf):  -DWAYLAND=ON
BuildOption(conf):  -DSCREENCOPY=ON
BuildOption(conf):  -DX11=ON
BuildOption(conf):  -DSERVICE_PIPEWIRE=ON
BuildOption(conf):  -DSERVICE_PAM=ON
BuildOption(conf):  -DSERVICE_POLKIT=ON
BuildOption(conf):  -DHYPRLAND=ON
BuildOption(conf):  -DI3=ON
# no wm
BuildOption(check):  --exclude-regex '^popupwindow$'

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  qt6-macros
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qtdeclarative-private-devel >= %{qt6_version}
BuildRequires:  cmake(CLI11)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  qt6-qtwayland-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
%if %{with tests}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%endif
%if %{with crash_handler}
# BuildRequires:  cpptrace-devel
# BuildRequires:  libunwind-devel
%endif

Requires:       qt6-qtdeclarative >= %{qt6_version}
Requires:       qt6-qtsvg >= %{qt6_version}
Provides:       quick-shell = %{version}-%{release}

%description
Quickshell is a QtQuick-based toolkit for building desktop shell components
and Wayland or X11 compositor integrations.

%check -p
export QT_QPA_PLATFORM=offscreen

%files
%doc README.md BUILD.md changelog/
%license LICENSE LICENSE-GPL
%{_bindir}/quickshell
%{_bindir}/qs
%{_datadir}/applications/org.quickshell.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.quickshell.svg
%{_qt6_qmldir}/Quickshell/

%changelog
%autochangelog
