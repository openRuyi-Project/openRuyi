# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sasl
%define go_import_path  github.com/emersion/go-sasl
%define commit_id       b788ff22d5a6b3970cde181998f52658a475bffc

Name:           go-github-emersion-go-sasl
Version:        0+git20260721.b788ff2
Release:        %autorelease
Summary:        Simple Authentication and Security Layer library for Go
License:        MIT
URL:            https://github.com/emersion/go-sasl
#!RemoteAsset:  sha256:860a2cf75e5e59a13a40efbb7aa7ceeec624221a94df3ef20961e9dcc88d5dc6
Source0:        https://github.com/emersion/go-sasl/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/emersion/go-sasl) = %{version}

%description
A Go implementation of the Simple Authentication and Security Layer protocol.
It provides client and server support for common SASL authentication mechanisms.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
