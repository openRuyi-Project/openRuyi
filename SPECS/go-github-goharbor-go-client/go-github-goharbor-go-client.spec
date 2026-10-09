# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-client
%define go_import_path  github.com/goharbor/go-client

Name:           go-github-goharbor-go-client
Version:        0.26.2
Release:        %autorelease
Summary:        Client library with golang for accessing Harbor API
License:        Apache-2.0
URL:            https://github.com/goharbor/go-client
VCS:            git:https://github.com/goharbor/go-client.git
#!RemoteAsset:  sha256:646fe45454f60f71d1cc41be6e9f926e00c0273cfc853349dabaa5eca32dafcd
Source0:        https://github.com/goharbor/go-client/archive/v0.26.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-client-0.26.2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/runtime)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/goharbor/go-client) = %{version}

Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-openapi/runtime)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/validate)

%description
This package provides the github.com/goharbor/go-client Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
