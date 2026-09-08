# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kong-hcl
%define go_import_path  github.com/alecthomas/kong-hcl
%define commit_id       98e50d023e3b02b1908a8773a81732c72e2e6464

Name:           go-github-alecthomas-kong-hcl
Version:        1.0.1+git20260819.98e50d0
Release:        %autorelease
Summary:        HCL configuration loader for Kong
License:        MIT
URL:            https://github.com/alecthomas/kong-hcl
#!RemoteAsset:  sha256:2ba1e19813a247e5ce0efd3b0998050e3be890b1cf2c4b892c0d3c56e5133b24
Source0:        https://github.com/alecthomas/kong-hcl/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kong)
BuildRequires:  go(github.com/alecthomas/repr)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hashicorp/hcl/v2)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/zclconf/go-cty)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/alecthomas/kong)
Requires:       go(github.com/alecthomas/repr)
Requires:       go(github.com/hashicorp/hcl)
Requires:       go(github.com/hashicorp/hcl/v2)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/zclconf/go-cty)

%description
Kong-HCL loads HashiCorp Configuration Language files into command-line
applications built with Kong.

%files
%doc README.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
