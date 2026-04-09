# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dockercfg
%define go_import_path  github.com/cpuguy83/dockercfg

Name:           go-github-cpuguy83-dockercfg
Version:        0.3.2
Release:        %autorelease
Summary:        Library to load docker CLI configs, auths, etc w/ minimal deps
License:        MIT
URL:            https://github.com/cpuguy83/dockercfg
#!RemoteAsset
Source0:        https://github.com/cpuguy83/dockercfg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cpuguy83/dockercfg) = %{version}

%description
Go library to load docker CLI configs, auths, etc. with minimal deps. So
far the only deps are on the stdlib.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
