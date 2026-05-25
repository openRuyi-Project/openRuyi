# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           swag
%define go_import_path  github.com/go-openapi/swag

Name:           go-github-go-openapi-swag
Version:        0.25.4
Release:        %autorelease
Summary:        Helper functions for go-openapi projects
License:        Apache-2.0
URL:            https://github.com/go-openapi/swag
#!RemoteAsset:  sha256:d283d5dc2842d8d2376a1d815c82f1bf32acffc0640fa75cd8aaca0565ae8806
Source0:        https://github.com/go-openapi/swag/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go vet rejects yamlutils/yaml.go's %q format for yaml.v3 Kind; keep tests
# enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/testify)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/go-openapi/swag) = %{version}

Requires:       go(github.com/mailru/easyjson)
Requires:       go(go.yaml.in/yaml/v3)

%description
Package swag contains helper functions for go-openapi and go-swagger projects.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
