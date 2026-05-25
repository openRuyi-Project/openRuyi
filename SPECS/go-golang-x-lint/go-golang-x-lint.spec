# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lint
%define go_import_path  golang.org/x/lint
%define commit_id 6edffad5e6160f5949cdefc81710b2706fbcd4f6

Name:           go-golang-x-lint
Version:        0+git20260607.6edffad
Release:        %autorelease
Summary:        Go lint tool
License:        BSD-3-Clause
URL:            https://github.com/golang/lint
#!RemoteAsset:  sha256:5a064a54611ce69d55789e18e3e104e1c0dcad0df82d6454c975033125eaaf46
Source0:        https://github.com/golang/lint/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/lint) = %{version}

Requires:       go(golang.org/x/tools)

%description
lint provides the historical golint tool and supporting packages.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
