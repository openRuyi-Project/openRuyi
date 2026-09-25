# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonutils
%define go_import_path  yunion.io/x/jsonutils
%define commit_id       1abcf4f443b1ff48e5ea8c4e113630b3fa24650b

Name:           go-yunion-x-jsonutils
Version:        0+git20260922.1abcf4f
Release:        %autorelease
Summary:        JSON data manipulation library for Cloudpods
License:        Apache-2.0
URL:            https://github.com/yunionio/jsonutils
#!RemoteAsset:  sha256:0c81b6d79615b4315f9af025562587086751c506f69c3feeb1a6c68c4f54c8b7
Source0:        https://github.com/yunionio/jsonutils/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/ghodss/yaml)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(yunion.io/x/log)
BuildRequires:  go(yunion.io/x/pkg/errors)
BuildRequires:  go(yunion.io/x/pkg/gotypes)
BuildRequires:  go(yunion.io/x/pkg/sortedmap)
BuildRequires:  go(yunion.io/x/pkg/tristate)
BuildRequires:  go(yunion.io/x/pkg/util/reflectutils)
BuildRequires:  go(yunion.io/x/pkg/util/regutils)
BuildRequires:  go(yunion.io/x/pkg/util/timeutils)
BuildRequires:  go(yunion.io/x/pkg/utils)

Provides:       go(yunion.io/x/jsonutils) = %{version}

Requires:       go(github.com/ghodss/yaml)
Requires:       go(golang.org/x/text)
Requires:       go(yunion.io/x/log)
Requires:       go(yunion.io/x/pkg/errors)
Requires:       go(yunion.io/x/pkg/gotypes)
Requires:       go(yunion.io/x/pkg/sortedmap)
Requires:       go(yunion.io/x/pkg/tristate)
Requires:       go(yunion.io/x/pkg/util/reflectutils)
Requires:       go(yunion.io/x/pkg/util/regutils)
Requires:       go(yunion.io/x/pkg/util/timeutils)
Requires:       go(yunion.io/x/pkg/utils)

%description
This library provides JSON parsing, marshaling, querying, comparison
and YAML conversion for Cloudpods.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
