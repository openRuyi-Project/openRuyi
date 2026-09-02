# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uap-go
%define go_import_path  github.com/ua-parser/uap-go
%define commit_id       17c35e68e58c2c175ee4e0515ea4309d0015b50d
%define uap_core_commit c941f1d2cd528be1d597471e5c502a9dc0eb3ac8

Name:           go-github-ua-parser-uap-go
Version:        0+git20260817.17c35e6
Release:        %autorelease
Summary:        User agent parser for Go
License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-go
#!RemoteAsset:  sha256:2253e72a2041d486994d97b0b7cf0b54b78bf417af6962141e105fe9c565ba9c
Source0:        https://github.com/ua-parser/uap-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:9c1e6eb603c14ab040ac5056f2d552adb5834b242443449b1c3debe567a5fd2b
Source1:        https://github.com/ua-parser/uap-core/archive/%{uap_core_commit}.tar.gz#/%{_name}-core-%{uap_core_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id} -a1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/hashicorp/golang-lru)
Requires:       go(gopkg.in/yaml.v3)

%description
This package identifies browsers, operating systems, and devices from user
agent strings using ua-parser definitions embedded in Go source.

%prep -a
rm -rf uap-core
mv uap-core-%{uap_core_commit} uap-core

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
