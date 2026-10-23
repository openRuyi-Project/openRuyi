# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gomoddirectives
%define go_import_path  github.com/ldez/gomoddirectives

Name:           go-github-ldez-gomoddirectives
Version:        0.10.0
Release:        %autorelease
Summary:        Go analyzer for module directives
License:        Apache-2.0
URL:            https://github.com/ldez/gomoddirectives
#!RemoteAsset:  sha256:ea9f21848d575adfb6f9f57f44e40f759f095ab60d349c04b05d5f04410179f9
Source0:        https://github.com/ldez/gomoddirectives/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/context)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/ldez/grignotin)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ldez/gomoddirectives) = %{version}

Requires:       go(github.com/ldez/grignotin)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for module directives.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gomoddirectives-%{version}

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/github.com/ldez/gomoddirectives

%changelog
%autochangelog
