# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kdbusaddons
# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kdbusaddons
Version:        6.22.0
Release:        %autorelease
Summary:        Convenience classes for QtDBus
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            https://invent.kde.org/frameworks/kdbusaddons
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6GuiPrivate) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package        tools
Summary:        Convenience classes for QtDBus: CLI tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Aditional CLI tools.

%package        devel
Summary:        Convenience classes for QtDBus: Build Environment
Requires:       kf6-extra-cmake-modules
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus) >= %{qt6_version}

%description    devel
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kdbusaddons.categories
%{_kf6_debugdir}/kdbusaddons.renamecategories
%{_kf6_libdir}/libKF6DBusAddons.so.*
%{_datadir}/locale/*/LC_MESSAGES/kdbusaddons6_qt.qm

%files tools
%{_kf6_bindir}/kquitapp6

%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_cmakedir}/KF6DBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so

%changelog
%autochangelog
