# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ding-libs
Version:        0.6.2
Release:        %autorelease
Summary:        'Ding is not GLib' utility libraries
License:        GPL-3.0-or-later AND LGP-3.0-or-later
URL:            https://github.com/SSSD/ding-libs
#!RemoteAsset:  sha256:e5f07f34f5921bcb5ccccfe3751c28497879a6451cd7b395e99e24d9b5728e8d
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

%package        devel
Summary:        Development files for ding-libs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
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
%{_libdir}/pkgconfig/basicobjects.pc
%{_libdir}/pkgconfig/collection.pc
%{_libdir}/pkgconfig/dhash.pc
%{_libdir}/pkgconfig/ini_config.pc
%{_libdir}/pkgconfig/path_utils.pc
%{_libdir}/pkgconfig/ref_array.pc

%changelog
%autochangelog
