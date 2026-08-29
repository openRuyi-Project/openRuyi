# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mighty
%define go_import_path  github.com/icza/mighty
%define commit_id       cfd07d671de60f8c16c2833ce36bafb6f6c83c7f

Name:           go-github-icza-mighty
Version:        0+git20260716.cfd07d6
Release:        %autorelease
Summary:        Lightweight extension to Go's testing package
License:        Apache-2.0
URL:            https://github.com/icza/mighty
VCS:            git:https://github.com/icza/mighty.git
#!RemoteAsset:  sha256:1ba704924d398a6c880f811a7d136c3819519056ac1bba37648fa319f4598720
Source0:        https://github.com/icza/mighty/archive/%{commit_id}.tar.gz#/mighty-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n mighty-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/icza/mighty) = %{version}

%description
Mighty is a lightweight extension to Go's testing package that removes
repetitive assertion code while keeping tests readable.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
