# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kded
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kded
Version:        6.22.0
Release:        %autorelease
Summary:        Central daemon of KDE workspaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kded
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

# One of the main tasks of kded is to run kconf_update when necessary
Requires:       kf6-kconfig

%description
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

%package        devel
Summary:        Central daemon of KDE workspaces: Build Environment
Requires:       kf6-kded >= %{version}

%description    devel
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%preun
%systemd_user_preun plasma-kded6.service

%post
%systemd_user_post plasma-kded6.service

%postun
%systemd_user_postun plasma-kded6.service

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_mandir}/*/kded6.*
%{_kf6_applicationsdir}/org.kde.kded6.desktop
%{_kf6_bindir}/kded6
%{_kf6_debugdir}/kded.categories
%{_kf6_debugdir}/kded.renamecategories
%{_kf6_sharedir}/dbus-1/services/org.kde.kded6.service
%{_userunitdir}/plasma-kded6.service
%{_kf6_mandir}/man8/kded6.8%{?ext_man}
%{_kf6_mandir}/*/man8/kded6.8%{?ext_man}

%files devel
%{_kf6_cmakedir}/KF6KDED/
%{_kf6_dbusinterfacesdir}/org.kde.kded6.xml

%changelog
%autochangelog
