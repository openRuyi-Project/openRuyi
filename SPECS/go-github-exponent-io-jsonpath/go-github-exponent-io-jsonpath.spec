# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonpath
%define go_import_path  github.com/exponent-io/jsonpath

Name:           go-github-exponent-io-jsonpath
Version:        0+git20151013.d6023ce
Release:        %autorelease
Summary:        Go library for jsonpath
License:        MIT
URL:            https://github.com/exponent-io/jsonpath
VCS:            git:https://github.com/exponent-io/jsonpath.git
#!RemoteAsset:  sha256:398eb399e422475edfaf0890cbc8a5e6a915f2cbc07c835fb0a221920ee2278a
Source0:        https://github.com/exponent-io/jsonpath/archive/d6023ce2651d.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n jsonpath-d6023ce2651d8eafb5c75bb0c7167536102ec9f5

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/exponent-io/jsonpath) = %{version}

%description
This package provides the github.com/exponent-io/jsonpath Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
