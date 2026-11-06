# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zxcvbn-go
%define go_import_path  github.com/ccojocar/zxcvbn-go

Name:           go-github-ccojocar-zxcvbn-go
Version:        1.0.4
Release:        %autorelease
Summary:        Password strength estimator for Go
License:        MIT
URL:            https://github.com/ccojocar/zxcvbn-go
#!RemoteAsset:  sha256:3aacaec0bd52a8c56592882d89c9a92077a6dcd548e9db413e4146494fef7549
Source0:        https://github.com/ccojocar/zxcvbn-go/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.20
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/ccojocar/zxcvbn-go) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/adjacency) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/data) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/entropy) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/frequency) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/match) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/matching) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/scoring) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/testapp) = %{version}
Provides:       go(github.com/ccojocar/zxcvbn-go/utils/math) = %{version}

%description
Password strength estimator for Go. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
