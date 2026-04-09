# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           compress
%define go_import_path  github.com/klauspost/compress

Name:           go-github-klauspost-compress
Version:        1.18.2
Release:        %autorelease
Summary:        Optimized Go Compression Packages
License:        BSD-3-Clause AND Apache-2.0 AND MIT
URL:            https://github.com/klauspost/compress
#!RemoteAsset
Source0:        https://github.com/klauspost/compress/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -short -timeout 1h

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/klauspost/compress) = %{version}

%description
This package provides various compression algorithms.

 * zstandard (https://github.
   com/klauspost/compress/tree/master/zstd#zstd) compression and
   decompression in pure Go.
 * S2 (https://github.com/klauspost/compress/tree/master/s2#s2-
   compression) is a high performance replacement for Snappy.
 * Optimized deflate (https://godoc.org/github.
   com/klauspost/compress/flate) packages which can be used as a dropin
   replacement for gzip (https://godoc.org/github.
   com/klauspost/compress/gzip), zip (https://godoc.org/github.
   com/klauspost/compress/zip) and zlib (https://godoc.org/github.
   com/klauspost/compress/zlib).
 * snappy (https://github.com/klauspost/compress/tree/master/snappy) is
   a drop-in replacement for github.com/golang/snappy offering better
   compression and concurrent streams.
 * huff0 (https://github.com/klauspost/compress/tree/master/huff0) and
   FSE (https://github.com/klauspost/compress/tree/master/fse)
   implementations for raw entropy encoding.
 * gzhttp (https://github.com/klauspost/compress/tree/master/gzhttp)
   Provides client and server wrappers for handling gzipped requests
   efficiently.
 * pgzip (https://github.com/klauspost/pgzip) is a separate package that
   provides a very fast parallel gzip implementation.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
