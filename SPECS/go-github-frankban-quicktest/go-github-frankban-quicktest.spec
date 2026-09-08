# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           quicktest
%define go_import_path  github.com/frankban/quicktest

Name:           go-github-frankban-quicktest
Version:        1.14.6
Release:        %autorelease
Summary:        Quick helpers for testing Go applications
License:        MIT
URL:            https://github.com/frankban/quicktest
#!RemoteAsset:  sha256:c77b45b267ac5f5e03d00ab1b3f944d68c74e91601a1c8121e49040ff89d8b0a
Source0:        https://github.com/frankban/quicktest/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)

Provides:       go(github.com/frankban/quicktest) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/kr/pretty)

%description
This package quicktest provides a collection of Go helpers for writing
tests.

%check -p
# Keep encoding/json v1 semantics for tests incompatible with Go 1.27 jsonv2.
export GOEXPERIMENT=nojsonv2

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
