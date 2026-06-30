# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfm-qt
Version:        2.4.0
Release:        %autorelease
Summary:        Qt library for file manager development
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/lxqt/libfm-qt
VCS:            git:https://github.com/lxqt/libfm-qt.git
#!RemoteAsset:  sha256:72766d7b41fd1aa06c0a7ef8be015205506ff75963b977e5307994555dcc023b
Source0:        https://github.com/lxqt/libfm-qt/releases/download/%{version}/libfm-qt-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6LinguistTools) >= 6.6.0
BuildRequires:  cmake(Qt6Widgets) >= 6.6.0
BuildRequires:  cmake(lxqt-menu-data) >= 2.4.0
BuildRequires:  cmake(lxqt2-build-tools) >= 2.4.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.50.0
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache) >= 1.1.0
BuildRequires:  pkgconfig(xcb)

Requires:       lxqt-menu-data >= 2.4.0

%description
libfm-qt is the Qt port of libfm. It provides components used to build
desktop file managers and related file management utilities.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets)
Requires:       pkgconfig(gio-2.0) >= 2.50.0
Requires:       pkgconfig(gio-unix-2.0) >= 2.50.0
Requires:       pkgconfig(glib-2.0) >= 2.50.0
Requires:       pkgconfig(gobject-2.0) >= 2.50.0
Requires:       pkgconfig(gthread-2.0) >= 2.50.0
Requires:       pkgconfig(libexif)
Requires:       pkgconfig(libmenu-cache) >= 1.1.0
Requires:       pkgconfig(xcb)

%description    devel
Development files for libfm-qt.

%install -a
%find_lang %{name} --generate-subpackages --with-qt

%files -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%license LICENSE LICENSE.BSD-3-Clause
%{_libdir}/libfm-qt6.so.17*
%dir %{_datadir}/libfm-qt6
%dir %{_datadir}/libfm-qt6/translations
%{_datadir}/libfm-qt6/archivers.list
%{_datadir}/libfm-qt6/terminals.list
%{_datadir}/mime/packages/libfm-qt6-mimetypes.xml

%files devel
%{_includedir}/libfm-qt6/
%{_libdir}/libfm-qt6.so
%{_libdir}/pkgconfig/libfm-qt6.pc
%{_datadir}/cmake/fm-qt6/

%changelog
%autochangelog
