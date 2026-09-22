# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assertions
%define go_import_path  github.com/smartystreets/assertions
%define go_test_exclude %{go_import_path}/internal/go-render/render

Name:           go-github-smartystreets-assertions
Version:        1.2.0
Release:        %autorelease
Summary:        Go library for assertions
License:        MIT
URL:            https://github.com/smartystreets/assertions
VCS:            git:https://github.com/smartystreets/assertions.git
#!RemoteAsset:  sha256:b1b6becbca1d6375d426461d95c7daf5532770e4747b4ee600627d97aae10f87
Source0:        https://github.com/smartystreets/assertions/archive/v1.2.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n assertions-1.2.0
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata

Provides:       go(github.com/smartystreets/assertions) = %{version}

%description
This package provides the github.com/smartystreets/assertions Go module source.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
