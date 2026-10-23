# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           importas
%define go_import_path  github.com/julz/importas

Name:           go-github-julz-importas
Version:        0.2.0
Release:        %autorelease
Summary:        A linter to enforce importing certain packages consistently
License:        Apache-2.0
URL:            https://github.com/julz/importas
#!RemoteAsset:  sha256:285d5b78d6294f44c199cc6afab22d69ef20107b2d58ce2f556a144f27be54b9
Source0:        https://github.com/julz/importas/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(knative.dev/serving)

Provides:       go(github.com/julz/importas) = %{version}

Requires:       go(golang.org/x/tools)

%description
A linter to enforce importing certain packages consistently.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n importas-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/julz/importas

%changelog
%autochangelog
