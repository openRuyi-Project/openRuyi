# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-dnsstamps
%define go_import_path  github.com/jedisct1/go-dnsstamps
%define commit_id       6579dc73e4a24adff7def08165a50d81609f4759

Name:           go-github-jedisct1-go-dnsstamps
Version:        0+git20261118.6579dc7
Release:        %autorelease
Summary:        DNS Stamps library for Go
License:        MIT
URL:            https://github.com/jedisct1/go-dnsstamps
#!RemoteAsset:  sha256:2fbb611e130232a193d08202cd351d935b3edc969edbb4ab905b7186fe9b73b5
Source0:        https://github.com/jedisct1/go-dnsstamps/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jedisct1/go-dnsstamps) = %{version}

%description
DNS Stamps library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
