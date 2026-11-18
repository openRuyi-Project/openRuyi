# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gocovmerge
%define go_import_path  github.com/wadey/gocovmerge
%define commit_id       b5bfa59ec0adc420475f97f89b58045c721d761c

Name:           go-github-wadey-gocovmerge
Version:        0+git20261022.b5bfa59
Release:        %autorelease
Summary:        Gocovmerge takes the results from multiple go test -coverprofile runs and merges them into one profile
License:        BSD-2-Clause
URL:            https://github.com/wadey/gocovmerge
#!RemoteAsset:  sha256:3058a7cdc3e79a3496c2b1d44c25b9cb06e7264aa0d69364b92bb86fd4a80473
Source0:        https://github.com/wadey/gocovmerge/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/tools/cover)

Provides:       go(github.com/wadey/gocovmerge) = %{version}

Requires:       go(golang.org/x/tools/cover)

%description
Gocovmerge takes the results from multiple go test -coverprofile runs and merges them into one profile.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gocovmerge-%{commit_id}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/wadey/gocovmerge

%changelog
%autochangelog
