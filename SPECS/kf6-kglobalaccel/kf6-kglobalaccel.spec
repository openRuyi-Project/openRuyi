# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kglobalaccel
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kglobalaccel
Version:        6.22.0
Release:        %autorelease
Summary:        Global desktop keyboard shortcuts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kglobalaccel
#!RemoteAsset:  sha256:332e3be3d0ac2aec8e786419c1e875a1b33ae84b8aada3283639deccc6ffd4d8
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package        devel
Summary:        Global desktop keyboard shortcuts: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kglobalaccel.categories
%{_kf6_debugdir}/kglobalaccel.renamecategories
%{_kf6_libdir}/libKF6GlobalAccel.so.*

%files devel
%{_kf6_libdir}/libKF6GlobalAccel.so
%{_kf6_cmakedir}/KF6GlobalAccel/
%{_kf6_includedir}/KGlobalAccel/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.KGlobalAccel.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.kglobalaccel.Component.xml

%changelog
%autochangelog
