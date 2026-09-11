# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-clone
%define go_import_path  github.com/huandu/go-clone

Name:           go-github-huandu-go-clone
Version:        1.7.3
Release:        %autorelease
Summary:        Deep and shallow cloning of Go values
License:        MIT
URL:            https://github.com/huandu/go-clone
VCS:            git:https://github.com/huandu/go-clone.git
#!RemoteAsset:  sha256:1daa0d255cda33afaa70a6d63bef03bdb5a24fb210d5108d52e695c6d57b0e38
Source0:        https://github.com/huandu/go-clone/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/huandu/go-assert)

Provides:       go(%{go_import_path}) = %{version}

%description
This library creates deep or shallow copies of Go values, with support for
custom clone functions and allocators. The source includes its generic API
and the upstream tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
