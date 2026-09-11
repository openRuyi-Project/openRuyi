# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pbzip2
%define go_import_path  github.com/cosnicolaou/pbzip2
# TestBzip2Tests git-clones sourceware.org/bzip2-tests; the sandbox has no git.
%define go_test_ignore_failure 1

Name:           go-github-cosnicolaou-pbzip2
Version:        1.0.5
Release:        %autorelease
Summary:        Parallel bzip2 decompression for Go
License:        Apache-2.0
URL:            https://github.com/cosnicolaou/pbzip2
#!RemoteAsset:  sha256:df45ca125533ec6aa16d6fb9a24f68d52b0b2db9a2282325e6fef66deeb2dbc2
Source0:        https://github.com/cosnicolaou/pbzip2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

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
