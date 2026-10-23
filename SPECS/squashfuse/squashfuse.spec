# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           squashfuse
Version:        0.6.5
Release:        %autorelease
Summary:        FUSE filesystem to mount squashfs archives
License:        BSD-2-Clause
URL:            https://github.com/vasi/squashfuse
#!RemoteAsset:  sha256:d7c324bd320c4e36de72b2b9db1d5c04c7c04ec57b03c29c7a4870e1ec58a018
Source:         https://github.com/vasi/squashfuse/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

# The low-level library is linked against the FUSE 3 provider.
Patch2000:      2000-use-fuse3-pkg-config-dependency.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-demo

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
This package contains the user-space tools and runtime libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries for
developing applications that use squashfuse.

%conf -p
./autogen.sh

%files
%doc README CONFIGURATION NEWS TODO
%license LICENSE
%{_bindir}/squashfuse
%{_bindir}/squashfuse_ll
%{_mandir}/man1/squashfuse.1*
%{_mandir}/man1/squashfuse_ll.1*
# Libraries (merged from -libs)
%{_libdir}/libsquashfuse.so.0*
%{_libdir}/libsquashfuse_ll.so.0*

%files devel
%{_includedir}/squashfuse/
%{_libdir}/pkgconfig/squashfuse.pc
%{_libdir}/pkgconfig/squashfuse_ll.pc
%{_libdir}/libsquashfuse.so
%{_libdir}/libsquashfuse_ll.so

%changelog
%autochangelog
