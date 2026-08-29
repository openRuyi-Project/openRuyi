# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-osc52
%define go_import_path  github.com/aymanbagabas/go-osc52/v2

Name:           go-github-aymanbagabas-go-osc52-v2
Version:        2.0.1
Release:        %autorelease
Summary:        OSC52 clipboard helper library for Go
License:        MIT
URL:            https://github.com/aymanbagabas/go-osc52
#!RemoteAsset:  sha256:dad92f43db3cd17e7395db59533283b5888c2780fa1b2cb67344a9feaa3291e0
Source0:        https://github.com/aymanbagabas/go-osc52/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aymanbagabas/go-osc52/v2) = %{version}

%description
This package provides OSC52 clipboard helper library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
