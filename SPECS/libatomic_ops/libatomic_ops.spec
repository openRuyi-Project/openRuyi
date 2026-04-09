# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libatomic_ops
Version:        7.8.2
Release:        %autorelease
Summary:        A portable library for atomic memory operations
License:        GPL-2.0-or-later AND MIT
URL:            https://github.com/ivmai/libatomic_ops
#!RemoteAsset
Source:         https://github.com/ivmai/libatomic_ops/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --docdir=%{_docdir}/%{name}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Provides implementations for atomic memory update operations on a
number of architectures. This allows direct use of these in reasonably
portable code. Unlike earlier similar packages, this one explicitly
considers memory barrier semantics, and allows the construction of code
that involves minimum overhead across a variety of architectures.

%package        devel
Summary:        A portable library for atomic memory operations

%description    devel
Provides implementations for atomic memory update operations on a
number of architectures. This allows direct use of these in reasonably
portable code. Unlike earlier similar packages, this one explicitly
considers memory barrier semantics, and allows the construction of code
that involves minimum overhead across a variety of architectures.

%build -p
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%files devel
%license LICENSE COPYING
%doc ChangeLog README.md
%{_libdir}/libatomic_ops*.a
%{_includedir}/atomic_ops/
%{_includedir}/atomic_ops*.h
%{_libdir}/pkgconfig/atomic_ops.pc
%{_docdir}/%{name}/

%changelog
%autochangelog
