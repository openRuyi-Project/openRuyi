# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-rendezvous
%define go_import_path  github.com/dgryski/go-rendezvous
%define commit_id       9f7001d12a5f0021fd3283525f888b5814ccee27

Name:           go-github-dgryski-go-rendezvous
Version:        0+git20260823.9f7001d
Release:        %autorelease
Summary:        Rendezvous hashing implementation for Go
License:        MIT
URL:            https://github.com/dgryski/go-rendezvous
#!RemoteAsset:  sha256:9180c6abef7b9269ef951245b73b2f23b1b80a2826dd032c80c80753b162ef06
Source0:        https://github.com/dgryski/go-rendezvous/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dgryski/go-rendezvous) = %{version}

%description
Package rendezvous implements rendezvous hashing for Go.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
