# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           libvpx
Version:        1.15.2
Release:        %autorelease
Summary:        VP8/VP9 codec library
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            https://chromium.googlesource.com/webm/libvpx
VCS:            git:https://chromium.googlesource.com/webm/libvpx
#!RemoteAsset:  git+https://chromium.googlesource.com/webm/libvpx#v%{version}
#!CreateArchive
Source:         %{name}-%{version}.tar.gz
BuildSystem:    autotools

# Add arch support for riscv64.
Patch:          0001-libvpx-configure-add-arch.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
%ifarch x86_64
BuildRequires:  nasm
%endif

%description
WebM is an open, royalty-free, media file format designed for the web.
This package contains the documentation.

%package        devel
Summary:        Development files for libvpx
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and library for libvpx.

%conf
# Not a standard configure file And can not autoreconf.
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-unit-tests \
    --enable-shared \
    --enable-pic \
    --disable-static \
    --enable-vp8 \
    --enable-vp9 \
    --enable-vp9-highbitdepth \
    --enable-postproc \
    --enable-multithread \
    --extra-cflags="-std=gnu99 -U_FORTIFY_SOURCE %{optflags}" \
    --extra-cxxflags="-U_FORTIFY_SOURCE %{optflags}" \
    --size-limit=8192x8192

%check
# just skip,the test needs to download form internet.

%files
%doc AUTHORS README CHANGELOG
%license LICENSE
%{_bindir}/vpxenc
%{_bindir}/vpxdec
%{_libdir}/libvpx.so.11*

%files devel
%{_includedir}/vpx/
%{_libdir}/pkgconfig/vpx.pc
%{_libdir}/libvpx.so

%changelog
%autochangelog
