# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           swag
%define go_import_path  github.com/go-openapi/swag

Name:           go-github-go-openapi-swag
Version:        0.25.4
Release:        %autorelease
Summary:        goodie bag in use in the go-openapi projects
License:        Apache-2.0
URL:            https://github.com/go-openapi/swag
#!RemoteAsset
Source0:        https://github.com/go-openapi/swag/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/testify)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/go-openapi/swag) = %{version}

Requires:       go(github.com/go-openapi/testify)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(go.yaml.in/yaml/v3)

%description
Package swag contains a bunch of helper functions for go-openapi and go-
swagger projects.

You may also use it standalone for your projects.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
