# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pbzip2
%define go_import_path  github.com/cosnicolaou/pbzip2

Name:           go-github-cosnicolaou-pbzip2
Version:        1.0.6
Release:        %autorelease
Summary:        Parallel bzip2 decompression for Go
License:        Apache-2.0
URL:            https://github.com/cosnicolaou/pbzip2
#!RemoteAsset:  sha256:1a4eaccaf2661cff459b821d823129b670ac1138fd33bd7fc1f31b49f3a6a0a7
Source0:        https://github.com/cosnicolaou/pbzip2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# This test clones the external bzip2 test suite; other tests run offline.
BuildOption(check):  -skip '^TestBzip2Tests$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cosnicolaou/pbzip2) = %{version}

%description
pbzip2 provides parallel, streaming bzip2 decompression for Go by
splitting independent bzip2 blocks across workers.

%prep -a
# cmd/pbzip2 is a nested module with its own go.mod. The C pbzip2
# package already owns /usr/bin/pbzip2.
rm -rf cmd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
