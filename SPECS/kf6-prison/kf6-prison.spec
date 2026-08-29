# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname prison
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-prison
Version:        6.28.0
Release:        %autorelease
Summary:        Barcode abstraction layer library
License:        MIT
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/prison.git
#!RemoteAsset:  sha256:ad24dd64b5150ec9ebc4df9734b4c2a58c27a588eafeb4239cdcef01629fe696
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
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

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/prison.categories
%{_kf6_debugdir}/prison.renamecategories
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6Prison.so.%{version}
%{_kf6_libdir}/libKF6PrisonScanner.so.6
%{_kf6_libdir}/libKF6PrisonScanner.so.%{version}
%{_kf6_qmldir}/org/kde/prison/

%files devel
%{_kf6_cmakedir}/KF6Prison/
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so

%changelog
%autochangelog
