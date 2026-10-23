# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bodyclose
%define go_import_path  github.com/timakin/bodyclose
%define commit_id       98ded9ab4ef2741bca30b6d18b73bd9b53181cd4

Name:           go-github-timakin-bodyclose
Version:        0+git20261022.98ded9a
Release:        %autorelease
Summary:        Bodyclose is a static analysis tool which checks whether res.Body is correctly closed
License:        MIT
URL:            https://github.com/timakin/bodyclose
#!RemoteAsset:  sha256:1341252d6f0f078e7f5aa300b04b170da3adb9696da13105718cf030d6688d60
Source0:        https://github.com/timakin/bodyclose/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/timakin/bodyclose) = %{version}
Provides:       go(github.com/timakin/bodyclose/passes/bodyclose) = %{version}

Requires:       go(github.com/gostaticanalysis/analysisutil)
Requires:       go(golang.org/x/tools)

%description
Bodyclose is a static analysis tool which checks whether res.Body is correctly closed.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n bodyclose-%{commit_id}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/timakin/bodyclose

%changelog
%autochangelog
