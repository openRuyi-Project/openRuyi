# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ioctl
%define go_import_path  github.com/dennwc/ioctl
%define git_commit      01780425206817ff049d3eef4327d3f28e04450f

Name:           go-github-dennwc-ioctl
Version:        1.0.1+git20181021.0178042
Release:        %autorelease
Summary:        Go helpers for Linux ioctl calls
License:        MIT
URL:            https://github.com/dennwc/ioctl
#!RemoteAsset:  sha256:c6d64b75ca5d8d3d52077ebff31a3b381ccf2a0bb312d7045b4d566d2b0bc789
Source0:        %{url}/archive/%{git_commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{git_commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dennwc/ioctl) = %{version}

%description
Go helpers for issuing Linux ioctl calls with typed request values.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
