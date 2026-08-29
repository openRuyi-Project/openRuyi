# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uritemplate
%define go_import_path  github.com/yosida95/uritemplate/v3

Name:           go-github-yosida95-uritemplate-v3
Version:        3.0.2
Release:        %autorelease
Summary:        RFC 6570 URI Template implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/yosida95/uritemplate
VCS:            git:https://github.com/yosida95/uritemplate.git
#!RemoteAsset:  sha256:7421e5ed342a20a7eec91139de06cf91157e8f4267bdd61d7d94ae746873145a
Source0:        https://github.com/yosida95/uritemplate/archive/refs/tags/v%{version}.tar.gz#/uritemplate-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n uritemplate-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/yosida95/uritemplate/v3) = %{version}

%description
Uritemplate is an RFC 6570 URI Template implementation for Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
