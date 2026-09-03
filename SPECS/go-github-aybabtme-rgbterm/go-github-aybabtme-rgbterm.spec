# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rgbterm
%define go_import_path  github.com/aybabtme/rgbterm
%define commit_id       cc83f3b3ce5911279513a46d6d3316d67bedaa54

Name:           go-github-aybabtme-rgbterm
Version:        0+git20260720.cc83f3b
Release:        %autorelease
Summary:        RGB and 256-color terminal text helpers for Go
License:        MIT AND BSD-2-Clause
URL:            https://github.com/aybabtme/rgbterm
#!RemoteAsset:  sha256:18a0abf828dcd7f89d0a713c6c171e4e059ca1d72dcbd45fe260af141cea2849
Source0:        https://github.com/aybabtme/rgbterm/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aybabtme/rgbterm) = %{version}

%description
rgbterm provides helpers for rendering foreground and background text colors
using the 256-color terminal palette.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
