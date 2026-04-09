# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           joincontext
%define go_import_path  github.com/LK4D4/joincontext
%define commit_id 1724345da6d5bcc8b66fefb843b607ab918e175c

Name:           go-github-lk4d4-joincontext
Version:        0+git20171026.1724345
Release:        %autorelease
Summary:        Join contexts like never before!
License:        MIT
URL:            https://github.com/lk4d4/joincontext
#!RemoteAsset
Source0:        https://github.com/lk4d4/joincontext/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/lk4d4/joincontext) = %{version}

Requires:       go(golang.org/x/net)

%description
Package joincontext provides a way to combine two contexts. For example
it might be useful for grpc server to cancel all handlers in addition to
provided handler context.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
