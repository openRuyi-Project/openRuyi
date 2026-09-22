# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           squirrel
%define go_import_path  github.com/Masterminds/squirrel
%define go_test_exclude %{go_import_path}/integration

Name:           go-github-masterminds-squirrel
Version:        1.4.0
Release:        %autorelease
Summary:        Provides a fluent SQL generator
License:        MIT
URL:            https://github.com/Masterminds/squirrel
VCS:            git:https://github.com/Masterminds/squirrel.git
#!RemoteAsset:  sha256:a4f59e9622a49c010949373d36ddda198fe0de1e66de6c524edc415aead8ff9c
Source0:        https://github.com/Masterminds/squirrel/archive/v1.4.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n squirrel-1.4.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lann/builder)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/Masterminds/squirrel) = %{version}

Requires:       go(github.com/lann/builder)

%description
This package provides the github.com/Masterminds/squirrel Go module source.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
