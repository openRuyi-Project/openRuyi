# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define _sover 6

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           kpipewire
Version:        6.7.1
Release:        %autorelease
Summary:        PipeWire integration for KDE Plasma
License:        LGPL-2.0-only AND LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kpipewire.git
#!RemoteAsset:  sha256:a29b6d8614683038e98fbc696f78dd5137cb642abcddb73781f8d0796fc4c014
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6_version}
BuildRequires:  cmake(Qt6QmlIntegration) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)

%description
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.

%package        devel
Summary:        Development files for kpipewire
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6QmlIntegration) >= %{qt6_version}
Requires:       pkgconfig(epoxy)
Requires:       pkgconfig(libpipewire-0.3)

%description    devel
KPipeWire provides PipeWire integration for the Plasma desktop and mobile shells.
This package provides the development files needed to build applications
which use KPipeWire.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libKPipeWire.so.*
%{_kf6_debugdir}/kpipewire.categories
%{_kf6_libdir}/libKPipeWireRecord.so.*
%{_kf6_debugdir}/kpipewirerecord.categories
%{_kf6_libdir}/libKPipeWireDmaBuf.so.*
%{_kf6_qmldir}/org/kde/pipewire/

%files devel
%{_includedir}/KPipeWire/
%{_kf6_cmakedir}/KPipeWire/
%{_kf6_libdir}/libKPipeWire.so
%{_kf6_libdir}/libKPipeWireRecord.so
%{_kf6_libdir}/libKPipeWireDmaBuf.so

%changelog
%autochangelog
