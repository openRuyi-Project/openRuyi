# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           brotli
Version:        1.1.0
Release:        %autorelease
Summary:        Lossless Compression Algorithm
License:        MIT
URL:            https://github.com/google/brotli
#!RemoteAsset
Source:         https://github.com/google/brotli/archive/v%version.tar.gz
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  pkg-config
BuildSystem:    cmake

%description
This package contains the brotli command line utility to compress and
decompress data with the brotli compression algorithm.

Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with a
compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with
deflate but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in
RFC 7932.

%package devel
Summary:        Development and Header Files for Brotli Compression
Requires:       %{name} = %version-%release

%description    devel
Development and headers files for (de)compressing data using the
Brotli general purpose lossless compression algorithm.

The specification of the Brotli Compressed Data Format is defined in
RFC 7932.

%build -p
export CFLAGS="%{optflags} -DBROTLI_ENCODER_CLEANUP_ON_OOM"

%install -a
mkdir -p "%buildroot/%{_mandir}/man1" "%buildroot/%{_mandir}/man3"
install -pm0644 docs/*.1 "%buildroot/%_mandir/man1/"
install -pm0644 docs/*.3 "%buildroot/%_mandir/man3/"

%files
%license LICENSE
%_bindir/brotli
%_mandir/man1/brotli.1*
%_libdir/libbrotlicommon.so.*
%_libdir/libbrotlidec.so.*
%_libdir/libbrotlienc.so.*

%files devel
%_includedir/brotli/
%_libdir/libbrotlicommon.so
%_libdir/libbrotlidec.so
%_libdir/libbrotlienc.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
%{?autochangelog}
