# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           terraform-plugin-log
%define go_import_path  github.com/hashicorp/terraform-plugin-log

Name:           go-github-hashicorp-terraform-plugin-log
Version:        0.10.0
Release:        %autorelease
Summary:        Module for logging from Terraform plugins.
License:        MPL-2.0
URL:            https://github.com/hashicorp/terraform-plugin-log
#!RemoteAsset
Source0:        https://github.com/hashicorp/terraform-plugin-log/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/mitchellh/go-testing-interface)

Provides:       go(github.com/hashicorp/terraform-plugin-log) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/mitchellh/go-testing-interface)

%description
terraform-plugin-log is a helper module for logging from Terraform
providers. It uses RPC-specific loggers to attach context and
information
to logs, and has multiple loggers to allow filtering of log output,
making finding what you're looking for easier. It is a small wrapper on
top of go-hclog (https://github.com/hashicorp/go-hclog), adding some
conventions and reframing things for Terraform plugin developers.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
