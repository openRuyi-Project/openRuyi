# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           go-evdev
%define go_import_path  github.com/holoplot/go-evdev
%global commit_id       ab1d56a1fe83d276fa8273cd74fa844c6367a4a2

Name:           go-github-holoplot-go-evdev
Version:        0+git20261023.ab1d56a
Release:        %autorelease
Summary:        Pure Go bindings for Linux input events
License:        MIT
URL:            https://github.com/holoplot/go-evdev
#!RemoteAsset:  sha256:57c41c954b29467982e16cc6bd9bcbeb9e19e22c5636bbb813e895df675cc643
Source0:        https://github.com/holoplot/go-evdev/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/holoplot/go-evdev) = %{version}

%description
Go interfaces for Linux evdev devices and events without CGO dependencies.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
