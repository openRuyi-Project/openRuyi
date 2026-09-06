# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwalterweatherman
%define go_import_path  github.com/spf13/jwalterweatherman

Name:           go-github-spf13-jwalterweatherman
Version:        1.1.0
Release:        %autorelease
Summary:        Seamless printing to terminal and logging to files for Go
License:        MIT
URL:            https://github.com/spf13/jwalterweatherman
#!RemoteAsset:  sha256:4fd850a792c5738954c4801cf549d8d0bf53edd17139cd39d179aa5abf7ec68d
Source0:        https://github.com/spf13/jwalterweatherman/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
Jwalterweatherman provides leveled terminal output and log-file handling for
Go command-line applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
