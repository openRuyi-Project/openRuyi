# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lz4
Version:        1.10.0
Release:        %autorelease
Summary:        Hash-based Predictive Lempel–Ziv compressor
License:        BSD-2-Clause AND GPL-2.0-or-later
URL:            https://lz4.github.io/lz4/
#!RemoteAsset
Source:         https://github.com/lz4/lz4/releases/download/v%{version}/lz4-%{version}.tar.gz
Patch1:         lz4-export.diff
BuildRequires:  pkgconfig
BuildRequires:  make
BuildSystem:    autotools
BuildOption(build): PREFIX=%{_prefix}
BuildOption(install): PREFIX=%{_prefix} LIBDIR=%{_libdir}
%description
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(Lempel–Ziv) family of byte-oriented compression schemes. It is a
LZP2 fork and provides better compression ratio for text files.

This subpackage provides a GPL command-line utility to make use of
the LZ4 algorithm.

%package devel
Summary:        Development files for the LZ4 compressor
License:        BSD-2-Clause
Requires:       %{name} = %version

%description devel
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(Lempel–Ziv) family of byte-oriented compression schemes. It is a

This subpackage contains libraries and header files for developing
applications that want to make use of liblz4.

%package static
Summary:        Static version of %{name} library
Requires:       %{name}-devel = %{version}

%description static
Static library for the %{name} library

# no configure script
%conf

%files
%_bindir/lz4*
%_bindir/unlz4
%_mandir/man1/*.1*
%{_libdir}/liblz4.so.1*

%files devel
%{_includedir}/lz4*.h
%{_libdir}/liblz4.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/liblz4.a

%changelog
%{?autochangelog}
