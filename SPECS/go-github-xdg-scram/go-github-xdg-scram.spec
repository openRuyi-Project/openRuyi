# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           scram
%define go_import_path  github.com/xdg/scram

Name:           go-github-xdg-scram
Version:        1.0.5
Release:        %autorelease
Summary:        Legacy scram library → use xdg-go/scram instead
License:        Apache-2.0
URL:            https://github.com/xdg/scram
#!RemoteAsset
Source0:        https://github.com/xdg/scram/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xdg/stringprep)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/xdg/scram) = %{version}

%description
Package scram provides client and server implementations of the Salted
Challenge Response Authentication Mechanism (SCRAM) described in
[RFC-5802](https://tools.ietf.org/html/rfc5802) and
[RFC-7677](https://tools.ietf.org/html/rfc7677).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
