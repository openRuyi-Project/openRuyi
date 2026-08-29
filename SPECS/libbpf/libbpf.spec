# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libbpf
Version:        1.7.0
Release:        %autorelease
Summary:        C library for managing eBPF programs and maps
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://github.com/libbpf/libbpf
#!RemoteAsset:  sha256:7ab5feffbf78557f626f2e3e3204788528394494715a30fc2070fcddc2051b7b
Source:         https://github.com/libbpf/libbpf/archive/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(build):  -C src
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  -C src

BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)

%description
libbpf is a C library which provides API for managing eBPF programs and maps.

%package        devel
Summary:        Development files for libbpf
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libbpf is a C library which provides API for managing eBPF programs and maps.

%package        static
Summary:        Static library for libbpf development
Requires:       %{name}-devel = %{version}-%{release}

%description    static
The %{name}-static package contains static library for
developing applications that use %{name}.

%conf

%check
# Upstream does not provide a 'make check' target.

%files
%{_libdir}/libbpf.so.*

%files devel
%{_libdir}/libbpf.so
%{_includedir}/bpf/
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%changelog
%autochangelog
