# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lz4
%define go_import_path  github.com/pierrec/lz4

Name:           go-github-pierrec-lz4
Version:        2.0.5
Release:        %autorelease
Summary:        LZ4 compression and decompression for Go
License:        BSD-3-Clause
URL:            https://github.com/pierrec/lz4
#!RemoteAsset:  sha256:322b98493c960e940cf187646957bea4fe96a274412b88d7d199a9cbf39591c6
Source0:        https://github.com/pierrec/lz4/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pierrec/lz4) = %{version}

%description
This library implements LZ4 block compression, readers and writers in Go.

%prep -a
# The standalone profiling command is outside the reusable compression library.
rm -rf lz4c

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
