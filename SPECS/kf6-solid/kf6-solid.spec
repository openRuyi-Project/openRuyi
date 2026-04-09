# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname solid

Name:           kf6-solid
Version:        6.22.0
Release:        %autorelease
Summary:        KDE Desktop hardware abstraction
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/solid
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mount)

%description
Solid is a device integration framework. It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package        devel
Summary:        KDE Desktop hardware abstraction: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Solid is a device integration framework. It provides a way of querying and
interacting with hardware independently of the underlying operating system.
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
%{_kf6_debugdir}/solid.categories
%{_kf6_debugdir}/solid.renamecategories
%{_kf6_bindir}/solid-hardware6
%{_kf6_libdir}/libKF6Solid.so.*

%files devel
%{_kf6_includedir}/Solid/
%{_kf6_cmakedir}/KF6Solid/
%{_kf6_libdir}/libKF6Solid.so

%changelog
%autochangelog
