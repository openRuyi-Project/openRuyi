# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           woff2
Version:        1.0.2
Release:        %autorelease
Summary:        Web Open Font Format 2.0 library
License:        GPL-3.0-or-later
URL:            https://github.com/google/woff2
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_SKIP_RPATH=TRUE
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  pkgconfig(libbrotlidec)

# We provide tools! No need for a separate package.
Provides:       %{name}-tools

%patchlist
# https://github.com/google/woff2/pull/176
0001-woff2-fix-build-with-gcc15.patch
# Install woff tools
0002-install-executables.patch

%description
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF 1.0 with
improved compression that is achieved by using the Brotli algorithm. The primary
purpose of the WOFF2 format is to efficiently package fonts linked to Web
documents by means of CSS @font-face rules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files and utils for %{name}

%files
%license LICENSE
%{_bindir}/woff2_compress
%{_bindir}/woff2_decompress
%{_bindir}/woff2_info
%{_libdir}/libwoff2common.so.*
%{_libdir}/libwoff2dec.so.*
%{_libdir}/libwoff2enc.so.*

%files devel
%{_includedir}/woff2
%{_libdir}/libwoff2common.so
%{_libdir}/libwoff2dec.so
%{_libdir}/libwoff2enc.so
%{_libdir}/pkgconfig/libwoff2common.pc
%{_libdir}/pkgconfig/libwoff2dec.pc
%{_libdir}/pkgconfig/libwoff2enc.pc

%changelog
%autochangelog
