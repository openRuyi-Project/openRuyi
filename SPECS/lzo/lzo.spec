# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:    lzo
Version: 2.10
Release: %autorelease
License: GPL-2.0-or-later
URL:     https://www.oberhumer.com/opensource/lzo/
#!RemoteAsset
Source0: https://www.oberhumer.com/opensource/%{name}/download/%{name}-%{version}.tar.gz

BuildSystem: autotools
BuildOption(conf): --enable-shared

Summary: Data compression library suitable for real-time data de-/compression
%description
LZO is a data compression library which is suitable for data
de-/compression in real-time.  This means it favours speed over
compression ratio.

LZO is written in ANSI C.  Both the source code and the compressed data
format are designed to be portable across platforms.


%package devel
Summary:        Development files for lzo
Requires:       lzo = %{version}

%description devel
LZO is a portable lossless data compression library written in ANSI C.
Decompression requires no memory. LZO is suitable for data
de-/compression in real-time. This means it favours speed over
compression ratio.


%files
%license COPYING
%doc %{_docdir}/%{name}
%{_libdir}/liblzo2.so.*

%files devel
%doc AUTHORS BUGS NEWS README THANKS
%doc doc/* util/*
%{_libdir}/liblzo2.so
%{_libdir}/liblzo2.a
%{_includedir}/lzo
%{_libdir}/pkgconfig/lzo2.pc

%changelog
%autochangelog
