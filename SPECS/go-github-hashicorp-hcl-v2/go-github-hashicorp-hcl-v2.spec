# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hcl
%define go_import_path  github.com/hashicorp/hcl/v2

Name:           go-github-hashicorp-hcl-v2
Version:        2.24.0
Release:        %autorelease
Summary:        HashiCorp Configuration Language version 2 for Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/hcl
#!RemoteAsset:  sha256:0eef23c176aeb7d6f2e7a93aa7bb66405ff38bb407bac0a1ecbab89b09c7c6cf
Source0:        https://github.com/hashicorp/hcl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/agext/levenshtein)
BuildRequires:  go(github.com/apparentlymart/go-textseg/v15)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-test/deep)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mitchellh/go-wordwrap)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/zclconf/go-cty)
BuildRequires:  go(github.com/zclconf/go-cty-debug)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/agext/levenshtein)
Requires:       go(github.com/apparentlymart/go-textseg/v15)
Requires:       go(github.com/mitchellh/go-wordwrap)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/zclconf/go-cty)
Requires:       go(github.com/zclconf/go-cty-debug)
Requires:       go(golang.org/x/term)

%description
HCL is a toolkit for creating structured configuration languages that are
both human-friendly and machine-friendly. This package provides version 2.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
