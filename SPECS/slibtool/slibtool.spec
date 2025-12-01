# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           slibtool
Version:        0.7.3
Release:        %autorelease
Summary:        A skinny libtool implementation, written in C
License:        MIT
URL:            http://git.midipix.org/cgit.cgi/slibtool
#!RemoteAsset
Source0:        http://midipix.org/dl/slibtool/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  gcc make
BuildRequires:  m4

%description
'slibtool' is an independent reimplementation of the widely used libtool,
written in C. It is designed to be a clean, fast, easy-to-use
libtool drop-in replacement. Being a compiled binary, building a package
with 'slibtool' is often faster than with its script-based counterpart.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
This package provides files necessary for developing applications
that use functionality provided by slibtool.

%conf
# --disable-silent-rules: unsupported config argument.
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --includedir=%{_includedir} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --enable-shared \
    --all-shared \
    --disable-static

# No tests.
%check
:

%files
%license COPYING.SLIBTOOL
%doc README NEWS THANKS CONTRIB
%{_bindir}/*
%{_libdir}/lib*.so*

%files devel
%{_libdir}/lib*.so
%{_includedir}/slibtool/
%{_libdir}/pkgconfig/slibtool.pc
%{_datadir}/slibtool/

%changelog
%{?autochangelog}
