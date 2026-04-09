# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mimalloc
Version:        3.1.5
Release:        %autorelease
Summary:        A general purpose allocator with excellent performance
License:        MIT
URL:            https://github.com/microsoft/mimalloc
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# unmerged patch enabling native RISC-V pause support
Patch0:         riscv-atomic-yield-fastpath.patch

BuildOption(conf):  -DMI_INSTALL_TOPLEVEL=ON
# if you want to override malloc/free globally, set this to ON
BuildOption(conf):  -DMI_OVERRIDE=OFF
BuildOption(conf):  -DMI_BUILD_STATIC=OFF
BuildOption(conf):  -DMI_BUILD_OBJECT=OFF
BuildOption(conf):  -DMI_BUILD_TESTS=ON
BuildOption(conf):  -DMI_OPT_ARCH=ON
BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
mimalloc (pronounced "me-malloc") is a general purpose allocator with
excellent performance characteristics. Initially developed by Daan Leijen
for run-time systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed to develop
applications that use mimalloc.

%prep -a
# Remove any pre-compiled binaries from the source tarball.
rm -rf bin

%files
%license LICENSE
%doc readme.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/mimalloc.h
%{_includedir}/mimalloc-new-delete.h
%{_includedir}/mimalloc-override.h
%{_includedir}/mimalloc-stats.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
