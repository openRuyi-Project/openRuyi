# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minlz
%define go_import_path  github.com/minio/minlz

Name:           go-github-minio-minlz
Version:        1.2.0
Release:        %autorelease
Summary:        MinLZ is a LZ77-type compressor with a fixed byte-aligned encoding,
License:        Apache-2.0
URL:            https://github.com/minio/minlz
#!RemoteAsset:  sha256:97ee400e2722d5da9f159ee5f68d42c413a59a71d5a6814242e7f6e00bcf8f15
Source0:        https://github.com/minio/minlz/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/klauspost/compress) >= 1.19.0

Provides:       go(github.com/minio/minlz) = %{version}

Requires:       go(github.com/klauspost/compress) >= 1.19.0

%description
MinLZ is a LZ77-type compressor with a fixed byte-aligned encoding, in
the
similar class to Snappy and LZ4.

The goal of MinLZ is to provide a fast, low memory compression algorithm
that can be used for fast compression of data, where encoding and/or
decoding speed is the primary concern.

MinLZ is designed to operate *faster than IO* for both compression and
decompression.

It is a viable "always on" option, even if some content already is
compressed.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
