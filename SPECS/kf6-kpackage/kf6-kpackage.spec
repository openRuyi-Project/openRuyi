# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kpackage
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kpackage
Version:        6.22.0
Release:        %autorelease
Summary:        Non-binary asset user-installable package managing framework
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kpackage
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtds

%description
This framework lets applications to manage user installable packages of
non-binary assets.

%package        devel
Summary:        Non-binary asset user-installable package managing framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}

%description    devel
This framework lets applications to manage user installable packages of
non-binary assets.

Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6Package.so.*
%{_kf6_bindir}/kpackagetool6
%{_kf6_mandir}/man1/*.1*
%{_datadir}/man/*/man1/*.1*
%{_kf6_debugdir}/kpackage.categories
%{_kf6_debugdir}/kpackage.renamecategories

%files devel
%{_kf6_includedir}/KPackage/
%{_kf6_cmakedir}/KF6Package/
%{_kf6_libdir}/libKF6Package.so

%changelog
%autochangelog
