# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ding-libs
Version:        0.6.2
Release:        %autorelease
Summary:        'Ding is not GLib' utility libraries
License:        GPLv3+ and LGPLv3+
URL:            https://github.com/SSSD/ding-libs/releases
#!RemoteAsset
Source0:        https://github.com/SSSD/ding-libs/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildSystem:    autotools
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pkgconfig

%description
A meta-package that pulls in libcollection, libdhash, libini_config,
librefarray libbasicobjects, and libpath_utils.

%package devel
Summary:         Development files for ding-libs
Requires:        ding-libs = %{version}-%{release}

%description devel
This package provides development libraries and other development files.

%conf -p
autoreconf -fiv

%files
%defattr(-,root,root)
%doc COPYING COPYING.LESSER README* dhash/* refarray/README.ref_array path_utils/README.path_utils
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc COPYING COPYING.LESSER README*
%{_includedir}/*
%{_libdir}/lib*.{a,la,so}
%{_libdir}/pkgconfig/*

%changelog
%{?autochangelog}
