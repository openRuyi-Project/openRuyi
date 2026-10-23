# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           promlinter
%define go_import_path  github.com/yeya24/promlinter

Name:           go-github-yeya24-promlinter
Version:        0.3.0
Release:        %autorelease
Summary:        A linter for checking Prometheus metrics name via promlint
License:        Apache-2.0
URL:            https://github.com/yeya24/promlinter
#!RemoteAsset:  sha256:4a4975e7cc519ba68173bdc854723d9e9ffa5edc1caaa0759bbad1c04bdf2708
Source0:        https://github.com/yeya24/promlinter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/template)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/alecthomas/kingpin.v2)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/yeya24/promlinter) = %{version}

Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(gopkg.in/alecthomas/kingpin.v2)
Requires:       go(gopkg.in/yaml.v2)

%description
A linter for checking Prometheus metrics name via promlint.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n promlinter-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/yeya24/promlinter

%changelog
%autochangelog
