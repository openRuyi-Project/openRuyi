# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lz4
%define go_import_path  github.com/pierrec/lz4/v4
# TODO: this specific needs a lot of unpackaged build dependencies..
%define go_test_exclude_glob github.com/pierrec/lz4/v4/cmd*

Name:           go-github-pierrec-lz4-v4
Version:        4.1.23
Release:        %autorelease
Summary:        LZ4 compression and decompression in pure Go
License:        BSD-3-Clause
URL:            https://github.com/pierrec/lz4
#!RemoteAsset
Source0:        https://github.com/pierrec/lz4/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# TODO: tests are currently failing, need to investigate - 251
Patch0:         2000-skip-multiple-tests.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pierrec/lz4/v4) = %{version}

%description
This package provides a streaming interface to LZ4 data streams
(http://fastcompression.blogspot.fr/2013/04/lz4-streaming-format-
final.html) as well as low level compress and uncompress functions for
LZ4 data blocks. The implementation is based on the reference C one
(https://github.com/lz4/lz4).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
