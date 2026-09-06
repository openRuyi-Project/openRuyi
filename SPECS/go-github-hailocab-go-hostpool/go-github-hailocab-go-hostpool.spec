# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-hostpool
%define go_import_path  github.com/hailocab/go-hostpool
%define commit_id       e80d13ce29ede4452c43dea11e79b9bc8a15b478

Name:           go-github-hailocab-go-hostpool
Version:        0+git20260818.e80d13c
Release:        %autorelease
Summary:        Host pool library for Go
License:        MIT
URL:            https://github.com/hailocab/go-hostpool
#!RemoteAsset:  sha256:ee47b177b2b97548ff0525cb8b6d6a25ab324dfd04d7003ca453f9c71f75e9b7
Source0:        https://github.com/hailocab/go-hostpool/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Give the legacy example request error a concrete type so it compiles.
Patch2000:      2000-example-make-request-error-placeholder-compile.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bitly/go-hostpool)
BuildRequires:  go(github.com/bmizerany/assert)

Provides:       go(%{go_import_path}) = %{version}

%description
This package selects hosts using round-robin or epsilon-greedy strategies and
temporarily avoids unresponsive hosts.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
