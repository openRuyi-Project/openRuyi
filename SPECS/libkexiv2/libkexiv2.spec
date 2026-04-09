# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libkexiv2
Version:        25.12.2
Release:        %autorelease
Summary:        A wrapper around Exiv2 library (Qt6)
License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:            https://invent.kde.org/graphics/libkexiv2
#!RemoteAsset:  sha256:b8d914d03ca96b4e2d3a1707af424980a7f0685b109220b25efb76ed7e7778b6
Source0:        http://download.kde.org/stable/release-service/%{version}/src/libkexiv2-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  pkgconfig(exiv2)

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures metadata
as EXIF IPTC and XMP.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)

%description    qt6-devel
Development files for libkexiv2-qt6.

%files
%license LICENSES/*
%doc AUTHORS README
%{_datadir}/qlogging-categories6/*libkexiv2.*
%{_libdir}/libKExiv2Qt6.so.*

%files qt6-devel
%{_libdir}/libKExiv2Qt6.so
%{_includedir}/KExiv2Qt6/
%{_libdir}/cmake/KExiv2Qt6/

%changelog
%autochangelog
