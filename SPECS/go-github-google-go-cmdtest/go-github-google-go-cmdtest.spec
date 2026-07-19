# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cmdtest
%define go_import_path  github.com/google/go-cmdtest

Name:           go-github-google-go-cmdtest
Version:        0.4.0
Release:        %autorelease
Summary:        Go package for testing command-line interfaces
License:        Apache-2.0
URL:            https://github.com/google/go-cmdtest
#!RemoteAsset:  sha256:08ee0bebd49e0f52004286fcb264093f8524ed3d26dba235c7d6d772670a3bcd
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/renameio)

Provides:       go(github.com/google/go-cmdtest) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/renameio)

%description
The cmdtest package simplifies testing of command-line interfaces. It provides
a simple, cross-platform, shell-like language to express command execution.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
