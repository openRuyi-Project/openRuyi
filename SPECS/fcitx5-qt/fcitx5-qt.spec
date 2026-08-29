# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __provides_exclude_from ^%{_libdir}/(fcitx5|qt6)/.*\\.so$

Name:           fcitx5-qt
Version:        5.1.13
Release:        %autorelease
Summary:        Qt library and IM module for fcitx5
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/fcitx/fcitx5-qt
#!RemoteAsset:  sha256:80f2604516a247ae2cd6b0b1994d75d2eb3df5160c8e19a90b1767e62d875cf9
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-qt/fcitx5-qt-%{version}.tar.zst
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_QT5=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ninja
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon-x11)

%description
Qt library and IM module for fcitx5.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt LICENSES/BSD-3-Clause.txt
%{_libdir}/qt6/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%{_libdir}/fcitx5/qt6/
%{_bindir}/fcitx5-qt6-immodule-probing
%{_libexecdir}/fcitx5-qt6-gui-wrapper
%{_libdir}/libFcitx5Qt6DBusAddons.so.1
%{_libdir}/libFcitx5Qt6DBusAddons.so.*.*
%{_libdir}/libFcitx5Qt6WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt6WidgetsAddons.so.*.*
%{_datadir}/applications/org.fcitx.fcitx5-qt6-gui-wrapper.desktop

%files devel
%{_includedir}/Fcitx5Qt6/
%{_libdir}/cmake/Fcitx5Qt6*
%{_libdir}/libFcitx5Qt6DBusAddons.so
%{_libdir}/libFcitx5Qt6WidgetsAddons.so

%changelog
%autochangelog
