# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dupl
%define go_import_path  github.com/golangci/dupl

Name:           go-github-golangci-dupl
Version:        0+git20261022.c99c5cf
Release:        %autorelease
Summary:        Duplicate Go code detection library and tool
License:        MIT
URL:            https://github.com/golangci/dupl
#!RemoteAsset:  sha256:5e219bfd45675f4aaa0e8ecf0baf64a5fef84d9ce7e470c306fee8aeb5f525b2
Source0:        https://codeload.github.com/golangci/dupl/tar.gz/c99c5cf5c202c7e5bb1292e1212e7de4038324c8#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.22.0
BuildRequires:  go-rpm-macros

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/dupl) = %{version}
Provides:       go(github.com/golangci/dupl/job) = %{version}
Provides:       go(github.com/golangci/dupl/lib) = %{version}
Provides:       go(github.com/golangci/dupl/printer) = %{version}
Provides:       go(github.com/golangci/dupl/suffixtree) = %{version}
Provides:       go(github.com/golangci/dupl/syntax) = %{version}
Provides:       go(github.com/golangci/dupl/syntax/golang) = %{version}

%description
Duplicate Go code detection library and tool. This package contains the
complete upstream repository sources and tests.

%prep
%autosetup -n dupl-c99c5cf5c202c7e5bb1292e1212e7de4038324c8

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
