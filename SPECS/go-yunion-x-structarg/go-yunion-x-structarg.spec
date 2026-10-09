# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structarg
%define go_import_path  yunion.io/x/structarg
%define commit_id       df4d5009457ca8275a54852a2bedd037a9646327

Name:           go-yunion-x-structarg
Version:        0+git20260922.df4d500
Release:        %autorelease
Summary:        Struct-based argument parsing library for Go
License:        Apache-2.0
URL:            https://github.com/yunionio/structarg
#!RemoteAsset:  sha256:0d40e84fdeff9e3f25872460301123b90f2ea8a38137a162bc601f97bf8a6b24
Source0:        https://github.com/yunionio/structarg/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/texttheater/golang-levenshtein)
BuildRequires:  go(yunion.io/x/jsonutils)
BuildRequires:  go(yunion.io/x/log)
BuildRequires:  go(yunion.io/x/pkg/errors)
BuildRequires:  go(yunion.io/x/pkg/gotypes)
BuildRequires:  go(yunion.io/x/pkg/util/reflectutils)
BuildRequires:  go(yunion.io/x/pkg/utils)

Provides:       go(yunion.io/x/structarg) = %{version}

Requires:       go(github.com/texttheater/golang-levenshtein)
Requires:       go(yunion.io/x/jsonutils)
Requires:       go(yunion.io/x/log)
Requires:       go(yunion.io/x/pkg/errors)
Requires:       go(yunion.io/x/pkg/gotypes)
Requires:       go(yunion.io/x/pkg/util/reflectutils)
Requires:       go(yunion.io/x/pkg/utils)

%description
This library parses command-line arguments and configuration files
into Go structures using field tags to define argument behavior.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
