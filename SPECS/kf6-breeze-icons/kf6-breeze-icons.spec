# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname breeze-icons
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

%define _lto_cflags %{nil}

Name:           kf6-breeze-icons
Version:        6.28.0
Release:        %autorelease
Summary:        Breeze icon theme
License:        LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/breeze-icons
#!RemoteAsset:  sha256:45de8138ead0f3ff24de886fbe61d588ecd7f66dde6f8cf6f2906279254d094d
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBINARY_ICONS_RESOURCE:BOOL=TRUE
BuildOption(conf):  -DWITH_ICON_GENERATION:BOOL=FALSE

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  libxml2
# Skip 24px icons generation (saves ~30MB and installs dangling symlinks)
# BuildRequires:  python3 python3-lxml
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}

%description
Breeze-icons is a freedesktop.org compatible icon theme.

%package        rcc
Summary:        Breeze icon theme - rcc file

%description    rcc
Breeze-icons is a freedesktop.org compatible icon theme.
This contains the Breeze (non-dark) icons in a QResource file, used by Kexi.

%package        devel
Summary:        CMake config files for kf6-breeze-icons
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides CMake config files for projects that wish to ensure
the Breeze icons are available at build time.

%install -a
# yast2-theme uses these, but it got renamed in 5.55.0
ln -s yast-software-group.svg %{buildroot}%{_kf6_iconsdir}/breeze/preferences/32/yast-software.svg

%files
%license COPYING*
%ghost %{_kf6_iconsdir}/breeze/icon-theme.cache
%ghost %{_kf6_iconsdir}/breeze-dark/icon-theme.cache
%exclude %{_kf6_iconsdir}/breeze/breeze-icons.rcc
%exclude %{_kf6_iconsdir}/breeze-dark/breeze-icons-dark.rcc
%{_kf6_iconsdir}/breeze/
%{_kf6_iconsdir}/breeze-dark/
%{_kf6_libdir}/libKF6BreezeIcons.so.*

%files rcc
%dir %{_kf6_iconsdir}/breeze
# Kexi does not need the -dark variant.
%{_kf6_iconsdir}/breeze/breeze-icons.rcc
# No dark rcc built/installed in this config

%files devel
%{_kf6_cmakedir}/KF6BreezeIcons/
%{_kf6_includedir}/BreezeIcons/
%{_kf6_libdir}/libKF6BreezeIcons.so

%changelog
%autochangelog
