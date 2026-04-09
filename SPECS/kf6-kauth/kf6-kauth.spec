# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname   kauth
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kauth
Version:        6.22.0
Release:        %autorelease
Summary:        Framework which lets applications perform actions as a privileged user
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kauth
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  kf6-kcoreaddons-devel >= %{_kf6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_version}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Framework which lets applications perform actions as a privileged user
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}

%description    devel
KAuth is a framework to let applications perform actions as a privileged user.
Development files.

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
%dir %{_kf6_plugindir}/kf6/kauth
%{_kf6_plugindir}/kf6/kauth/backend/
%{_kf6_dbuspolicydir}/org.kde.kf6auth.conf
%{_kf6_debugdir}/kauth.categories
%{_kf6_debugdir}/kauth.renamecategories
%{_kf6_libexecdir}/kauth/kauth-policy-gen
%{_kf6_plugindir}/kf6/kauth/helper/
%{_kf6_libdir}/libKF6AuthCore.so.*

%files devel
%{_kf6_cmakedir}/KF6Auth/
%dir %{_kf6_datadir}/kauth
%{_kf6_datadir}/kauth/dbus_policy.stub
%{_kf6_datadir}/kauth/dbus_service.stub
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
%{_kf6_libdir}/libKF6AuthCore.so

%changelog
%autochangelog
