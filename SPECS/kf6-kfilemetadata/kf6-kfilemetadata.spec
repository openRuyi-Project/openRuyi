# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kfilemetadata
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

%bcond ffmpeg 1

Name:           kf6-kfilemetadata
Version:        6.27.0
Release:        %autorelease
Summary:        Library for extracting Metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kfilemetadata.git
#!RemoteAsset:  sha256:27f68558259394ad84d357aa316821672ee66481fa851ddf2a6109f668a6c6a3
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
%if %{without ffmpeg}
BuildOption(conf):  -DCMAKE_DISABLE_FIND_PACKAGE_FFmpeg=ON
%endif

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig(libattr)
BuildRequires:  ebook-tools-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2)
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
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
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
