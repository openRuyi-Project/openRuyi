# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cidr
%define go_import_path  github.com/apparentlymart/go-cidr

Name:           go-github-apparentlymart-go-cidr
Version:        1.1.1
Release:        %autorelease
Summary:        Go library for various manipulations of CIDR netmasks and their associated addresses
License:        MIT
URL:            https://github.com/apparentlymart/go-cidr
#!RemoteAsset:  sha256:0f48cee94809f6885ed1bf90194c3f21b4cd450aa7ad102f5d0414a5430a2b64
Source0:        https://github.com/apparentlymart/go-cidr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/apparentlymart/go-cidr) = %{version}

%description
Go library for various manipulations of CIDR netmasks and their associated addresses

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
