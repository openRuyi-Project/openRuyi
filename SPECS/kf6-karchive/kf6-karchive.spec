# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname karchive
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-karchive
Version:        6.27.0
Release:        %autorelease
Summary:        Qt 6 addon providing access to numerous types of archives
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/karchive
#!RemoteAsset:  sha256:434edf78df8f4c9f25000d107ad1520d7ac14db580a202047bf19cbf77376522
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

It also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice.

%package        devel
Summary:        Development files for kf6-karchive
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

It also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice. Development files

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/karchive.categories
%{_kf6_debugdir}/karchive.renamecategories
%{_kf6_libdir}/libKF6Archive.so.*

%files devel
%{_kf6_includedir}/KArchive/
%{_kf6_cmakedir}/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so
%{_kf6_pkgconfigdir}/KF6Archive.pc

%changelog
%autochangelog
