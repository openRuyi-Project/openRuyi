# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname prison
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-prison
Version:        6.22.0
Release:        %autorelease
Summary:        Barcode abstraction layer library
License:        MIT
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/prison.git
#!RemoteAsset:  sha256:c40d692607bdadf8dbd5a56761289b1ee96973f048ca3671e760519e2ae4339a
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(ZXing) >= 1.2.0
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Prison is a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%package        devel
Summary:        Development files Prison, a barcode abstraction library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description    devel
Development files for prison, a barcode abstraction layer library providing
uniform access to generation of barcodes with data.

%install -a

%files
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/prison.categories
%{_kf6_debugdir}/prison.renamecategories
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6Prison.so.%{version}
%{_kf6_qmldir}/org/kde/prison/

%files devel
%{_kf6_cmakedir}/KF6Prison/
%{_kf6_includedir}/Prison/
%{_kf6_libdir}/libKF6Prison.so

%changelog
%autochangelog
