# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gocapability
%define go_import_path  github.com/syndtr/gocapability
%global commit_id       42c35b4376354fd554efc7ad35e0b7f94e3a0ffb

Name:           go-github-syndtr-gocapability
Version:        0+git20260716.42c35b4
Release:        %autorelease
Summary:        Linux capability support for Go
License:        BSD-2-Clause
URL:            https://github.com/syndtr/gocapability
VCS:            git:https://github.com/syndtr/gocapability
#!RemoteAsset:  sha256:4993ab545cd5832080c4dfcfa9e71b3ed7ebe7e51454c1ac711cf06e5b5ad923
Source0:        https://github.com/syndtr/gocapability/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/syndtr/gocapability) = %{version}

%description
Gocapability provides Linux capability support for Go programs.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
