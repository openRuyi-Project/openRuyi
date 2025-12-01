# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           plzip
Version:        1.12
Release:        %autorelease
Summary:        Parallel lossless data compressor for the lzip format
License:        GPLv2+ AND BSD-2-Clause
URL:            https://www.nongnu.org/lzip/plzip.html
#!RemoteAsset
Source0:         https://download.savannah.nongnu.org/releases/lzip/plzip/plzip-%{version}.tar.gz
#!RemoteAsset
Source1:         https://download.savannah.nongnu.org/releases/lzip/plzip/plzip-%{version}.tar.gz.sig
BuildSystem:    autotools
BuildRequires:  gcc-c++
BuildRequires:  texinfo
BuildRequires:  lzlib-devel
%description
Plzip is a massively parallel (multi-threaded) lossless data compressor
and decompressor that uses the lzip file format (.lz).  Files produced by plzip
are fully compatible with lzip and can be rescued with lziprecover.
On multiprocessor machines, plzip can compress and decompress large files much
faster than lzip, at the cost of a slightly reduced compression ratio (0.4% to
2%).  The number of usable threads is limited by file size: on files of only a
few MiB, plzip is no faster than lzip.
Files that were compressed with regular lzip will also not be decompressed
faster by plzip, unless the @code{-b} option was used: lzip usually produces
single-member files which can't be decompressed in parallel.

%install -a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc README
%license COPYING
%{_bindir}/plzip
%{_mandir}/man1/*
%{_infodir}/*

%changelog
%{?autochangelog}
