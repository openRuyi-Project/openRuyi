# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-uuid
%define go_import_path  github.com/hashicorp/go-uuid

Name:           go-github-hashicorp-go-uuid
Version:        1.0.3
Release:        %autorelease
Summary:        Generates UUID-format strings using purely high quality random bytes
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-uuid
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-uuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-uuid) = %{version}

%description
Generates UUID-format strings using high quality, *purely random* bytes.
It is **not** intended to be RFC compliant, merely to use a well-
understood string representation of a 128-bit value. It can also parse
UUID-format strings into their component bytes.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
