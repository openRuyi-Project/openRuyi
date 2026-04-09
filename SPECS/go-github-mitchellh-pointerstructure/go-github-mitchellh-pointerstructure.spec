# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pointerstructure
%define go_import_path  github.com/mitchellh/pointerstructure

Name:           go-github-mitchellh-pointerstructure
Version:        1.2.1
Release:        %autorelease
Summary:        Go library for addressing and reading/writing a specific value within any Go structure using a string syntax.
License:        MIT
URL:            https://github.com/mitchellh/pointerstructure
#!RemoteAsset
Source0:        https://github.com/mitchellh/pointerstructure/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mitchellh/mapstructure)

Provides:       go(github.com/mitchellh/pointerstructure) = %{version}

Requires:       go(github.com/mitchellh/mapstructure)

%description
pointerstructure is a Go library for identifying a specific value within
any Go structure using a string syntax.

pointerstructure is based on JSON Pointer (RFC 6901)
(https://tools.ietf.org/html/rfc6901), but reimplemented for Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
