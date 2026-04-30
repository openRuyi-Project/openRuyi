# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kfilemetadata
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

%bcond_without ffmpeg

Name:           kf6-kfilemetadata
Version:        6.22.0
Release:        %autorelease
Summary:        Library for extracting Metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kfilemetadata.git
#!RemoteAsset:  sha256:58e594fdb77883d684bd699731ed57ff24e8970c13c2a1bdb470f5dca84fb2bd
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  attr-devel
BuildRequires:  ebook-tools
BuildRequires:  pkgconfig
BuildRequires:  cmake(exiv2) >= 0.21
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
# Not packaged
# BuildRequires:  cmake(QMobipocket6)
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif

%description
KFileMetaData provides plugins for extracting file metadata.

%package        devel
Summary:        Development package for kfilemetadata
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
A library for extracting file metadata. Development files

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kfilemetadata_dump6
%{_kf6_debugdir}/kfilemetadata.categories
%{_kf6_debugdir}/kfilemetadata.renamecategories
%{_kf6_libdir}/libKF6FileMetaData.so.*
%{_kf6_plugindir}/kf6/kfilemetadata/

%files devel
%{_kf6_cmakedir}/KF6FileMetaData/
%{_kf6_includedir}/KFileMetaData/
%{_kf6_libdir}/libKF6FileMetaData.so

%changelog
%autochangelog
