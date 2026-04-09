# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           phonon
Version:        4.12.0
Release:        %autorelease
Summary:        Multimedia framework api
License:        LGPL-2.1-or-later
URL:            https://community.kde.org/Phonon
VCS:            git:https://invent.kde.org/libraries/phonon
#!RemoteAsset:  sha256:3287ffe0fbcc2d4aa1363f9e15747302d0b080090fe76e5f211d809ecb43f39a
Source0:        https://download.kde.org/stable/phonon/%{version}/phonon-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DPHONON_BUILD_QT5=OFF
BuildOption(conf):  -DPHONON_BUILD_QT6=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)

%description
Phonon is the multimedia API for KDE 4. This package contains the Qt 6
bindings.

%package        qt6-devel
Summary:        Developer files for %{name}-qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    qt6-devel
Developer files for %{name}-qt6.

%install -a
mkdir -p %{buildroot}%{_qt6_pluginsdir}/phonon4qt6_backend
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license COPYING.LIB
%{_bindir}/phononsettings
%{_libdir}/libphonon4qt6.so.4*
%{_libdir}/libphonon4qt6experimental.so.4*
%{_qt6_pluginsdir}/designer/phonon4qt6widgets.so
%dir %{_qt6_pluginsdir}/phonon4qt6_backend/

%files qt6-devel
%{_libdir}/cmake/phonon4qt6/
%{_includedir}/phonon4qt6/
%{_libdir}/libphonon4qt6.so
%{_libdir}/libphonon4qt6experimental.so
%{_libdir}/pkgconfig/phonon4qt6.pc

%changelog
%autochangelog
